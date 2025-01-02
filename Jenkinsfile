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
                setGitHubPullRequestStatus(
                    context: 'Jenkins Build',
                    status: 'SUCCESS',
                    description: 'Build completed successfully.'
                )
            }
            echo 'Todos los tests pasaron correctamente.'
        }
        failure {
            script {
                setGitHubPullRequestStatus(
                    context: 'Jenkins Build',
                    status: 'SUCCESS',
                    description: 'Build completed successfully.'
                )
            }
            echo 'La ejecución del pipeline falló.'
            mail to: 'andres2078@gmail.com',
                 subject: 'Fallo en la ejecución de Jenkins Pipeline',
                 body: """El pipeline de Jenkins ha fallado en la rama develop.
                          Revisa los logs para más detalles:
                          ${env.BUILD_URL}"""
        }
    }
}
