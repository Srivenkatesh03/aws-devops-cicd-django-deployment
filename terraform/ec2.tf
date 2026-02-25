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

  user_data = <<-EOF
                #!/bin/bash
                apt update -y
                apt install docker.io -y
                systemctl start docker
                systemctl enable docker
                usermod -aG docker ubuntu
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