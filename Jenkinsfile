pipeline { 
    agent any

    environment {
        GITURL = "https://github.com/Avinjay/Flask_Pytest_Jenkins"
    }
    
    stages {
        
        stage('Git Clone') {
            steps {
                git branch: 'main', url: "${env.GITURL}"
            }
        }

        stage('Build') {
            steps {
                sh 'python3 -m venv venv'
                sh '. venv/bin/activate && pip install -r requirements.txt'
            }
        }

        stage('Test') {
            steps {
                sh '. venv/bin/activate && pytest'
            }
        }

        stage('Deploy') {
            when {
                expression {
                    currentBuild.result == null || currentBuild.result == 'SUCCESS'
                }
            }
            steps {
                sh '. venv/bin/activate && nohup python app.py &'
            }
        }
    }

    post {
        success {
            mail to: 'avimer1412@gmail.com',
                 subject: "SUCCESS: Build #${env.BUILD_NUMBER}",
                 body: " Build passed."
        }
        failure {
            mail to: 'avimer1412@gmail.com',
                 subject: "FAILURE: Build #${env.BUILD_NUMBER}",
                 body: "The build failed."
        }
    }
}
