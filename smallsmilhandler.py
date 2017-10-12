#!/usr/bin/python3
# -*- coding: utf-8 -*-

from xml.sax.handler import ContentHandler


rootlayout = ["width", "height", "background-color"]
region = ["id", "top", "bottom", "left", "right"]
img = ["src", "region", "begin", "dur"]
audio = ["src", "begin", "dur"]
textstream = ["src", "region"]
encontradas = []

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

        self.arg = arg
    def get_tags(self):
        pass

    def startElement(self,name, attrs):

        for clave in etiquetas
            for atributo in clave.atributos

                if name == atributo
                    self.calificacion = attrs.get('calificacion', "")
                    print (self.calificacion)


if __name__ == "__main__":
    """
    Programa principal
    """
    print (etiquetas)
