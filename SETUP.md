Required Jenkins Plugins

To successfully build and deploy your urban-flow app using Jenkins, include the following plugins:

Docker Pipeline Plugin

Enables Jenkins to build, run, and push Docker images from a Jenkins Pipeline (supports docker.build(), docker.withRegistry(), etc.).

This plugin is essential when building Docker images inside Jenkins jobs. 
Jenkins Plugins

Credentials Plugin

Lets you securely store and manage sensitive data like usernames, passwords, or tokens for Docker Hub and other services.

Provides a way to inject credentials into your pipeline without hardcoding them. 
Medium

Git Plugin

Allows Jenkins to clone source code from your GitHub repository (your urban-flow project).

Required for the checkout scm or git ... steps. 
Medium

Optional but useful:

Pipeline: Multibranch Plugin (for multi-branch pipelines)

Blue Ocean Plugin (for better visual pipeline UI)

NodeJS Plugin (if you want Jenkins to run npm install/npm test without Docker)

2️ How to Securely Store Docker Hub Credentials in Jenkins

You should never hardcode your Docker Hub credentials inside a Jenkinsfile. Instead, do the following:

Steps to Store Credentials

Go to Jenkins Dashboard → Manage Jenkins → Manage Credentials

Choose the domain (usually (global) for simple setups)

Click Add Credentials

Fill out the form:

Kind: Username with password

Username: Your Docker Hub username

Password: Your Docker Hub password or access token

ID: e.g., docker-hub-credentials

Description: Docker Hub Registry Credentials

Click Save

This will securely encrypt your credentials in Jenkins.

Jenkins Example

pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps {
                git url: 'https://github.com/nehanayak07/urban-flow.git'
            }
        }

        stage('Docker Login') {
            steps {
                withCredentials([usernamePassword(
                    credentialsId: 'docker-hub-credentials',
                    usernameVariable: 'DOCKER_USER',
                    passwordVariable: 'DOCKER_PASS'
                )]) {
                    sh 'echo $DOCKER_PASS | docker login -u $DOCKER_USER --password-stdin'
                }
            }
        }

        stage('Build Image') {
            steps {
                script {
                    dockerImage = docker.build("yourdockerhubusername/urban-flow:${env.BUILD_NUMBER}")
                }
            }
        }

        stage('Push Image') {
            steps {
                script {
                    docker.withRegistry('', 'docker-hub-credentials') {
                        dockerImage.push()
                    }
                }
            }
        }
    }
}
