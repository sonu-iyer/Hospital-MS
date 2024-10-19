pipeline {
    agent any

    environment {
        DOCKER_IMAGE = "hms-app"
    }

    stages {
        stage('Checkout') {
            steps {
                git url: 'https://github.com/sonu-iyer/Hospital-MS.git'
            }
        }
        stage('Build Docker Image') {
            steps {
                script {
                    docker.build("${DOCKER_IMAGE}")
                }
            }
        }
        stage('Run Tests') {
            steps {
                script {
                    docker.run("${DOCKER_IMAGE}", "python -m unittest discover")
                }
            }
        }
        stage('Push to Docker Hub') {
            steps {
                script {
                    withCredentials([usernamePassword(credentialsId: 'sonalika27', usernameVariable: 'sonalika27', passwordVariable: '7815976825AS')]) {
                        sh "docker login -u sonalika27 -p 7815976825AS"
                        sh "docker tag ${DOCKER_IMAGE} sonalika27/${DOCKER_IMAGE}"
                        sh "docker push sonalika27/${DOCKER_IMAGE}"
                    }
                }
            }
        }
        stage('Deploy') {
            steps {
                script {
                    // Stop and remove existing container
                    sh 'docker stop hms-app || true && docker rm hms-app || true'

                    // Run the Docker container
                    sh "docker run -d --name hms-app -p 80:80 ${DOCKER_IMAGE}"
                }
            }
        }
    }
    post {
        always {
            echo 'Pipeline finished.'
        }
    }
}

