pipeline {
    agent any
    
    stages {
        stage('Clone') {
            steps {
                // Add your build steps here
            }
        }
        
        stage('Build') {
            steps {
                // Add your test steps here
            }
        }
        
        stage('Deploy') {
            steps {
                sh(if docker ps -a --format '{{.Names}}' | grep -q "^sicei$"; then
                    docker stop sicei
                    docker rm sicei
                fi)
                sh(docker build -t sicei-${GIT_BRANCH}:1.0.0-${BUILD_NUMBER} .)
                sh(docker run -d -p 7000:8000 sicei-${GIT_BRANCH}:1.0.0-${BUILD_NUMBER})
            }
        }
    }
}