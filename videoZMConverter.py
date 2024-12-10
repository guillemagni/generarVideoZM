import cv2
import os
import glob
from tqdm import tqdm

def generarVideo(fotos, video, fps):
    #Revisar el parametro para la terminación del archivo dependiendo que tipo de imagen se quiera utilziar
    originales = sorted(glob.glob(os.path.join(fotos, "*.jpg")))
    if not originales:
        print("ERROR! -> La carpeta está vacía.")
        return
    
    #config para el video
    frameEjemplo = cv2.imread(originales[0])
    altura, ancho, _ = frameEjemplo.shape
    codecVideo = cv2.VideoWriter_fourcc(*'mp4v')
    crearVideo = cv2.VideoWriter(video, codecVideo, fps, (ancho, altura)) #Objeto para crear el video
    print("Creando video..")

    for imagen in tqdm(originales, desc="Procesando", unit="frame"):
        frame = cv2.imread(imagen)
        if frame is None:
            print(f"ERROR! -> Error al leer la imagen {imagen}")
            continue
        crearVideo.write(frame)

    crearVideo.release()
    print(f"Video creado: {path_video}")

if __name__ == "__main__":
    print()
    print("### Generador de video Zone Minder ###")
    nombre = input("Ingrese el nombre que desee para el video: ")
    path_carpeta = input("Ingrese el path de la carpeta donde se encuentran las imágenes: ")
    path_video =  nombre + ".mp4"
    fps = 30

    if not os.path.exists(path_carpeta):
        print(f"ERROR! -> La carpeta {path_carpeta} no existe. Modifique el path..")
    else:
        generarVideo(path_carpeta, path_video, fps)