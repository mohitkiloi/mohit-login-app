pipeline {
    agent any

    environment {
        // Set environment variables if needed
        APP_ENV = 'development'
    }

    stages {

        stage('Checkout SCM') {
            steps {
                checkout scm
            }
        }

        stage('Clone Repo') {
            steps {
                git 'https://github.com/mohitkiloi/mohit-login-app.git'
            }
        }

        stage('Setup Python Env') {
            steps {
                bat 'python -m venv venv'
                bat '.\\venv\\Scripts\\activate && pip install --upgrade pip'
                bat '.\\venv\\Scripts\\activate && pip install -r requirements.txt'
            }
        }

        stage('Run Flask App') {
            steps {
                bat '''
                    call .\\venv\\Scripts\\activate
                    start /B python app.py
                    timeout /t 30
                '''
            }
        }
    }

    post {
        always {
            echo 'Cleaning up workspace...'
        }
        success {
            echo 'Pipeline completed successfully 🎉'
        }
        failure {
            echo 'Pipeline failed 💥'
        }
    }
}
