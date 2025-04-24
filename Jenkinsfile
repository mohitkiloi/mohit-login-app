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
                powershell '''
                    Write-Host "⚙️  Starting Flask app in background..."
                    Start-Process -FilePath "venv\\Scripts\\python.exe" -ArgumentList "app.py"
                    Start-Sleep -Seconds 100
                    Write-Host "⏹️  Time limit reached. Ending build..."
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
