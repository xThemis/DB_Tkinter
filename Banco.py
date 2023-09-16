# xThemis
import os
import sqlite3
from sqlite3 import Error


def ConexaoBanco():
    caminho = "C:\\Users\\thais\\OneDrive\\Área de Trabalho\\RoadMap (Programação)\\SQLite\\HelloWorld"
    con = None
    try:
        con = sqlite3.connect(caminho)
    except Error as ex:
        print(ex)
    return con


# selecionar
def dql(query):
    Vcon = ConexaoBanco()
    c = Vcon.cursor()
    c.execute(query)
    res = c.fetchall()
    Vcon.close()
    return res


# Inserir e deletar
def dml(query):
    try:
        Vcon = ConexaoBanco()
        c = Vcon.cursor()
        c.execute(query)
        Vcon.commit()
        Vcon.close()
    except Error as ex:
        print(ex)
