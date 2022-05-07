//Jenkinsfile (Declarative Pipeline)
pipeline {
    agent { docker { image 'python:3.10.4-alpine' } }
    stages {
        stage('python tests') {
            sh 'pip install -r ./flask/server/requirements.txt'
            echo 'pip install successfull'
        }
        stage('build') {
            steps {
                sh 'python --version'
            }
        }
    }
}