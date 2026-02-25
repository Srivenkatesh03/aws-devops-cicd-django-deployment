# AWS DevOps CI/CD Django Deployment

![Build Status](https://img.shields.io/badge/build-passing-brightgreen)
![Terraform](https://img.shields.io/badge/terraform-v1.5+-purple)
![AWS](https://img.shields.io/badge/AWS-cloud-orange)
![Django](https://img.shields.io/badge/django-6.0-green)

## 📋 Overview

A production-ready DevOps project demonstrating automated deployment of a **Django Student Management System** to AWS using **Infrastructure as Code (Terraform)** and **CI/CD pipelines (Jenkins)**. This project showcases modern cloud architecture, security best practices, containerization, and automated deployment workflows.

### 🎯 Key Features

- ✅ **Infrastructure as Code**: Complete AWS infrastructure provisioned with Terraform
- ✅ **CI/CD Pipeline**: Automated build and deployment using Jenkins with SSH-based deployment
- ✅ **High Availability**: Multi-AZ Application Load Balancer for traffic distribution
- ✅ **Security**: VPC isolation with public/private subnets, bastion host architecture
- ✅ **Containerization**: Docker-based application deployment with Docker Compose
- ✅ **Database**: PostgreSQL database running in Docker
- ✅ **Zero-Downtime Deployment**: Rolling deployment strategy via Jenkins

---

## 🏗️ Architecture

```
┌──────────────────────────────────────────────────────────────┐
│                         GitHub                               │
│                    (Source Control)                          │
└────────────────────┬─────────────────────────────────────────┘
                     │
                     ▼
┌──────────────────────────────────────────────────────────────────┐
│                        Jenkins                                   │
│  • Checkout Code    • Build Docker    • Push to DockerHub        │
│  • Deploy via SSH   • Health Check                               │
└──────────���─────────┬─────────────────────────────────────────┘
                         │
                         ▼
┌──────────────────────────────────────────────────────────────┐
│                    AWS Infrastructure                        │
│                                                              │
│  ┌─────────────────────────────────────────────────────┐     │
│  │  VPC (10.0.0.0/16)                                  │     │
│  │                                                     │     │
│  │  ┌──────────────────┐       ┌─────────────────┐     │     │
│  │  │  Public Subnets  │       │ Private Subnet  │     │     │
│  │  │  (Multi-AZ)      │       │                 │     │     │
│  │  │                  │       │                 │     │     │
│  │  │ • ALB            │───────▶ • EC2 (Django) │     │      |
│  │  │ • Jenkins        │       │ • PostgreSQL    │     │     │
│  │  │ • Bastion Host   │       │   (Docker)      │     │     │
│  │  │ • NAT Gateway    │       │                 │     │     │
│  │  └──────────────────┘       └─────────────────┘     │     │
│  │                                                     │     │
│  └─────────────────────────────────────────────────────┘     │
│                                                              │
└──────────────────────────────────────────────────────────────┘
```

---

## 🛠️ Technology Stack

### Backend & Application
- **Python 3.13** - Programming language
- **Django 6.0** - Web framework
- **PostgreSQL 16** - Database
- **Gunicorn** - WSGI HTTP Server
- **Docker & Docker Compose** - Containerization

### Infrastructure & DevOps
- **Terraform** - Infrastructure as Code
- **Jenkins** - CI/CD automation
- **Docker Hub** - Container registry
- **AWS Services**:
  - **VPC** - Virtual Private Cloud with public/private subnets
  - **EC2** - Compute instances (Jenkins, Bastion, Application)
  - **ALB** - Application Load Balancer (Multi-AZ)
  - **NAT Gateway** - Outbound internet access for private subnet
  - **S3** - Terraform state storage
  - **DynamoDB** - Terraform state locking

---

## 📁 Project Structure

```
aws-devops-cicd-django-deployment/
├── app/                           # Django Student Management System
│   ├── core/                      # Core app (students, marks, attendance)
│   ├── student_manager/           # Django project settings
│   ├── templates/                 # HTML templates
│   ├── static/                    # Static files (CSS, JS)
│   ├── media/                     # User uploads
│   ├── manage.py                  # Django management
│   ├── requirements.txt           # Python dependencies
│   └── wait_for_db.py            # Database connection helper
│
├── terraform/                     # Infrastructure as Code
│   ├── backend.tf                 # Terraform backend (S3 + DynamoDB)
│   ├── provider.tf                # AWS provider configuration
│   ├── variables.tf               # Input variables
│   ├── outputs.tf                 # Output values
│   ├── vpc.tf                     # VPC and Internet Gateway
│   ├── subnet.tf                  # Subnets, route tables, NAT Gateway
│   ├── security.tf                # Security groups
│   ├── ec2.tf                     # EC2 instances (private, bastion, jenkins)
│   ├── alb.tf                     # Application Load Balancer
│   └── TargetGroup.tf            # Target Group and Listener
│
├��─ docker/                        # Docker configuration
│   ├── Dockerfile                 # Application container image
│   ├── docker-compose.yaml        # Multi-container setup (app + db)
│   └── .dockerignore             # Docker ignore rules
│
├── Jenkinsfile                    # CI/CD pipeline definition
├── .gitignore                     # Git ignore rules
└── README.md                      # This file
```

---

## 🚀 Getting Started

### Prerequisites

- **AWS Account** with appropriate permissions
- **AWS CLI** configured (`aws configure`)
- **Terraform** >= 1.5.0
- **Docker** and Docker Compose
- **SSH Key Pair** named `devops-key` in AWS (or update in terraform)
- **Jenkins Server** (deployed via this project's Terraform)
- **DockerHub Account** (for storing container images)

---

### 🔧 Step 1: Clone the Repository

```bash
git clone https://github.com/Srivenkatesh03/aws-devops-cicd-django-deployment.git
cd aws-devops-cicd-django-deployment
```

---

### 🏗️ Step 2: Deploy AWS Infrastructure

#### 1. **Create S3 Bucket for Terraform State** (One-time setup)

```bash
aws s3 mb s3://srivenkatesh-terraform-state --region ap-south-1
```

#### 2. **Create DynamoDB Table for State Locking** (One-time setup)

```bash
aws dynamodb create-table \
  --table-name terraform-lock \
  --attribute-definitions AttributeName=LockID,AttributeType=S \
  --key-schema AttributeName=LockID,KeyType=HASH \
  --billing-mode PAY_PER_REQUEST \
  --region ap-south-1
```

#### 3. **Initialize Terraform**

```bash
cd terraform
terraform init
```

#### 4. **Review Infrastructure Plan**

```bash
terraform plan
```

#### 5. **Apply Infrastructure**

```bash
terraform apply
```

**Note the outputs:**
- `bastion_public_ip` - Bastion host public IP
- `jenkins_server_ip` - Jenkins server public IP
- `private_server_ip` - Private EC2 instance IP
- `alb_url` - Application Load Balancer URL

---

### 🔐 Step 3: Configure Jenkins

#### 1. **Access Jenkins**

```bash
# Get initial admin password
ssh -i devops-key.pem ubuntu@<jenkins_server_ip>
sudo cat /var/lib/jenkins/secrets/initialAdminPassword
```

Open: `http://<jenkins_server_ip>:8080`

#### 2. **Install Required Plugins**
- Pipeline
- Git
- SSH Agent
- Docker Pipeline
- Credentials Binding

#### 3. **Configure Jenkins Credentials**

Go to: **Manage Jenkins → Credentials → Global → Add Credentials**

| Credential ID | Type                          | Description                      |
|---------------|-------------------------------|----------------------------------|
| `dockerhub`   | Username with password        | DockerHub credentials            |
| `ec2-ssh-key` | SSH Username with private key | EC2 SSH key (devops-key.pem)     |
| `private-ip`  | Secret text                   | Private EC2 instance IP          |
| `bastion-ip`  | Secret text                   | Bastion host public IP           |
| `sms-env`     | Secret file                   | `.env` file with Django settings |

#### 4. **Create `.env` File** (for `sms-env` credential)

```env
SECRET_KEY=your-django-secret-key-here
DEBUG=False
ALLOWED_HOSTS=*

DB_ENGINE=django.db.backends.postgresql
DB_NAME=student_db
DB_USER=admin
DB_PASSWORD=admin
DB_HOST=db
DB_PORT=5432
```

#### 5. **Create Jenkins Pipeline**

1. Click **New Item** → **Pipeline**
2. Name: `django-cicd-pipeline`
3. Under **Pipeline**:
   - Definition: **Pipeline script from SCM**
   - SCM: **Git**
   - Repository URL: `https://github.com/Srivenkatesh03/aws-devops-cicd-django-deployment.git`
   - Branch: `main`
   - Script Path: `Jenkinsfile`
4. Save

---

## 📊 CI/CD Pipeline Flow

The Jenkins pipeline automates the entire deployment process:

```
┌─────────────────────────────────────────────────────────┐
│  Stage 1: Checkout                                      │
│  • Clone repository from GitHub                         │
└────────────────────┬────────────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────────┐
│  Stage 2: Build Docker Image                            │
│  • docker build -t srivenkatesh04/sms-app:latest        │
└────────────────────┬────────────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────────┐
│  Stage 3: Push to DockerHub                             │
│  • docker login + docker push                           │
└────────────────────┬────────────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────────┐
│  Stage 4: Deploy to Private EC2                         │
│  • SSH via bastion host (ProxyJump)                     │
│  • Transfer docker-compose.yaml and .env                │
│  • Pull latest image                                    │
│  • docker compose down && docker compose up -d          │
└────────────────────┬────────────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────────┐
│  Stage 5: Health Check                                  │
│  • curl http://localhost:8000/                          │
│  • Verify application is running                        │
└─────────────────────────────────────────────────────────┘
```

**Key Features:**
- ✅ Automated Docker image building
- ✅ Container registry push (DockerHub)
- ✅ Secure SSH deployment via bastion host
- ✅ Zero-downtime deployment with Docker Compose
- ✅ Automated health checks

---

## 🔒 Security Architecture

### Network Security
- ✅ **VPC Isolation**: Custom VPC with isolated subnets
- ✅ **Public Subnet**: ALB, Jenkins, Bastion Host
- ✅ **Private Subnet**: Application server (no direct internet access)
- ✅ **NAT Gateway**: Allows private subnet to pull Docker images
- ✅ **Bastion Host**: Secure SSH access to private instances

### Security Groups

| Security Group | Ingress Rules                         | Purpose            |
|----------------|---------------------------------------|--------------------|
| `alb-sg`       | 80 (HTTP), 443 (HTTPS) from 0.0.0.0/0 | Public ALB access  |
| `private-sg`   | 22 (SSH), 8000 from VPC               | Application server |
| `bastion-sg`   | 22 (SSH) from 0.0.0.0/0               | Jump server access |
| `jenkins-sg`   | 22 (SSH), 8080, 80 from 0.0.0.0/0     | Jenkins CI/CD      |

### Access Patterns
```
Internet → ALB (port 80) → Private EC2 (port 8000)
Developer → Bastion (SSH) → Private EC2 (SSH)
Jenkins → Bastion (ProxyJump) → Private EC2 (Deploy)
```

---

## 💰 Cost Estimation

**Approximate monthly costs** (ap-south-1 region):

| Service            | Configuration             | Monthly Cost       |
|--------------------|---------------------------|--------------------|
| EC2 (t3.micro) × 3 | Private, Bastion, Jenkins | ~$22.50            |
| ALB                | Application Load Balancer | ~$16.20            |
| NAT Gateway        | Data transfer             | ~$32.40            |
| S3                 | Terraform state           | ~$0.50             |
| DynamoDB           | State locking             | ~$0.00 (free tier) |

**Total: ~$70-75/month**

💡 **Cost Optimization Tips:**
- Use AWS Free Tier where applicable
- Stop non-production instances when not in use
- Use `terraform destroy` to tear down resources

---

## 🧪 Local Development Setup

### Option 1: Using Docker Compose

```bash
cd docker

# Create .env file
cat > .env <<EOF
SECRET_KEY=dev-secret-key
DEBUG=True
ALLOWED_HOSTS=*

DB_ENGINE=django.db.backends.postgresql
DB_NAME=student_db
DB_USER=admin
DB_PASSWORD=admin
DB_HOST=db
DB_PORT=5432
EOF

# Start containers
docker-compose up -d

# Run migrations
docker exec -it sms_web python manage.py migrate
docker exec -it sms_web python manage.py createsuperuser

# Access at http://localhost:8000
```

### Option 2: Manual Setup

```bash
# Create virtual environment
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r app/requirements.txt

# Set up PostgreSQL database locally
# Update .env with local database credentials

# Run migrations
cd app
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver

# Access at http://localhost:8000
```

---

## 🐛 Troubleshooting

### Issue 1: Terraform Apply Fails

```bash
# Check AWS credentials
aws sts get-caller-identity

# Validate Terraform configuration
cd terraform
terraform validate

# Check state lock
aws dynamodb scan --table-name terraform-lock
```

### Issue 2: Jenkins Cannot SSH to Private EC2

```bash
# Verify SSH key is added to Jenkins credentials
# Test SSH connection from Jenkins server
ssh -o ProxyJump=ubuntu@<bastion-ip> ubuntu@<private-ip>

# Check security groups allow port 22
```

### Issue 3: Application Not Accessible via ALB

```bash
# Check target health
aws elbv2 describe-target-health \
  --target-group-arn <target-group-arn>

# Verify Docker container is running
ssh -J ubuntu@<bastion-ip> ubuntu@<private-ip>
docker ps
docker logs sms-app

# Check ALB security group allows traffic
```

### Issue 4: Database Connection Error

```bash
# Check PostgreSQL container status
docker ps | grep postgres
docker logs sms_db

# Verify .env file has correct DB credentials
cat ~/app/.env
```

---

## 📚 What This Project Demonstrates

### DevOps Skills
- ✅ **Infrastructure as Code**: Terraform for reproducible infrastructure
- ✅ **CI/CD Pipelines**: Automated deployment with Jenkins
- ✅ **Containerization**: Docker and Docker Compose
- ✅ **Cloud Architecture**: AWS VPC, subnets, security groups
- ✅ **Security Best Practices**: Bastion host, private subnets, security groups
- ✅ **State Management**: Remote state in S3 with DynamoDB locking
- ✅ **Load Balancing**: Multi-AZ Application Load Balancer
- ✅ **SSH Automation**: ProxyJump configuration for secure access

### AWS Services
- VPC and Networking
- EC2 Compute
- Application Load Balancer
- Security Groups
- S3 and DynamoDB
- Multiple Availability Zones

---

## 🚧 Future Enhancements

Potential improvements to make this project production-ready:

- [ ] **Add RDS PostgreSQL** (managed database instead of containerized)
- [ ] **CloudWatch Monitoring** (metrics, logs, alarms)
- [ ] **Auto Scaling Group** (horizontal scaling based on load)
- [ ] **S3 + CloudFront** (static file hosting and CDN)
- [ ] **AWS Secrets Manager** (secure credential storage)
- [ ] **HTTPS/SSL** (ACM certificate + HTTPS listener on ALB)
- [ ] **Automated Testing** (pytest, flake8, security scanning in pipeline)
- [ ] **Blue-Green Deployment** (zero-downtime deployment strategy)
- [ ] **ECS/EKS** (container orchestration at scale)
- [ ] **Terraform Modules** (modular, reusable infrastructure code)

---

## 📝 License

This project is licensed under the MIT License.

---

## 👤 Author

**Srivenkatesh R**

- 🐙 GitHub: [@Srivenkatesh03](https://github.com/Srivenkatesh03)
- 💼 LinkedIn: https://www.linkedin.com/in/srivenkatesh49175
- 📧 Email: srivenkatesh49175@gmail.com

---

## 🙏 Acknowledgments

- [Django Documentation](https://docs.djangoproject.com/)
- [Terraform AWS Provider](https://registry.terraform.io/providers/hashicorp/aws/latest/docs)
- [Jenkins Documentation](https://www.jenkins.io/doc/)
- [Docker Documentation](https://docs.docker.com/)
- [AWS Documentation](https://docs.aws.amazon.com/)

---

