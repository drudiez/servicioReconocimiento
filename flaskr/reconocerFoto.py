
from flask import request
from flask import Blueprint, render_template
import pdb
from . import db
import face_recognition
import pickle
import numpy as np
import sys
bpReconocer = Blueprint('reconocer', __name__)


@bpReconocer.route('/reconocer', methods = ['GET','POST'])
def reconocer():
    if request.method == 'GET':
        cur = db.get_db().cursor()
        filas=cur.execute("SELECT * FROM users").fetchall()
        cur.close()

        known_face_names = []
        idFoto = []
        known_face_encodings = []
        
        for fila in filas:
            known_face_names.append(fila['idUser'])
            idFoto.append(fila['idFoto'])
            known_face_encodings.append(pickle.loads(fila['stringFoto']))
        
        data=[]
        for i in range(len(known_face_encodings)):
            data.append([known_face_names[i] , idFoto[i] , known_face_encodings[i]])

        return render_template('base.html', data=data)
    
    if request.method == 'POST':

        id_json = {'id': 'desconocido'}

        if 'file' not in request.files:
            return db.error_400, 400

        file = request.files['file']

        if not db.allowed_file(file.filename):
            return db.error_415, 415

        img = face_recognition.load_image_file(file)

        #Puede ser que no se detecten caras en la imagen
        try:
            unknown_face_encodings = face_recognition.face_encodings(img)[0]
        except IndexError as e:
            print(e)
            return db.error_400_1, 400


        cur = db.get_db().cursor()
        filas=cur.execute("SELECT * FROM users").fetchall()
        cur.close()

        known_face_ids = []
        idFoto = []
        known_face_encodings = []

        for fila in filas:
            known_face_ids.append(fila['idUser'])
            idFoto.append(fila['idFoto'])
            known_face_encodings.append(pickle.loads(fila['stringFoto']))
        
        #Matches es un array de booleanos, la posición True es la de la persona reconocida
        matches = face_recognition.compare_faces(known_face_encodings,unknown_face_encodings)

        #face_distances es un array con la distancia euclidea de las conocidas a la desconocida
        #la componente con valor mínimo es la que mas se parece
        face_distances = face_recognition.face_distance(known_face_encodings, unknown_face_encodings)
        best_match_index = np.argmin(face_distances)

        if matches[best_match_index]:
            id = known_face_ids[best_match_index]
            id_json['id'] = id

        return id_json, 200
