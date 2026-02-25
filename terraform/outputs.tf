output "bastion_public_ip" {
  value = aws_instance.bastion.public_ip
}

output "private_server_ip" {
  value = aws_instance.private_ec2.private_ip
}

output "jenkins_server_ip" {
  value = aws_instance.jenkins.public_ip
}

output "alb_dns_name" {
  value       = aws_alb.app_alb.dns_name
}

output "alb_url" {
  value       = "http://${aws_alb.app_alb.dns_name}"
}

output "cloudwatch_dashboard_url" {
  description = "CloudWatch Dashboard URL"
  value       = "https://console.aws.amazon.com/cloudwatch/home?region=ap-south-1#dashboards:name=devops-django-dashboard"
}

output "cloudwatch_log_group" {
  description = "CloudWatch Log Group"
  value       = aws_cloudwatch_log_group.django_app_logs.name
}

output "sns_topic_arn" {
  description = "SNS Topic for Alarms"
  value       = aws_sns_topic.cloudwatch_alarms.arn
}