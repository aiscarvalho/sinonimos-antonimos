#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup

def get_sinonimos(queryword):

    r = requests.get('http://www.lexico.pt/' + queryword)
    
    soup = BeautifulSoup(r.text, "lxml")

    try:
        listinha = soup.find("p", class_="adicional sinonimos").text.strip()
    except AttributeError:
        # 404 ou não tem sinónimos
        return []

    palavras_str = listinha.split(": ")[-1]
    palavras = palavras_str.split(", ")
    ultimas_palavras = palavras[-1].split(" e ")

    palavras.remove(palavras[-1])
    palavras.append(ultimas_palavras[0])
    palavras.append(ultimas_palavras[1])

    return palavras

def get_antonimos(queryword):

    r = requests.get('http://www.lexico.pt/' + queryword)

    soup = BeautifulSoup(r.text, "lxml")

    try:
        titulo = soup.select("h2#tit-antonimos")[0]
        listinha = titulo.find_next("p").text.strip()
    except AttributeError:
        # 404 ou não tem antonimos
        return []

    palavras_str = listinha.split(": ")[-1]
    palavras = palavras_str.split(", ")
    ultimas_palavras = palavras[-1].split(" e ")

    palavras.remove(palavras[-1])
    palavras.append(ultimas_palavras[0])
    palavras.append(ultimas_palavras[1])

    return palavras

if __name__ == "__main__":
    import sys
    print get_sinonimos(sys.argv[1])
    print get_antonimos(sys.argv[1])
