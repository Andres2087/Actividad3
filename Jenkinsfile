pipeline {
    agent any
    stages {
        stage('Preparar Entorno') {
            steps {
                echo 'Instalando dependencias'
                sh 'pip install -r requirements.txt'
            }
        }
        
        stage('Ejecución de Pruebas') {
            steps {
                echo 'Ejecutando pruebas automatizadas'
                sh 'python -m unittest discover -s tests'
            }
        }
    }
}
