pipeline {
    agent any
    environment {
        CI = 'true'
        registry = "lokesh773/sgmc" 

        registryCredential = 'dockerscred' 

        dockerImage = ''
    }
    stages {
        stage('Cloning Git') {
            steps {
                git branch: 'main',url:'https://github.com/Lokesh773/smart_garce_mark_calcluator.git'    
            }
        }
        stage('Install dependencies') {
            steps {
                sh 'pip install django pillow'
            }
        }
    }
    }      
        
       
