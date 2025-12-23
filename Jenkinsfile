pipeline {
    agent any

    environment {
        IMAGE_NAME = "ashwani12340987/urban-flow-api"
        IMAGE_TAG  = "ci-${BUILD_NUMBER}"
    }

    stages {

        stage('Checkout') {
            steps {
                echo 'Checking out source code...'
                checkout scm
            }
        }

        stage('Build') {
            steps {
                echo 'Building Docker image...'
                sh """
                   docker build -t ${IMAGE_NAME}:${IMAGE_TAG} .
                """
            }
        }

        stage('Test') {
            steps {
                echo 'Running dummy tests...'
                sh """
                   echo "No real tests implemented yet"
                   echo "Dummy test passed"
                """
                // Example real test:
                // sh "python -m pytest"
            }
        }

        stage('Security Scan') {
            steps {
                echo 'Running Trivy security scan...'
                sh """
                   trivy image --exit-code 1 --severity CRITICAL ${IMAGE_NAME}:${IMAGE_TAG}
                """
            }
        }
    }

    post {
        always {
            echo 'Cleaning workspace and Docker images...'
            sh """
               docker rmi ${IMAGE_NAME}:${IMAGE_TAG} || true
               docker system prune -f || true
            """
            cleanWs()
        }

        success {
            echo 'Pipeline completed successfully ✅'
        }

        failure {
            echo 'Pipeline failed ❌'
        }
    }
}