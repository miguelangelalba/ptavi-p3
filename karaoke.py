#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
from xml.sax import make_parser
from xml.sax.handler import ContentHandler
import smallsmilhandler

def mostrar_valores(lista):
    for elemento in lista:
        for atributo in elemento["atributos"]:
            print(elemento["etiqueta"] + "\t" + atributo + "\t" + elemento["atributos"][atributo])

if __name__ == '__main__':

    parser = make_parser()
    cHandler = smallsmilhandler.SmallSMILHandler()
    parser.setContentHandler(cHandler)
    print(len(sys.argv))
    if len(sys.argv) != 2:
        sys.exit("Usage:python3 karaoke.py file.smil.")

    parser.parse(open(sys.argv[1]))
    lista =cHandler.get_tags()
    mostrar_valores(lista)
