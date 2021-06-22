
from flask import request
from flask import Blueprint
import pdb
from . import db
import face_recognition
import pickle

bpAñadir = Blueprint('anadir', __name__)

#Extensiones permitidas
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@bpAñadir.route('/add', methods = ['GET','POST'])
def add():

    if request.method == 'POST':
        # Desde la parte de params de postman, usamos args
        # id = request.args.get('idfoto')

        idUser = request.form.get("iduser")
        idFoto = request.form.get("idfoto")
        file = request.files['file']

        if not allowed_file(file.filename):
            data = {'error': 'extensión de archivo no soportada'}
            return data, 415
        
        if (idUser == None or idFoto == None):
            data = {'error': 'petición incorrecta'}
            return "", 400
        
        #Cargamos la imagen en un array numpy
        img = face_recognition.load_image_file(file)

        img_encoding = face_recognition.face_encodings(img)[0]

        cur = db.get_db().cursor()

        fila = cur.execute("SELECT * FROM users WHERE idUser="+ idUser + " AND idFoto=" + idFoto).fetchall()
        if len(fila) != 0:
            cur.execute("DELETE FROM users WHERE  idUser="+ idUser + " AND idFoto=" + idFoto)
            cur.execute("INSERT INTO users (idUser, idFoto, stringFoto) VALUES (?,?,?)",
                    (idUser, idFoto, pickle.dumps(img_encoding)))
            db.get_db().commit()
            cur.close()
            return "", 200
        else:
            cur.execute("INSERT INTO users (idUser, idFoto, stringFoto) VALUES (?,?,?)",
                    (idUser, idFoto, pickle.dumps(img_encoding)))
            db.get_db().commit()
            cur.close()
            return "", 201

