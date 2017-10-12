#!/usr/bin/python3
# -*- coding: utf-8 -*-
from xml.sax import make_parser
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

    def __init__(self):
        self.encontradas = [""]

    def get_tags(self):
        print("Lista de etiquetas y atributos encontrados:")
        print (self.encontradas)

    def startElement(self,name, attrs):
        if name not in etiquetas.keys():
            return

        etiqueta_para_lista = {
            "etiqueta": name,
            "atributos": {}
        }

        for atributo in etiquetas[name]:
            #etiqueta_para_lista["caca"] = 4
            etiqueta_para_lista["atributos"][atributo] = attrs.get(atributo,"")

        self.encontradas.append(etiqueta_para_lista)


if __name__ == "__main__":
    """
    Programa principal
    """
    print (etiquetas)
    parser = make_parser()
    cHandler = SmallSMILHandler()
    parser.setContentHandler(cHandler)
    parser.parse(open('karaoke.smil'))
    cHandler.get_tags()
