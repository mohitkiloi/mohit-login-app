pipeline {
    agent any

    environment {
        VENV_DIR = 'venv'
    }

    stages {

        stage('Clone Repo') {
            steps {
                git branch: 'main', url: 'https://github.com/mohitkiloi/mohit-login-app.git'
            }
        }

        stage('Setup Python Env') {
            steps {
                bat "python -m venv ${env.VENV_DIR}"
                bat ".\\${env.VENV_DIR}\\Scripts\\activate && pip install --upgrade pip"
                // If you have a requirements.txt file, uncomment below:
                // bat ".\\${env.VENV_DIR}\\Scripts\\activate && pip install -r requirements.txt"
            }
        }

        stage('Run Flask App') {
            steps {
                bat ".\\${env.VENV_DIR}\\Scripts\\activate && start /MIN python app.py && timeout /t 30"
            }
        }
    }

    post {
        always {
            echo '🧹 Cleanup done. Pipeline finished.'
        }
        success {
            echo '✅ Success! App ran and finished correctly.'
        }
        failure {
            echo '❌ Something went wrong. Check the logs.'
        }
    }
}
