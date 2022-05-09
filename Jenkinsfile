//Jenkinsfile (Declarative Pipeline)
pipeline {
    agent { docker { image 'python:latest' } }
    stages {
        stage ('set up venv and dependencies') {
            steps {
                sh 'python -m venv tests'
                sh '. ./tests/bin/activate'
                sh 'python -m pip install -r ./flask/server/requirements.txt'
                echo 'pip install successfull'
            }
        }
        stage('python tests') {
            steps {
                echo 'running pytests'
            }
        }
        stage('build') {
            steps {
                sh 'python --version'
            }
        }
    }
}