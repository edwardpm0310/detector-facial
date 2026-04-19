import cv2
import os
import numpy as np

datapath = './data'
peoplelist = os.listdir(datapath)
print('Lista de personas: ', peoplelist)

#variables iniciales
labels = []
facesdata = []
label = 0

print('Leyendo las imagenes...')

for nameDir in peoplelist:
    personPath = datapath + '/' + nameDir

    for filename in os.listdir(personPath):
        print('Rostro: ', nameDir + '/' + filename)
        labels.append(label)
        facesdata.append(cv2.imread(personPath + '/' + filename, 0)) 
    label = label + 1

face_recognizer = cv2.face.LBPHFaceRecognizer_create()

#Entrenando el nodelo
print('Entrenando modelo...')
face_recognizer.train(facesdata, np.array(labels))
face_recognizer.write('modelo.xml')
print('Modelo entrenado')
