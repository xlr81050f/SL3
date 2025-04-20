pipeline {
    agent any
    
    stages {
        stage('Build') {
            steps {
                echo 'Building..'
                sh 'docker-compose build'
            }
        }
        
        stage('Test') {
            steps {
                echo 'Testing..'
                sh 'docker-compose run --rm web python manage.py test'
            }
        }
        
        stage('Deploy') {
            steps {
                echo 'Deploying....'
                sh 'docker-compose down'
                sh 'docker-compose up -d'
            }
        }
    }
    
    post {
        always {
            echo 'Cleaning up...'
            sh 'docker-compose down'
        }
        
        success {
            echo 'Deployment successful!'
        }
        
        failure {
            echo 'Deployment failed!'
        }
    }
}