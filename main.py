import argparse
import sys
import time
import scanner.variables as var
import parser.productions as prod
from scanner.symbolTable import SymbolTable
from scanner.tokenClass import Token
from scanner.Scanner import scanner
from parser.parser import parse


global line
global column

def main():
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('path', metavar='Path', help='Caminho do arquivo ')
    args = parser.parse_args()
    
    symbolTable = SymbolTable()
    initPalavras(symbolTable)

    var.init()   
    prod.init()

    file = open(sys.argv[1], "r")
    lines = file.readlines()

    parse(lines, symbolTable)

def initPalavras(symbolTable):
    symbolTable.insert("inicio", Token("inicio", "inicio", "inicio"))
    symbolTable.insert("varinicio", Token("varinicio", "varinicio", "varinicio"))
    symbolTable.insert("varfim", Token("varfim", "varfim", "varfim"))
    symbolTable.insert("escreva", Token("escreva", "escreva", "escreva"))
    symbolTable.insert("leia", Token("leia", "leia", "leia"))
    symbolTable.insert("se", Token("se", "se", "se"))
    symbolTable.insert("entao", Token("entao", "entao", "entao"))
    symbolTable.insert("fimse", Token("fimse", "fimse", "fimse"))
    symbolTable.insert("repita", Token("repita", "repita", "repita"))
    symbolTable.insert("fimrepita", Token("fimrepita", "fimrepita", "fimrepita"))
    symbolTable.insert("fim", Token("fim", "fim", "fim"))
    symbolTable.insert("inteiro", Token("inteiro", "inteiro", "inteiro"))
    symbolTable.insert("literal", Token("literal", "literal", "literal"))
    symbolTable.insert("real", Token("real", "real", "real"))

    

if __name__ == "__main__":
    main()