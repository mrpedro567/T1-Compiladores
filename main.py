import argparse
import sys
import time
import variables as var
from symbolTable import SymbolTable
from tokenClass import Token
from Scanner import scanner

global line
global column

def main():
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('path', metavar='Path', help='Caminho do arquivo ')
    args = parser.parse_args()
    
    symbolTable = SymbolTable()
    initPalavras(symbolTable)

    var.init()    

    file = open(sys.argv[1], "r")
    lines = file.readlines()

    while(True): 
        token = scanner(lines, symbolTable)

        if(token.classe != "ERRO"): 
            print("Classe: " + str(token.classe) + ", Lexema: " + str(token.lexema) + " , Tipo: " + str(token.tipo))
        if(token.classe == "EOF"): 
            break

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
    symbolTable.insert("literal", Token("literal", "literal", "literal"))

    

if __name__ == "__main__":
    main()