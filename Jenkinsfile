
pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                echo 'Checking out ACEest DevOps Rollback project'
                checkout scm
            }
        }

        stage('Install Dependencies') {
            steps {
                dir('flask-app') {
                    bat 'python -m pip install -r requirements.txt'
                }
            }
        }

        stage('Run Automated Tests') {
            steps {
                dir('flask-app') {
                    bat 'python -m pytest -v'
                }
            }
        }

        stage('Build Docker Image') {
            steps {
                dir('flask-app') {
                    bat 'docker build -t aceest-fitness-gym .'
                }
            }
        }
    }

    post {
        success {
            echo 'ACEest CI pipeline completed successfully'
        }
        failure {
            echo 'Pipeline failed. Check the failed stage in Console Output.'
        }
    }
}
