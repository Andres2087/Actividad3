pipeline {
    agent any
    stages {
        stage('Preparar Entorno') {
            steps {
                echo 'Instalando dependencias...'
                bat 'C:\\Users\\andre\\python3.13\\python.exe -m pip install -r requirements.txt'
            }
        }
        stage('Ejecutar Tests') {
            steps {
                echo 'Ejecutando tests automatizados...'
                bat 'C:\\Users\\andre\\python3.13\\python.exe test1_selenium.py'
                bat 'C:\\Users\\andre\\python3.13\\python.exe test2_selenium.py'
                bat 'C:\\Users\\andre\\python3.13\\python.exe test3_selenium.py'
                bat 'C:\\Users\\andre\\python3.13\\python.exe test4_selenium.py'
            }
        }   
    }
    post {
        always {
            echo 'Pipeline finalizado.'
        }
        success {
            script {
                // Notificar el éxito a GitHub
                githubCommitStatus(context: 'build', state: 'success', targetUrl: 'https://5b29-186-119-217-255.ngrok-free.app/job/EjemplosMuestra/job/Desarrollo/job/job-actividad3/')
            }
            echo 'Todos los tests pasaron correctamente.'
        }
        failure {
            script {
                // Notificar el fallo a GitHub
                githubCommitStatus(context: 'build', state: 'failure', targetUrl: 'https://5b29-186-119-217-255.ngrok-free.app/job/EjemplosMuestra/job/Desarrollo/job/job-actividad3/')
            }
            echo 'La ejecución del pipeline falló. Enviando correo electrónico...'
            mail to: 'andres2078@gmail.com',
                 subject: 'Fallo en la ejecución de Jenkins Pipeline',
                 body: 'El pipeline de Jenkins ha fallado en la rama develop. Revisa los logs para más detalles.'
        }
    }
}
