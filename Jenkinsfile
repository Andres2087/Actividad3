pipeline {
    agent any
    environment {
        GITHUB_CREDENTIALS_ID = 'github-token' // ID del token configurado
        GITHUB_REPO = 'Andres2087/Actividad3' // Reemplaza con tu usuario y repositorio
        GIT_COMMIT = env.GIT_COMMIT
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
                bat 'C:\\Users\\andre\\python3.13\\python.exe test5_selenium.py'
            }
        }   
    }
    post {
        always {
            echo 'Pipeline finalizado.'
        }
        success {
            echo 'Todos los tests pasaron correctamente.'
            updateGitHubCommitStatus('success', 'Pipeline completado con éxito')
        }
        failure {
            echo 'La ejecución del pipeline falló. Enviando correo electrónico...'
            updateGitHubCommitStatus('failure', 'Pipeline falló')
            mail to: 'andres2078@gmail.com',
                subject: 'Fallo en la ejecución de Jenkins Pipeline',
                body: 'El pipeline de Jenkins ha fallado en la rama develop. Revisa los logs para más detalles.'
        }
    }
}

def updateGitHubCommitStatus(state, description) {
    withCredentials([string(credentialsId: env.GITHUB_CREDENTIALS_ID, variable: 'GITHUB_TOKEN')]) {
        sh """
            curl -X POST -H "Authorization: token ${GITHUB_TOKEN}" \
                -d '{
                    "state": "${state}",
                    "target_url": "${env.BUILD_URL}",
                    "description": "${description}",
                    "context": "Jenkins Pipeline"
                }' \
                https://api.github.com/repos/${env.GITHUB_REPO}/statuses/${env.GIT_COMMIT}
        """
    }
}
