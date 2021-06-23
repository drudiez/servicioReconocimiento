# servicioReconocimiento

Primero iniciar el entorno virtual:

    . venv/bin/activate

Crear la BD:

    flask init-db

Para iniciar el servidor debemos ejecutar los siguentes comandos:

    export FLASK_APP=flaskr
    export FLASK_ENV=development
    flask run --host=0.0.0.0


Peticiones:

POST: /add {idfoto, iduser, file}

POST: /reconocer {file}
GET: /reconocer