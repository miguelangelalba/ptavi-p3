#!/usr/bin/python3
# -*- coding: utf-8 -*-

from xml.sax.handler import ContentHandler


rootlayout = ["width", "height", "background-color"]
region = ["id", "top", "bottom", "left", "right"]
img = ["src", "region", "begin", "dur"]
audio = ["src", "begin", "dur"]
textstream = ["src", "region"]


etiquetas = {
    "root-layout": rootlayout,
    "region": region,
    "img": img,
    "audio": audio,
    "textstream": textstream
}

class SmallSMILHandler(ContentHandler):
    """docstring for SmallSMILHandler."""

    def __init__(self, arg):
        self.encontradas = []
        self.arg = arg
    def get_tags(self):
        pass

    def startElement(self,name, attrs):
        if name not in etiquetas.keys():
            return

        etiqueta_para_lista = {
            "etiqueta": name,
            "atributos": {}
        }

        for atributo in etiquetas[name]:

            if attrs == atributo:



        for clave in etiquetas:
            for atributo in clave.atributos:

                if name == atributo:
                    self.calificacion = attrs.get('calificacion', "")
                    print (self.calificacion)


if __name__ == "__main__":
    """
    Programa principal
    """
    print (etiquetas)
