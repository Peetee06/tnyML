Jenkinsfile (Declarative Pipeline)
pipeline {
    agent { docker { image 'python:3.10.4-alpine' } }
    stages {
        stage('build') {
            steps {
                sh 'python --version'
            }
        }
    }
}