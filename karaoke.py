#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import json
import urllib
from xml.sax import make_parser
from xml.sax.handler import ContentHandler
from smallsmilhandler import SmallSMILHandler

class KaraokeLocal(SmallSMILHandler):

    def __init__(self,fichero):
        parser = make_parser()
        cHandler = SmallSMILHandler()
        parser.setContentHandler(cHandler)
        parser.parse(open(fichero))
        self.lista = cHandler.get_tags()

    def __str__(self):
        #Creo que no tengo que imprimir y lo que tengo que hacer es guardar todo
        #en un str
        for elemento in self.lista:
            atr_a_imprimir = ""
            for atributo in elemento["atributos"]:
                if elemento["atributos"][atributo] != "":
                    atr_a_imprimir = atr_a_imprimir + "\t" + atributo + "=" + \
                    elemento["atributos"][atributo]
            print(elemento["etiqueta"] + atr_a_imprimir)

    def to_json(self,fichero,namejson):
        if namejson == "":
            namejson = fichero.split(".")[0] + ".json"
        with open(namejson,"w") as fich_json:
            json.dump(self.lista,fich_json, sort_keys=True,
                    indent=4, separators=(' ', ': '))

    def do_local(self):
        for elemento in self.lista:
            if "src" in elemento["atributos"].keys():
                if "http://" in  elemento["atributos"]["src"]:
                    url = elemento["atributos"]["src"]
                    filename = url[url.rfind("/") + 1:]
                    print ("descargando")
                    print(url)
                    urllib.request.urlretrieve(url,filename)




def mostrar_valores(lista):
    for elemento in lista:
        atr_a_imprimir = ""
        for atributo in elemento["atributos"]:
            if elemento["atributos"][atributo] != "":
                atr_a_imprimir = atr_a_imprimir + "\t" + atributo + "=" + \
                elemento["atributos"][atributo]
        #if elemento["atributos"][atributo] != "":
        print(elemento["etiqueta"] + atr_a_imprimir)

def to_json(fichero,lista):
    nombre_fich = fichero.split(".")[0] + ".json"
    with open(nombre_fich,"w") as fich_json:
        json.dump(lista,fich_json, sort_keys=True,
                indent=4, separators=(' ', ': '))

#def cahange_localizacion(fichero):

def dwn_to_local(lista):
    for elemento in lista:
        if "src" in elemento["atributos"].keys():
            if "http://" in  elemento["atributos"]["src"]:
                url = elemento["atributos"]["src"]
                filename = url[url.rfind("/") + 1:]
                print ("descargando")
                print(url)
                urllib.request.urlretrieve(url,filename)

if __name__ == '__main__':


    if len(sys.argv) != 2:
        sys.exit("Usage:python3 karaoke.py file.smil.")
    fichero = sys.argv[1]
    karaoke = KaraokeLocal(fichero)
    #imprimir
    karaoke.to_json(fichero)
    karaoke.do_local()
    karaoke.to_json(fichero,"local.json")
    #mostrar_valores(lista)
    #dwn_to_local(lista)
