pipeline {
    agent any
    environment {
        VENV_DIR = 'venv'
    }

    stages {
        stage('Checkout SCM') {
            steps {
                checkout scm
            }
        }

        stage('Clone Repo') {
            steps {
                git branch: 'main', url: 'https://github.com/mohitkiloi/mohit-login-app.git'
            }
        }

        stage('Setup Python Env') {
            steps {
                bat "python -m venv %VENV_DIR%"
                bat "%VENV_DIR%\\Scripts\\activate && pip install --upgrade pip"
                bat "%VENV_DIR%\\Scripts\\activate && pip install -r requirements.txt"
            }
        }

        stage('Run Flask App') {
            steps {
                bat '''
                    echo Running Flask app in background...
                    start /MIN %VENV_DIR%\\Scripts\\python.exe app.py
                    call timeout /t 30 /nobreak
                    echo Auto-stopping after 30 seconds.
                '''
            }
        }
    }

    post {
        always {
            echo '🧹 Cleanup done. Pipeline finished.'
        }
        failure {
            echo '❌ Something went wrong. Check the logs.'
        }
    }
}
