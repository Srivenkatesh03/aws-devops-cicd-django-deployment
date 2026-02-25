output "bastion_public_ip" {
  value = aws_instance.bastion.public_ip
}

output "private_server_ip" {
  value = aws_instance.private_ec2.private_ip
}

output "jenkins_server_ip" {
  value = aws_instance.jenkins.public_ip
}