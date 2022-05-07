//Jenkinsfile (Declarative Pipeline)
pipeline {
    agent { docker { image 'python:3.10.4-alpine' } }
    stages {
        stage ('setup') {
            sh 'apt-get update && apt-get upgrade -y && apt-get install -y git'
        }
        stage('python tests') {
            steps {
                sh 'pip install -r ./flask/server/requirements.txt'
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