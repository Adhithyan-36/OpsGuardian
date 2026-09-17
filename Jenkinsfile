pipeline {
    agent any

    stages {
        stage('Test') {
            steps {
                echo 'Testing OpsGuardian application'
            }
        }

        stage('Build Docker Image') {
            steps {
                bat 'docker build -t opsguardian-app:latest .'
            }
        }

        stage('Deploy to Kubernetes') {
            steps {
                bat 'kubectl apply -f k8s\\deployment.yaml'
                bat 'kubectl apply -f k8s\\service.yaml'
            }
        }
    }
}