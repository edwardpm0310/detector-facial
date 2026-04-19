# Sistema de Reconocimiento Facial con OpenCV

Este proyecto es un sistema de reconocimiento facial desarrollado en Python utilizando OpenCV y el algoritmo LBPH (Local Binary Patterns Histograms).

## Funcionalidades

- Registro de nuevas personas: captura 300 imágenes de una persona.
- Entrenamiento del modelo: entrena un reconocedor facial y genera el archivo modelo.xml.
- Reconocimiento en tiempo real: identifica a las personas registradas a través de la cámara y muestra su nombre o "Desconocido".

## Archivos del proyecto

- detector_de_rostro.py → Captura y guarda los rostros para registrar personas.
- entrenamiento.py → Entrena el modelo con las imágenes guardadas.
- clasificador_de_rostro.py → Realiza el reconocimiento facial en vivo.
- camera.py → Detecta automáticamente la cámara disponible.

## Requisitos

- Python 3
- OpenCV (opencv-contrib-python)
- imutils

## Cómo usar

1. Crea la carpeta "data" en la raíz del proyecto.
2. Ejecuta detector_de_rostro.py e ingresa el nombre de la persona (capturará 300 rostros).
3. Ejecuta entrenamiento.py para entrenar el modelo.
4. Ejecuta clasificador_de_rostro.py para probar el reconocimiento en tiempo real.
5. Presiona la tecla "q" para salir.

## Notas

- El modelo entrenado se guarda como modelo.xml
- Las fotos de cada persona se guardan en data/nombre_de_la_persona/
- Funciona mejor con buena iluminación y mirando de frente a la cámara.

Proyecto de reconocimiento facial usando OpenCV LBPH.
