# AWS DevOps CI/CD Django Deployment

![Architecture Diagram](docs/architecture-diagram.png)
![Build Status](https://img.shields.io/badge/build-passing-brightgreen)
![License](https://img.shields.io/badge/license-MIT-blue)

## 📋 Overview

A production-ready DevOps project demonstrating automated deployment of a Django application to AWS using Infrastructure as Code (Terraform) and CI/CD pipelines (Jenkins). This project showcases modern cloud architecture, security best practices, and automated deployment workflows.

### 🎯 Key Features

- **Infrastructure as Code**: Complete AWS infrastructure defined in Terraform
- **CI/CD Pipeline**: Automated build, test, and deployment using Jenkins
- **High Availability**: Multi-AZ deployment with Application Load Balancer
- **Security**: VPC isolation, security groups, secrets management
- **Containerization**: Docker-based application deployment
- **Database**: Managed RDS PostgreSQL in private subnet
- **Static Files**: S3 + CloudFront for static asset delivery
- **Monitoring**: CloudWatch logs and metrics

## 🏗️ Architecture

```
┌──────────────────────────────────────────────────────────────┐
│                         GitHub                               │
│                    (Source Control)                          │
└────────────────────┬─────────────────────────────────────────┘
                     │
                     ▼
┌──────────────────────────────────────────────────────────────┐
│                        Jenkins                               │
│  • Checkout Code    • Build & Test    • Security Scan        │
│  • Build Docker     • Terraform Plan  • Deploy               │
└────────────────────┬─────────────────────────────────────────┘
                     │
                     ▼
┌──────────────────────────────────────────────────────────────┐
│                    AWS Infrastructure                        │
│                                                              │
│  ┌─────────────────────────────────────────────────────┐     │
│  │  VPC (10.0.0.0/16)                                  │     │
│  │                                                     │     │
│  │  ┌──────────────┐           ┌─────────────────┐     │     │
│  │  │ Public       │           │ Private         │     │     │
│  │  │ Subnets      │           │ Subnets         │     │     │
│  │  │              │           │                 │     │     │
│  │  │ • ALB        │◄────────► │ • EC2 (Django)  │     │     │
│  │  │ • NAT GW     │           │ • RDS (Postgres)│     │     │
│  │  │ • Bastion    │           │                 │     │     │
│  │  └──────────────┘           └─────────────────┘     │     │
│  │                                                     │     │
│  └─────────────────────────────────────────────────────┘     │
│                                                              │
│  Other Services: ECR │ S3 │ CloudWatch │ Systems Manager     │
└──────────────────────────────────────────────────────────────┘
```

## 🛠️ Technology Stack

### Backend & Application
- **Python 3.11** - Programming language
- **Django 4.2** - Web framework
- **PostgreSQL** - Database
- **Gunicorn** - WSGI HTTP Server
- **Docker** - Containerization

### Infrastructure & DevOps
- **Terraform** - Infrastructure as Code
- **Jenkins** - CI/CD automation
- **AWS Services**:
  - EC2 (Compute)
  - RDS (Database)
  - VPC (Networking)
  - ALB (Load Balancing)
  - S3 (Static files)
  - ECR (Container registry)
  - CloudWatch (Monitoring)
  - Systems Manager (Configuration)

### Tools & Testing
- **pytest** - Testing framework
- **flake8** - Code linting
- **black** - Code formatting
- **bandit** - Security scanning
- **safety** - Dependency vulnerability scanning

## 📁 Project Structure

```
aws-devops-cicd-django-deployment/
├── django-app/                 # Django application
│   ├── config/                # Django configuration
│   ├── tasks/                 # Example app (task manager)
│   ├── requirements.txt       # Python dependencies
│   ├── Dockerfile            # Container definition
│   └── manage.py
│
├── terraform/                 # Infrastructure as Code
│   ├── main.tf               # Main Terraform configuration
│   ├── variables.tf          # Input variables
│   ├── outputs.tf            # Output values
│   ├── modules/              # Reusable Terraform modules
│   │   ├── vpc/
│   │   ├── ec2/
│   │   ├── rds/
│   │   └── s3/
│   └── terraform.tfvars.example
│
├── jenkins/                   # CI/CD pipeline
│   ├── Jenkinsfile           # Main pipeline
│   └── Jenkinsfile.test      # Test pipeline
│
├── docs/                      # Documentation
│   ├── architecture-diagram.png
│   ├── setup-guide.md
│   └── troubleshooting.md
│
├── scripts/                   # Utility scripts
│   ├── deploy.sh
│   └── rollback.sh
│
└── README.md
```

## 🚀 Getting Started

### Prerequisites

- AWS Account with appropriate permissions
- AWS CLI configured
- Terraform >= 1.6.0
- Docker installed
- Jenkins server (or use Docker to run Jenkins)
- Python 3.11+
- PostgreSQL (for local development)

### Local Development Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/Srivenkatesh03/aws-devops-cicd-django-deployment.git
   cd aws-devops-cicd-django-deployment
   ```

2. **Set up Python environment**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r django-app/requirements.txt
   ```

3. **Configure environment variables**
   ```bash
   cd django-app
   cp .env.example .env
   # Edit .env with your local database credentials
   ```

4. **Run migrations**
   ```bash
   python manage.py migrate
   python manage.py createsuperuser
   ```

5. **Run development server**
   ```bash
   python manage.py runserver
   ```
   Visit http://localhost:8000

### AWS Infrastructure Deployment

1. **Configure Terraform variables**
   ```bash
   cd terraform
   cp terraform.tfvars.example terraform.tfvars
   # Edit terraform.tfvars with your values
   ```

2. **Initialize Terraform**
   ```bash
   terraform init
   ```

3. **Review the plan**
   ```bash
   terraform plan
   ```

4. **Apply infrastructure**
   ```bash
   terraform apply
   ```

5. **Note the outputs**
   ```bash
   terraform output
   ```

### Jenkins Pipeline Setup

1. **Install Jenkins plugins**:
   - Pipeline
   - AWS Steps
   - Docker Pipeline
   - Git

2. **Configure AWS credentials** in Jenkins

3. **Create a new Pipeline job**:
   - Point to your repository
   - Use `jenkins/Jenkinsfile`

4. **Configure webhooks** in GitHub to trigger builds

## 📊 CI/CD Pipeline Flow

```
1. Code Push → GitHub
2. Webhook triggers Jenkins
3. Jenkins Pipeline:
   ├─ Checkout code
   ├─ Install dependencies
   ├─ Run linting (flake8, black)
   ├─ Run tests (pytest)
   ├─ Security scan (bandit, safety)
   ├─ Build Docker image
   ├─ Push to ECR
   ├─ Terraform plan
   ├─ Manual approval (for prod)
   ├─ Terraform apply
   ├─ Deploy to EC2
   └─ Health check
4. Application live on AWS
```

## 🧪 Testing

```bash
# Run all tests
python manage.py test

# Run with coverage
coverage run --source='.' manage.py test
coverage report

# Run linting
flake8 .
black --check .

# Security scan
bandit -r django-app/
```

## 📈 Monitoring & Logging

- **CloudWatch Logs**: Application and system logs
- **CloudWatch Metrics**: CPU, memory, network
- **ALB Health Checks**: Application health monitoring
- **Custom Metrics**: Django performance metrics

Access logs:
```bash
aws logs tail /aws/ec2/django-app --follow
```

## 🔒 Security Features

- ✅ VPC with public/private subnets
- ✅ Security groups with least privilege
- ✅ RDS in private subnet (no public access)
- ✅ Secrets management via AWS Systems Manager
- ✅ HTTPS support (certificate management)
- ✅ Regular dependency vulnerability scanning
- ✅ Docker image scanning
- ✅ IAM roles with minimal permissions

## 💰 Cost Estimation

Approximate monthly costs (us-east-1, basic setup):
- EC2 (t3.micro): $7.50
- RDS (db.t3.micro): $12.50
- ALB: $16.20
- NAT Gateway: $32.40
- S3/CloudWatch: $2-5

**Total: ~$70-75/month**

💡 **Tip**: Use AWS Free Tier where applicable, destroy resources when not needed.

## 🐛 Troubleshooting

### Common Issues

**1. Terraform apply fails**
```bash
# Check AWS credentials
aws sts get-caller-identity

# Validate Terraform
terraform validate
```

**2. Application won't start**
```bash
# Check EC2 instance logs
aws ssm start-session --target i-xxxxx
sudo docker logs django-app
```

**3. Database connection issues**
```bash
# Verify security group rules
# Check RDS endpoint in .env file
# Ensure EC2 can reach RDS (test with telnet/nc)
```

See [docs/troubleshooting.md](docs/troubleshooting.md) for more details.

## 📚 Learning Outcomes

Building this project demonstrates:

- ✅ **AWS Cloud Architecture**: VPC design, security groups, multi-tier architecture
- ✅ **Infrastructure as Code**: Terraform modules, state management, best practices
- ✅ **CI/CD**: Jenkins pipelines, automated testing, deployment strategies
- ✅ **Containerization**: Docker, ECR, container orchestration
- ✅ **Security**: AWS security best practices, secrets management
- ✅ **Monitoring**: CloudWatch, logging, alerting
- ✅ **Version Control**: Git workflows, branching strategies

## 🚧 Future Enhancements

- [ ] Implement Auto Scaling Groups
- [ ] Add CloudFront CDN
- [ ] Implement blue-green deployment
- [ ] Add Kubernetes/ECS deployment option
- [ ] Implement automated backups
- [ ] Add monitoring dashboards (Grafana)
- [ ] Implement log aggregation (ELK stack)
- [ ] Add infrastructure testing (Terratest)

## 📝 License

This project is licensed under the MIT License - see LICENSE file for details.

## 👤 Author

**Srivenkatesh R**
- GitHub: [@Srivenkatesh03](https://github.com/Srivenkatesh03)
- LinkedIn: [Add your LinkedIn]

## 🙏 Acknowledgments

- AWS Documentation
- Terraform Registry
- Django Documentation
- Jenkins Documentation

---

**Note**: This is a learning/portfolio project. For production use, additional security hardening, monitoring, and disaster recovery measures should be implemented.