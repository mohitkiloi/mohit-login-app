pipeline {
    agent any

    stage('Clone Repo') {
      steps {
        git branch: 'main', url: 'https://github.com/mohitkiloi/mohit-login-app.git'
      }
    }


        stage('Setup Python Env') {
            steps {
                sh 'python -m venv venv'
                sh '. venv/Scripts/activate && pip install -r requirements.txt || pip install flask'
            }
        }

        stage('Run Flask App') {
            steps {
                sh '. venv/Scripts/activate && python app.py > flask_output.log &'
            }
        }
    }

    post {
        always {
            archiveArtifacts artifacts: 'flask_output.log', onlyIfSuccessful: true
        }
    }
}
