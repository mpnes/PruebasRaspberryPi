from picamera import PiCamera
from time import sleep

camera = PiCamera()

camera.rotation = 180 #se puede rotar 90, 180, 270

#muestra lo que ve la camara inicia e preview
camera.start_preview() #transparencia con (alpha = 0/200)
sleep(10)

'''
for i in range(100): #brillo de 0 a 100, std 50, mismo con contraste
    camera.annotate_text = "Brillo%s" %i #esribir en la imagen
    camera.contrast = i
    camera.brightness = i
    sleep(.1)

for i in camera.IMAGE_EFFECTS:
        camera.image_effect = i
        camera.annotate_text = "efecto %s" %i
        sleep(5)
for i in camera.AWB_MODES:
        camera.awb_mode = i
        camera.annotate_text = "efecto %s" %i
        sleep(5)
for i in camera.EXPOSURE_MODES:
        camera.exposure_mode = i
        camera.annotate_text = "efecto %s" %i
        sleep(5)
    
#toma 2 fotos, 1 foto cada 2 segudos
for i in range(2):
    sleep(2)
    camera.capture('/home/pi/Documents/Camerapi/imaRes.jpg')

#toma video de 10 segudos, para reproducirlo usar comando omxplayer
camera.start_recording('/home/pi/Documents/Camerapi/video.h264')
sleep(10)
camera.stop_recording()
'''

#detiene el preview
camera.stop_preview()
