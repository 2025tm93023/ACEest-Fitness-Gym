
pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                echo 'Checking out ACEest DevOps project'
                checkout scm
            }
        }

        stage('Install Dependencies') {
            steps {
                dir('flask-app') {
                    sh 'python3 -m pip install -r requirements.txt'
                }
            }
        }

        stage('Run Automated Tests') {
            steps {
                dir('flask-app') {
                    sh 'python3 -m pytest -v'
                }
            }
        }

        stage('Build Docker Image') {
            steps {
                dir('flask-app') {
                    sh 'docker build -t aceest-fitness-gym .'
                }
            }
        }
    }

    post {
        success {
            echo 'ACEest CI pipeline completed successfully'
        }
        failure {
            echo 'Pipeline failed. Check Console Output.'
        }
    }
}
