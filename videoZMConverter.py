import cv2
import os
import glob

#Modificar el path por la carpeta donde se encuentren las imagenes del evento
path_carpeta = "path"
path_video = "video.mp4"
fps = 30

def generarVideo(fotos, video, fps):
    originales = sorted(glob.glob(os.path.join(fotos, "*.jpg")))
    if not originales:
        return
    
    #config para el video
    frameEjemplo = cv2.imread(originales[0])
    altura, ancho, _ = frameEjemplo.shape
    codecVideo = cv2.VideoWriter_fourcc(*'mp4v')


    crear = cv2.VideoWriter(video, codecVideo, fps, (ancho, altura))
    print("Creando video..")

    for imagen in originales:
        frame = cv2.imread(imagen)
        if frame is None:
            print(f"Error al leer la imagen {imagen}")
            continue
        crear.write(frame)

    crear.release()
    print(f"Video creado: {path_video}")

if __name__ == "__main__":
    if not os.path.exists(path_carpeta):
        print(f"La carpeta {path_carpeta} no existe. Modifique el path..")
    else:
        generarVideo(path_carpeta, path_video, fps)