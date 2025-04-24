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
                bat "python -m venv %VENV_DIR%"
                bat "%VENV_DIR%\\Scripts\\python.exe -m pip install --upgrade pip"
                // Uncomment below if using requirements.txt
                // bat "%VENV_DIR%\\Scripts\\python.exe -m pip install -r requirements.txt"
            }
        }

        stage('Run Flask App') {
            steps {
                bat '''
                    echo Starting Flask App
                    %VENV_DIR%\\Scripts\\python.exe app.py
                '''
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
