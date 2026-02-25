resource "aws_alb" "app_alb" {
  name = "devops-alb"
  internal = false
  load_balancer_type = "application"
  security_groups = [aws_security_group.alb_sg.id]
  subnets = [aws_subnet.Public_subnet.id,aws_subnet.Public_subnet2.id]

  tags = {
    Name = "devops-alb"
  }
}