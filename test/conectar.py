import requests


url = 'http://192.168.1.35:5000/add'
url2 = 'http://192.168.1.35:5000/reconocer'

#, 'file': open('test/data/train/ben_afflek/1.jpg', 'rb')
def subirFoto(idUsuario, idFoto, urlFoto):
    data = {'iduser': idUsuario , 'idfoto': idFoto}
    files= {'file': open( urlFoto + str(idFoto) + '.jpg', 'rb')}
    response = requests.post(url, data, files=files)
    print(response.json())
    
def reconocerFoto(urlFoto):
    files= {'file': open(urlFoto, 'rb')}
    return requests.post(url2, files=files)

print("=== AÑADIMOS LAS FOTOS==")
subirFoto(1,1,'test/data/train/ben_afflek/')
subirFoto(1,2,'test/data/train/ben_afflek/')
subirFoto(1,3,'test/data/train/ben_afflek/')
subirFoto(1,4,'test/data/train/ben_afflek/')
subirFoto(1,5,'test/data/train/ben_afflek/')

subirFoto(2,1,'test/data/train/elton_john/')
subirFoto(2,2,'test/data/train/elton_john/')
subirFoto(2,3,'test/data/train/elton_john/')
subirFoto(2,4,'test/data/train/elton_john/')
subirFoto(2,5,'test/data/train/elton_john/')

subirFoto(3,1,'test/data/train/jerry_seinfeld/')
subirFoto(3,2,'test/data/train/jerry_seinfeld/')
subirFoto(3,3,'test/data/train/jerry_seinfeld/')
subirFoto(3,4,'test/data/train/jerry_seinfeld/')
subirFoto(3,5,'test/data/train/jerry_seinfeld/')

subirFoto(4,1,'test/data/train/madonna/')
subirFoto(4,2,'test/data/train/madonna/')
subirFoto(4,3,'test/data/train/madonna/')
subirFoto(4,4,'test/data/train/madonna/')
subirFoto(4,5,'test/data/train/madonna/')

subirFoto(5,1,'test/data/train/mindy_kaling/')
subirFoto(5,2,'test/data/train/mindy_kaling/')
subirFoto(5,3,'test/data/train/mindy_kaling/')
subirFoto(5,4,'test/data/train/mindy_kaling/')
subirFoto(5,5,'test/data/train/mindy_kaling/')


#AHORA COMPROBAREMOS LAS FOTO CON LA VALIDACION
print('=== TIENEN QUE DEVOLVER ID 1:ben_afflek===')
print(reconocerFoto('test/data/val/ben_afflek/1.jpg').json())
print(reconocerFoto('test/data/val/ben_afflek/2.jpg').json())
print(reconocerFoto('test/data/val/ben_afflek/3.jpg').json())
print(reconocerFoto('test/data/val/ben_afflek/4.jpg').json())
print(reconocerFoto('test/data/val/ben_afflek/5.jpg').json())

print('=== TIENEN QUE DEVOLVER ID 2:elton_john===')
print(reconocerFoto('test/data/val/elton_john/1.jpg').json())
print(reconocerFoto('test/data/val/elton_john/2.jpg').json())
print(reconocerFoto('test/data/val/elton_john/3.jpg').json())
print(reconocerFoto('test/data/val/elton_john/4.jpg').json())
print(reconocerFoto('test/data/val/elton_john/5.jpg').json())

print('=== TIENEN QUE DEVOLVER ID 3:jerry_seinfeld===')
print(reconocerFoto('test/data/val/jerry_seinfeld/1.jpg').json())
print(reconocerFoto('test/data/val/jerry_seinfeld/2.jpg').json())
print(reconocerFoto('test/data/val/jerry_seinfeld/3.jpg').json())
print(reconocerFoto('test/data/val/jerry_seinfeld/4.jpg').json())
print(reconocerFoto('test/data/val/jerry_seinfeld/5.jpg').json())

print('=== TIENEN QUE DEVOLVER ID 4:madonna===')
print(reconocerFoto('test/data/val/madonna/1.jpg').json())
print(reconocerFoto('test/data/val/madonna/2.jpg').json())
print(reconocerFoto('test/data/val/madonna/3.jpg').json())
print(reconocerFoto('test/data/val/madonna/4.jpg').json())
print(reconocerFoto('test/data/val/madonna/5.jpg').json())

print('=== TIENEN QUE DEVOLVER ID 5:mindy_kaling===')
print(reconocerFoto('test/data/val/mindy_kaling/1.jpg').json())
print(reconocerFoto('test/data/val/mindy_kaling/2.jpg').json())
print(reconocerFoto('test/data/val/mindy_kaling/3.jpg').json())
print(reconocerFoto('test/data/val/mindy_kaling/4.jpg').json())
print(reconocerFoto('test/data/val/mindy_kaling/5.jpg').json())
