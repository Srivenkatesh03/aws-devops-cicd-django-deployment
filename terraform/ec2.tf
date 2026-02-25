data "aws_ami" "ubuntu" {
  most_recent = true

  filter {
    name = "name"
    values = [ "ubuntu/images/hvm-ssd/ubuntu-jammy-22.04-amd64-server-*" ]
  }

  filter {
    name = "virtualization-type"
    values = ["hvm"]
  }

  owners = ["099720109477"]
}

resource "aws_instance" "private_ec2" {
  ami = data.aws_ami.ubuntu.id
  instance_type = var.instance_type
  subnet_id = aws_subnet.private_subnet.id
  vpc_security_group_ids = [aws_security_group.private_sg.id]
  key_name = "devops-key"
  associate_public_ip_address = false
  iam_instance_profile        = aws_iam_instance_profile.ec2_profile.name

  user_data = <<-EOF
                #!/bin/bash
                apt update -y
                apt install docker.io -y
                systemctl start docker
                systemctl enable docker
                usermod -aG docker ubuntu

                 wget https://s3.amazonaws.com/amazoncloudwatch-agent/ubuntu/amd64/latest/amazon-cloudwatch-agent.deb
                dpkg -i -E ./amazon-cloudwatch-agent.deb
                
                cat > /opt/aws/amazon-cloudwatch-agent/etc/config.json <<'CWCONFIG'
                {
                  "metrics": {
                    "namespace": "CWAgent",
                    "metrics_collected": {
                      "mem": {
                        "measurement": [
                          {
                            "name": "mem_used_percent",
                            "rename": "MemoryUtilization",
                            "unit": "Percent"
                          }
                        ],
                        "metrics_collection_interval": 60
                      },
                      "disk": {
                        "measurement": [
                          {
                            "name": "used_percent",
                            "rename": "DiskUtilization",
                            "unit": "Percent"
                          }
                        ],
                        "metrics_collection_interval": 60,
                        "resources": [
                          "*"
                        ]
                      }
                    }
                  },
                  "logs": {
                    "logs_collected": {
                      "files": {
                        "collect_list": [
                          {
                            "file_path": "/var/log/syslog",
                            "log_group_name": "/aws/ec2/django-app",
                            "log_stream_name": "{instance_id}/syslog"
                          },
                          {
                            "file_path": "/var/log/docker.log",
                            "log_group_name": "/aws/ec2/docker",
                            "log_stream_name": "{instance_id}/docker"
                          }
                        ]
                      }
                    }
                  }
                }
                CWCONFIG
                
                /opt/aws/amazon-cloudwatch-agent/bin/amazon-cloudwatch-agent-ctl \
                  -a fetch-config \
                  -m ec2 \
                  -s \
                  -c file:/opt/aws/amazon-cloudwatch-agent/etc/config.json
                
                systemctl enable amazon-cloudwatch-agent
                EOF
              

  tags = {
    Name = "private-ec2"
  }  
}



resource "aws_instance" "bastion" {
  ami = data.aws_ami.ubuntu.id
  instance_type = var.instance_type
  subnet_id = aws_subnet.Public_subnet.id
  vpc_security_group_ids = [aws_security_group.bastion_sg.id]
  key_name = "devops-key"
  associate_public_ip_address = true

  tags = {
    Name = "bastion-host"
  }
}


resource "aws_instance" "jenkins" {
  ami = data.aws_ami.ubuntu.id
  instance_type = var.instance_type
  subnet_id = aws_subnet.Public_subnet.id
  vpc_security_group_ids = [aws_security_group.jenkins_sg.id]
  key_name = "devops-key"
  associate_public_ip_address = true

  tags = {
    Name = "jenkis-server"
  }
}