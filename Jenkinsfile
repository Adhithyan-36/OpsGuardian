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
                bat 'docker build -t opsguardian-app .'
            }
        }
    }
}