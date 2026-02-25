
resource "aws_s3_bucket" "alb_logs" {
  bucket = "devops-alb-logs-${data.aws_caller_identity.current.account_id}"

  tags = {
    Name = "alb-access-logs"
  }
}

resource "aws_s3_bucket_policy" "alb_logs_policy" {
  bucket = aws_s3_bucket.alb_logs.id

  policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Effect = "Allow"
        Principal = {
          AWS = "arn:aws:iam::718504428378:root"  # ELB service account for ap-south-1
        }
        Action   = "s3:PutObject"
        Resource = "${aws_s3_bucket.alb_logs.arn}/*"
      }
    ]
  })
}

resource "aws_alb" "app_alb" {
  name               = "devops-alb"
  internal           = false
  load_balancer_type = "application"
  security_groups    = [aws_security_group.alb_sg.id]
  subnets            = [aws_subnet.Public_subnet.id, aws_subnet.Public_subnet2.id]

  access_logs {
    bucket  = aws_s3_bucket.alb_logs.bucket
    enabled = true
  }

  tags = {
    Name = "devops-alb"
  }
}

data "aws_caller_identity" "current" {}
