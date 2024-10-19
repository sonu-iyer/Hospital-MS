pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git url: 'https://github.com/your-username/hospital-management-system.git'
            }
        }
        stage('Build Docker Image') {
            steps {
                script {
                    docker.build("hms-app")
                }
            }
        }
        stage('Run Tests') {
            steps {
                script {
                    docker.run("hms-app", "python -m unittest discover")
                }
            }
        }
        stage('Deploy') {
            steps {
                script {
                    // Stop and remove any existing container
                    sh 'docker stop hms-app || true && docker rm hms-app || true'

                    // Run the Docker container
                    sh 'docker run -d --name hms-app -p 80:80 hms-app'
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
