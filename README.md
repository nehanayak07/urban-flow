# Urban Flow Traffic API – Jenkins CI/CD Pipeline

## Project Overview
Urban Flow Traffic API is a Python-based REST API that simulates traffic flow data.  
The main objective of this project is to demonstrate a **Jenkins CI/CD pipeline** that automates building, deploying, and verifying the application.

This project focuses on **Continuous Integration and Continuous Deployment (CI/CD)** using **Jenkins**.

---

## Objective
- Automate application build and deployment
- Remove environment mismatch issues
- Ensure consistent and repeatable deployments
- Demonstrate Jenkins pipeline implementation

---

## Jenkins Role in This Project
Jenkins acts as the **automation server** that performs the following tasks:

1. Pulls the source code from GitHub
2. Builds the Docker image for the API
3. Deploys the application using Docker Compose
4. Verifies the running containers
5. Reports pipeline status

---

## Project Structure
```bash
urban-flow-api/
│
├── Jenkinsfile # Jenkins pipeline definition
├── Dockerfile # Application containerization
├── docker-compose.yml # Multi-container setup
├── app/ # Application source code
└── README.md # Project documentation
```

---

## Jenkins Pipeline Workflow

- GitHub → Jenkins → Docker Build → Docker Compose → Verification

Each code change triggers the Jenkins pipeline to ensure automated deployment.

---

## Jenkinsfile (Pipeline Configuration)

The CI/CD pipeline is defined using a **Declarative Jenkinsfile**.

### Pipeline Stages

| Stage Name | Description |
|----------|------------|
| Checkout Code | Pulls the latest code from GitHub |
| Build Docker Image | Builds the API Docker image |
| Run Application | Starts API, database, and Redis containers |
| Verify Application | Confirms all containers are running |

---

## Jenkinsfile Example

```groovy
pipeline {
    agent any

    stages {

        stage('Checkout Code') {
            steps {
                git 'https://github.com/your-username/urban-flow-api.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t urban-flow-api-api .'
            }
        }

        stage('Deploy Application') {
            steps {
                sh 'docker-compose up -d'
            }
        }

        stage('Verify Deployment') {
            steps {
                sh 'docker ps'
            }
        }
    }

    post {
        always {
            echo 'Pipeline execution completed'
        }
    }
}
```
# Jenkins Job Configuration (UI Steps)

- Open Jenkins Dashboard

- Click New Item

- Enter job name → urban-flow-pipeline

- Select Pipeline

- Under Pipeline Configuration:

- Definition: Pipeline script from SCM

- SCM: Git

- Repository URL: GitHub repository URL

- Script Path: Jenkinsfile

- Save and click Build Now

# Pipeline Output

- Docker image is built successfully

- Containers are launched automatically

- Application runs on port 8000

- Jenkins console shows deployment status

# Application Access

- Once the pipeline succeeds:
```bash
http://localhost:8000
```
- Response:
```bash
{
  "status": "Urban Flow API is running 🚦"
}
```
