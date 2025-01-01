pipeline {
    agent any
    stages {
        
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
