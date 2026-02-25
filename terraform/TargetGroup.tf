resource "aws_lb_target_group" "app_tg" {
  name = "devops-td"
  port = "8000" 
  protocol = "HTTP"
  vpc_id = aws_vpc.main.id

  health_check {
    path = "/"
    protocol = "HTTP"
    matcher = "200"
    interval = 30
    timeout = 5
    healthy_threshold = 2
    unhealthy_threshold = 3
  }

  tags = {
    Name = "devops-app-tg"
  }
}

resource "aws_lb_target_group_attachment" "app_attach" {
  target_group_arn = aws_lb_target_group.app_tg.arn
  target_id = aws_instance.private_ec2.id
  port = 8000
}

resource "aws_lb_listener" "http" {
  load_balancer_arn = aws_alb.app_alb.arn
  port = 80
  protocol = "HTTP"

  default_action {
    type = "forward"
    target_group_arn = aws_lb_target_group.app_tg.arn
  }
}