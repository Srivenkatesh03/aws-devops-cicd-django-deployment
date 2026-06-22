resource "aws_cloudwatch_log_group" "django_app_logs" {
  name              = "/aws/ec2/django-app"
  retention_in_days = 7
}

resource "aws_sns_topic" "cloudwatch_alarms" {
  name = "cloudwatch-alarms-topic"
}

resource "aws_cloudwatch_dashboard" "django_dashboard" {
  dashboard_name = "devops-django-dashboard"

  dashboard_body = jsonencode({
    widgets = [
      {
        type   = "metric"
        x      = 0
        y      = 0
        width  = 12
        height = 6
        properties = {
          metrics = [
            [ "AWS/EC2", "CPUUtilization", "InstanceId", aws_instance.private_ec2.id ]
          ]
          period = 300
          stat   = "Average"
          region = "ap-south-1"
          title  = "Private EC2 CPU Utilization"
        }
      }
    ]
  })
}
