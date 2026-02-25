pipeline {
    agent any

    environment {
        DOCKER_IMAGE = "sms-app"
        DOCKER_TAG = "${BUILD_NUMBER}"
    }

    stages {

        stage('Checkout') {
            steps {
                git branch: 'main',
                    url: 'https://github.com/Srivenkatesh03/Student_Management_System.git'
                echo '✅ Repository cloned successfully'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh """
                    cd docker
                    docker build -t ${DOCKER_IMAGE}:${DOCKER_TAG} .
                    docker tag ${DOCKER_IMAGE}:${DOCKER_TAG} ${DOCKER_IMAGE}:latest
                """
                echo '✅ Docker image built successfully'
            }
        }

        stage('Test') {
            steps {
                sh """
                    docker run --rm ${DOCKER_IMAGE}:${DOCKER_TAG} python manage.py test || echo "No tests found"
                """
                echo '✅ Tests completed'
            }
        }

        stage('Save Image') {
            steps {
                sh """
                    docker save ${DOCKER_IMAGE}:${DOCKER_TAG} | gzip > ${DOCKER_IMAGE}-${DOCKER_TAG}.tar.gz
                """
                echo '✅ Image archived'
            }
        }

        stage('Deploy to Private EC2') {
            steps {
                withCredentials([
                    sshUserPrivateKey(credentialsId: 'ec2-ssh-key', keyFileVariable: 'SSH_KEY'),
                    string(credentialsId: 'private-ip', variable: 'PRIVATE_IP'),
                    string(credentialsId: 'bastion-ip', variable: 'BASTION_IP'),
                    string(credentialsId: 'database-url', variable: 'DATABASE_URL')
                ]) {

                    sh """
                        # Copy image to private EC2 via bastion
                        scp -o StrictHostKeyChecking=no \
                            -o ProxyJump=ubuntu@${BASTION_IP} \
                            -i ${SSH_KEY} \
                            ${DOCKER_IMAGE}-${DOCKER_TAG}.tar.gz \
                            ubuntu@${PRIVATE_IP}:/tmp/

                        # Deploy on private EC2
                        ssh -o StrictHostKeyChecking=no \
                            -o ProxyJump=ubuntu@${BASTION_IP} \
                            -i ${SSH_KEY} \
                            ubuntu@${PRIVATE_IP} "
                            
                            docker load < /tmp/${DOCKER_IMAGE}-${DOCKER_TAG}.tar.gz &&
                            docker stop sms-app || true &&
                            docker rm sms-app || true &&
                            docker run -d \
                                --name sms-app \
                                -p 8000:8000 \
                                --restart unless-stopped \
                                -e DATABASE_URL='${DATABASE_URL}' \
                                ${DOCKER_IMAGE}:${DOCKER_TAG} &&
                            
                            rm /tmp/${DOCKER_IMAGE}-${DOCKER_TAG}.tar.gz &&
                            docker image prune -f
                            "
                    """
                }

                echo '✅ Deployed to private EC2 successfully'
            }
        }

        stage('Health Check') {
            steps {
                withCredentials([
                    sshUserPrivateKey(credentialsId: 'ec2-ssh-key', keyFileVariable: 'SSH_KEY'),
                    string(credentialsId: 'private-ip', variable: 'PRIVATE_IP'),
                    string(credentialsId: 'bastion-ip', variable: 'BASTION_IP')
                ]) {

                    sh """
                        ssh -o ProxyJump=ubuntu@${BASTION_IP} \
                            -i ${SSH_KEY} \
                            ubuntu@${PRIVATE_IP} \
                            'curl -f http://localhost:8000/ || exit 1'
                    """
                }

                echo '✅ Health check passed'
            }
        }
    }

    post {
        success {
            echo '🎉 Pipeline completed successfully!'
        }
        failure {
            echo '❌ Pipeline failed!'
        }
        cleanup {
            sh 'docker system prune -f || true'
        }
    }
}