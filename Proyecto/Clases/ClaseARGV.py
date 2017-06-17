import sys
import re
import urllib2 as sensor
import os
from os.path import basename
 
extensions = ['.png','.jpg','.bmp','.jpeg']
 
def descargarImagenes(url):

        fichero = raw_input("Nombre de carpeta en la cual se descargaran las imagenes: ")
        #ubicacion del directorio actual
        directorioActual = os.getcwd()
        directorio = os.path.join(fichero)
        #valida el directorio si ya existe, si no, lo crea
        if os.path.isdir(directorio):
                os.chdir(directorio)
        else:
         os.mkdir(directorio)
         os.chdir(directorio)

         #validacion de url
        if not url.lower().startswith('http://') and not url.lower().startswith('https://'):
                url = 'http://%s'%url
        print 'Descargando de: %s...'%url

        Content = sensor.urlopen(url).read()

        # Busqueda del tag img en la pagina web.
        imgUrls = re.findall('img .*?src="(.*?)"', Content)

        #descargar las imagenes
        for imgUrl in imgUrls:
 
                print imgUrl
                os.system('wget -q -nc ' + imgUrl)

         #muestra direccion actual de la descarga
        print "Direccion de las imagenes descargadas: " + os.getcwd()
        os.chdir(directorioActual)

 #uso de parametro argv 
if __name__ == '__main__':
        args = sys.argv
        if len(args) < 2:
                print 'Introducir url: '
                exit(-1)
        print args[1]
        descargarImagenes(args[1])
        exit(0)
