
from flask import request
from flask import Blueprint
import pdb

from flask.scaffold import F
from . import db
import face_recognition
import pickle

bpReconocer = Blueprint('reconocer', __name__)
@bpReconocer.route('/reconocer', methods = ['GET','POST'])
def add():
    if request.method == 'GET':
        cur = db.get_db().cursor()
        
        filas=cur.execute("SELECT * FROM users").fetchall()
        cur.close()

        #pic es el formato bueno

        pic = pickle.loads(filas[0]['stringFoto'])

        pdb.set_trace()


        for fila in filas:
            print(fila['id'] + fila['stringFoto'])

        
        return "es un get"
    
    if request.method == 'POST':
        # Desde la parte de params de postman, usamos args
        # id = request.args.get('idfoto')
        #Se puede obtener desde un formulario, usamos form
        id = request.form.get("idfoto")
        
        
        #Desde la opción body de postman, aqui añadimos la imagen
        file = request.files['file']
        #Cargamos la imagen en un array numpy
        img = face_recognition.load_image_file(file)

        img_encoding = face_recognition.face_encodings(img)

        cur = db.get_db().cursor()
        
        cur.execute("INSERT INTO users (id,stringFoto) VALUES (?,?)",
                    (id, pickle.dumps(img_encoding)))
        # c=pickle.dumps(img_encoding)
        # d=pickle.load(c)
        
        db.get_db().commit()

        return id + ' imagen'
