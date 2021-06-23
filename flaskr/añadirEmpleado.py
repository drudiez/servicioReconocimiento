
from flask import request
from flask import Blueprint
import pdb
from . import db
import face_recognition
import pickle

bpAñadir = Blueprint('anadir', __name__)
@bpAñadir.route('/add', methods = ['POST'])
def add():

    if request.method == 'POST':
        # Desde la parte de params de postman, usamos args
        # id = request.args.get('idfoto')

        if 'file' not in request.files or 'iduser' not in request.form or 'idfoto' not in request.form:
            return db.error_400, 400

        idUser = request.form.get("iduser")
        idFoto = request.form.get("idfoto")
        file = request.files['file']

        if not db.allowed_file(file.filename):
            return db.error_415, 415
        
        
        #Cargamos la imagen en un array numpy
        img = face_recognition.load_image_file(file)

        img_encoding = face_recognition.face_encodings(img)[0]

        cur = db.get_db().cursor()

        fila = cur.execute("SELECT * FROM users WHERE idUser=" + idUser + " AND idFoto=" + idFoto).fetchall()
        if len(fila) != 0:
            cur.execute("DELETE FROM users WHERE  idUser=" + idUser + " AND idFoto=" + idFoto)
            cur.execute("INSERT INTO users (idUser, idFoto, stringFoto) VALUES (?,?,?)",
                    (idUser, idFoto, pickle.dumps(img_encoding)))
            db.get_db().commit()
            cur.close()
            return db.update, 200
        else:
            cur.execute("INSERT INTO users (idUser, idFoto, stringFoto) VALUES (?,?,?)",
                    (idUser, idFoto, pickle.dumps(img_encoding)))
            db.get_db().commit()
            cur.close()
            return db.add, 201

