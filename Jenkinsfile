pipeline {
    agent any
    triggers {
        githubPush() // Este trigger requiere un webhook en GitHub
    }
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
        stage('Notificar a GitHub') {
            steps {
                script {
                    def status = currentBuild.result == 'SUCCESS' ? 'success' : 'failure'
                    setGitHubCommitStatus(
                        context: 'ci/selenium-tests',
                        state: status,
                        targetUrl: "https://jenkins.example.com/job/${JOB_NAME}/${BUILD_NUMBER}",
                        description: "Automated Selenium tests"
                    )
                }
            }
        }
    }
    post {
        always {
            echo 'Pipeline finalizado.'
        }
        success {
            echo 'Todos los tests pasaron correctamente.'
        }
        failure {
            echo 'La ejecución del pipeline falló. Enviando correo electrónico...'
            mail to: 'andres2078@gmail.com',
                subject: 'Fallo en la ejecución de Jenkins Pipeline',
                body: 'El pipeline de Jenkins ha fallado en la rama develop. Revisa los logs para más detalles.'
        }
    }
}
