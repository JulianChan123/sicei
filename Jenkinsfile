pipeline {
    agent any
    
    stages {
        stage('Clone') {
            steps {
                checkout scm
            }
        }
        
        stage('Build') {
            steps {
                sh 'echo "Building Docker image..."'
                sh 'docker build -t sicei-${GIT_BRANCH}:1.0.0-${BUILD_NUMBER} .'
            }
        }
        
        stage('Deploy') {
            steps {
                sh '''
                if docker ps -a --format '{{.Names}}' | grep -q "^sicei$"; then
                    docker stop sicei
                    docker rm sicei
                fi
                '''
                sh 'docker run -d -p 7000:8000 sicei-${GIT_BRANCH}:1.0.0-${BUILD_NUMBER}'
            }
        }
    }
}
