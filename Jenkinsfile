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
                sh '''
                docker build -t $DOCKER_IMAGE:latest docker/Dockerfile .
                '''
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
                    sshUserPrivateKey(credentialsId: 'ec2-ssh-key', keyFileVariable: 'SSH_KEY'),
                    string(credentialsId: 'private-ip', variable: 'PRIVATE_IP'),
                    string(credentialsId: 'bastion-ip', variable: 'BASTION_IP')
                ]) {

                    sh '''
                    ssh -o StrictHostKeyChecking=no \
                    -o ProxyJump=ubuntu@$BASTION_IP \
                    -i $SSH_KEY ubuntu@$PRIVATE_IP "

                    docker pull $DOCKER_IMAGE:latest &&
                    docker stop $CONTAINER_NAME || true &&
                    docker rm $CONTAINER_NAME || true &&
                    docker run -d -p 8000:8000 --name $CONTAINER_NAME $DOCKER_IMAGE:latest
                    "
                    '''
                }
            }
        }

        stage('Health Check') {
            steps {
                withCredentials([
                    sshUserPrivateKey(credentialsId: 'ec2-ssh-key', keyFileVariable: 'SSH_KEY'),
                    string(credentialsId: 'private-ip', variable: 'PRIVATE_IP'),
                    string(credentialsId: 'bastion-ip', variable: 'BASTION_IP')
                ]) {

                    sh '''
                    ssh -o ProxyJump=ubuntu@$BASTION_IP \
                    -i $SSH_KEY ubuntu@$PRIVATE_IP \
                    "curl -f http://localhost:8000/ || exit 1"
                    '''
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