//Jenkinsfile (Declarative Pipeline)
pipeline {
    agent { docker { image 'python:latest' } }
    environment {
        VENV_NAME = 'tests'
        VENV_PATH = "${VENV_NAME}/bin/"
    }
    stages {
        stage ('set up venv and dependencies') {
            steps {
                sh "python -m venv ${VENV_NAME}"
                sh ". ./${VENV_PATH}activate"
                sh "${VENV_PATH}pip install -r ./flask/server/requirements.txt"
                echo "${VENV_PATH}pip install successfull"
            }
        }
        stage('python tests') {
            steps {
                echo 'running pytests'
            }
        }
        stage('build') {
            steps {
                sh "${VENV_PATH}/python --version"
            }
        }
    }
}