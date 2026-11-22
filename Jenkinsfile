
pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                echo 'Connecting to GitHub...'
                git branch: 'main',
                    url: 'https://github.com/PreranaJaunjal/python-devops-task-manager.git'
            }
        }

        stage('Verify Python') {
            steps {
                sh 'python3 --version'
                sh 'python3 -m pip --version'
            }
        }

        stage('Install Dependencies') {
            steps {
                sh 'python3 -m venv venv'
                sh '. venv/bin/activate && pip install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                sh '. venv/bin/activate && python -m pytest -v'
            }
        }


stage('Build Docker Image') {
    steps {
        echo 'Building Task Manager Docker image...'
        sh 'docker version'
        sh 'docker build -t task-manager-api:${BUILD_NUMBER} .'
    }
}

stage('Build Docker Image') {
    steps {
        echo 'Building Task Manager Docker image...'
        sh 'docker version'
        sh 'docker build -t task-manager-api:${BUILD_NUMBER} .'
    }
}

    }
}
