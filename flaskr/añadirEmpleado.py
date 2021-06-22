
from flask import request
from flask import Blueprint
import pdb
from . import db
import face_recognition
import pickle

bpAñadir = Blueprint('anadir', __name__)

#Extensiones permitidas
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

@bpAñadir.route('/add', methods = ['GET','POST'])
def add():
    if request.method == 'GET':
        return "es un get"
    
    if request.method == 'POST':
        # Desde la parte de params de postman, usamos args
        # id = request.args.get('idfoto')
        #Se puede obtener desde un formulario, usamos form
        idUser = request.form.get("iduser")
        idFoto = request.form.get("idfoto")
        
        
        #Desde la opción body de postman, aqui añadimos la imagen
        file = request.files['file']
        #Cargamos la imagen en un array numpy
        img = face_recognition.load_image_file(file)

        img_encoding = face_recognition.face_encodings(img)[0]

        cur = db.get_db().cursor()
        # pdb.set_trace()
        # cur.execute("INSERT INTO users (idUser, idFoto, stringFoto) VALUES (?,?,?)",
        #             (idUser, idFoto, pickle.dumps(img_encoding)))

        # print(img_encoding)
        # print("=======================================")
        # print(pickle.dumps(img_encoding))
        
        # db.get_db().commit()
        # cur.close()

        #Como mucho devolverá una fila
        fila = cur.execute("SELECT * FROM users WHERE idUser="+ idUser + " AND idFoto=" + idFoto).fetchall()
        if len(fila) != 0:
            cur.execute("DELETE FROM users WHERE  idUser="+ idUser + " AND idFoto=" + idFoto)
            cur.execute("INSERT INTO users (idUser, idFoto, stringFoto) VALUES (?,?,?)",
                    (idUser, idFoto, pickle.dumps(img_encoding)))
            db.get_db().commit()
            cur.close()
            return "fila actualizada"
        else:
            cur.execute("INSERT INTO users (idUser, idFoto, stringFoto) VALUES (?,?,?)",
                    (idUser, idFoto, pickle.dumps(img_encoding)))
            db.get_db().commit()
            cur.close()
            return "fila añadida"

   
