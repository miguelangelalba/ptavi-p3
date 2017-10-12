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

        print (encontradas)

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

        encontradas.append = etiqueta_para_lista


if __name__ == "__main__":
    """
    Programa principal
    """

    print ("Etiquetas:" + etiquetas)
    parser = make_parser()
    cHandler = ChistesHandler()
    parser.setContentHandler(cHandler)
    parser.parse(open('karaoke.smil'))
