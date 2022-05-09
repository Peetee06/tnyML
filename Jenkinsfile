//Jenkinsfile (Declarative Pipeline)
pipeline {
    agent { docker { image 'python:latest' } }
    stages {
        stage ('set up venv and dependencies') {
            steps {

            }
        }
        stage('python tests') {
            steps {
                sh 'python -m venv tests'
                sh '. ./tests/bin/activate'
                sh 'python -m pip install -r ./flask/server/requirements.txt'
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