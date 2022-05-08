//Jenkinsfile (Declarative Pipeline)
pipeline {
    agent { docker { image 'python:latest' } }
    stages {
        stage('python tests') {
            steps {
                sh 'pip install -r ./flask/server/requirements.txt --user'
                echo 'pip install successfull'
            }
        }
        stage('build') {
            steps {
                sh 'python --version'
            }
        }
    }
}