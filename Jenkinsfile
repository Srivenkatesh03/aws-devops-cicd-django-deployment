pipeline {
    agent any

    environment {
        DOCKER_IMAGE = "srivenkatesh04/sms-app"
        CONTAINER_NAME = "sms-app"
    }

    stages {

        stage('Checkout') {
            steps {
                git branch: 'main',
                    url: 'https://github.com/Srivenkatesh03/aws-devops-cicd-django-deployment.git'
                echo 'Repo cloned'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t $DOCKER_IMAGE:latest -f docker/Dockerfile .'
            }
        }

        stage('Push to DockerHub') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'dockerhub', usernameVariable: 'USER', passwordVariable: 'PASS')]) {
                    sh '''
                        echo $PASS | docker login -u $USER --password-stdin
                        docker push $DOCKER_IMAGE:latest
                    '''
                }
            }
        }

        stage('Deploy to Private EC2') {
        steps {
            withCredentials([
                sshUserPrivateKey(credentialsId: 'ec2-ssh-key', keyFileVariable: 'SSH_KEY', usernameVariable: 'SSH_USER'),
                string(credentialsId: 'private-ip', variable: 'PRIVATE_IP'),
                string(credentialsId: 'bastion-ip', variable: 'BASTION_IP')
            ]) {
                sh """
                    chmod 600 $SSH_KEY

                    echo "Creating SSH config"
                    mkdir -p ~/.ssh

                    echo "Host bastion" > ~/.ssh/config
                    echo "    HostName $BASTION_IP" >> ~/.ssh/config
                    echo "    User $SSH_USER" >> ~/.ssh/config
                    echo "    IdentityFile $SSH_KEY" >> ~/.ssh/config
                    echo "    StrictHostKeyChecking no" >> ~/.ssh/config

                    echo "Host private" >> ~/.ssh/config
                    echo "    HostName $PRIVATE_IP" >> ~/.ssh/config
                    echo "    User $SSH_USER" >> ~/.ssh/config
                    echo "    IdentityFile $SSH_KEY" >> ~/.ssh/config
                    echo "    ProxyJump bastion" >> ~/.ssh/config
                    echo "    StrictHostKeyChecking no" >> ~/.ssh/config

                    echo "Creating project folder in private EC2"
                        ssh private "mkdir -p ~/app"

                        echo "Copy docker-compose"
                        scp docker-compose.yml private:~/app/

                        echo "Deploying app"
                        ssh private '
                        cd ~/app &&
                        docker pull srivenkatesh04/sms-app:latest &&
                        docker compose down || true &&
                        docker compose up -d &&
                        docker ps
                        '
                """
            }
        }
    }

        stage('Health Check') {
            steps {
                withCredentials([
                    sshUserPrivateKey(credentialsId: 'ec2-ssh-key', keyFileVariable: 'SSH_KEY', usernameVariable: 'SSH_USER'),
                    string(credentialsId: 'private-ip', variable: 'PRIVATE_IP'),
                    string(credentialsId: 'bastion-ip', variable: 'BASTION_IP')
                ]) {
                    sh """
                        chmod 600 $SSH_KEY

                        echo "Checking app health..."

                        ssh -o StrictHostKeyChecking=no \
                            -i $SSH_KEY \
                            -J $SSH_USER@$BASTION_IP \
                            $SSH_USER@$PRIVATE_IP \
                            "curl -f http://localhost:8000 || exit 1"
                    """
                }
            }
        }
    }

    post {
        success {
            echo 'DEPLOY SUCCESS'
        }
        failure {
            echo 'DEPLOY FAILED'
        }
    }
}