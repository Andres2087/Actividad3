pipeline {
    agent any
    environment {
        GITHUB_TOKEN = credentials('github-token') // Referencia al token de GitHub
    }
    stages {
        stage('Preparar Entorno') {
            steps {
                setGitHubStatus('IN_PROGRESS', 'Preparando el entorno')
                echo 'Instalando dependencias...'
                bat 'C:\\Users\\andre\\python3.13\\python.exe -m pip install -r requirements.txt'
            }
        }
        stage('Ejecutar Tests') {
            steps {
                setGitHubStatus('IN_PROGRESS', 'Ejecutando pruebas')
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
            setGitHubStatus('SUCCESS', 'Todos los tests pasaron correctamente.')
        }
        failure {
            setGitHubStatus('FAILURE', 'Falló la ejecución del pipeline.')
            mail to: 'andres2078@gmail.com',
                subject: 'Fallo en la ejecución de Jenkins Pipeline',
                body: 'El pipeline de Jenkins ha fallado en la rama develop. Revisa los logs para más detalles.'
        }
    }
}

def setGitHubStatus(status, description) {
    withCredentials([string(credentialsId: 'github-token', variable: 'GITHUB_TOKEN')]) {
        sh """
        curl -X POST -H "Authorization: token $GITHUB_TOKEN" -H "Accept: application/vnd.github.v3+json" \
        https://api.github.com/repos/Andres2087/Actividad3/statuses/${env.GIT_COMMIT} \
        -d '{
            "state": "${status.toLowerCase()}",
            "target_url": "${env.BUILD_URL}",
            "description": "${description}",
            "context": "Jenkins Pipeline"
        }'
        """
    }
}
