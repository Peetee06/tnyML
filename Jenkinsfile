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
                sh "${VENV_PATH}pip install -r ./flask/server/requirements.txt --cache-dir ./.pipcache/"
                echo "pip install successfull"
            }
        }
        stage('build') {
            steps {
                sh "${VENV_PATH}python --version"
            }
        }
        stage('python tests') {
            steps {
                sh ". ./${VENV_PATH}activate && pytest ./flask/server/test --junitxml=./test_xml_report/output.xml"
            }
        }
    }
}