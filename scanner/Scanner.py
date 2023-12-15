import variables as var
from tokenClass import Token
from symbolTable import SymbolTable

def nextChar(file): 
    if(var.column >= len(file[var.line]) - 1):
        var.column = 0
        var.line += 1
    else: 
        var.column += 1

def isEOF(file):
    if(var.line >= (len(file) ) ):
        return True
    else:
        return False

def scanner(file, table) -> Token:
    letters = list('ABCDEFGHIJKLMNOPKRSTUVWXYZabcdefghijklmnopqrstuvwxyz')
    digits = list('0123456789')
    state = 0
    word = str("")
    i = 1

    while(i == 1): 
        match(state):
            case(0):
                if(isEOF(file)): 
                    state = 24
                    continue

                char = file[var.line][var.column]

                if(char in letters):
                    state = 6 
                    word += char
                    continue

                if(char in digits):
                    state = 1
                    word += char
                    continue


                match(char):
                    case('"'):
                        state = 4  
                        word += char
                    case('{'):
                        state = 7
                        word += char
                    case('<'): 
                        state = 9
                        word += char
                    case('>'):
                        state = 13
                        word += char
                    case('='):
                        state = 15
                        word += char
                    case('+'):
                        state = 16
                        word += char
                    case('-'):
                        state = 16
                        word += char
                    case('*'):
                        state = 16
                        word += char
                    case('/'):
                        state = 16
                        word += char
                    case('('):
                        state = 18
                        word += char
                    case(')'):
                        state = 17
                        word += char
                    case(';'):
                        state = 19
                        word += char
                    case(','):
                        state = 20
                        word += char
                    case(' '):
                        state = 21
                        word += char
                    case('\t'):
                        state = 22
                        word += char
                    case('\n'):
                        state = 23
                        word += char
                    case(_):
                        print("Erro: Caractere invalido na linha: " + str(var.line) + " , coluna: " + str(var.column))
                        nextChar(file)
                        return Token("ERRO", None, None)
            case(1):
                nextChar(file)
                if(isEOF(file)):
                    return Token("Num", word, "inteiro")
                
                char = file[var.line][var.column]
                if(char in digits):
                    state = 2
                    word += char
                    
                elif(char == "E"):
                        state = 26
                        word += char
                elif(char == "e"):
                        state = 26
                        word += char
                elif(char == "."):
                        state = 3
                        word += char
                else:
                    return Token("Num", word, "inteiro")
            case(2):
                nextChar(file)

                if(isEOF(file)):
                    return Token("Num", word, "inteiro")
                
                char = file[var.line][var.column]
                if(char in digits):
                    state = 2
                    word += char
                elif(char == "."):
                    state = 3
                    word += char
                else:
                    return Token("Num", word, "inteiro")
            case(3):
                nextChar(file)
                if(isEOF(file)):
                    print('Erro: Número esperado na Linha: ' + str(var.line) + ' Coluna: ' + str(var.column))
                    nextChar(file)
                    return Token("ERRO", None, None)

                char = file[var.line][var.column]
                if(char in digits):
                    state = 25
                    word += char
                else:
                    print('Erro: Número esperado na Linha: ' + str(var.line) + ' Coluna: ' + str(var.column))
                    nextChar(file)
                    return Token("ERRO", None, None)
            case(4):
                nextChar(file)
               
                if(isEOF(file)):
                    print('Erro: Esperado caráctere: ". Linha: ' + str(var.line) + ' Coluna: ' + str(var.column))
                    nextChar(file)
                    return Token("ERRO", None, None)

                char = file[var.line][var.column]

                match(char):
                    case('"'):
                        state = 5
                        word += char                        
                    case(_):
                        state = 4
                        word += char
            case(5):
                nextChar(file)
                return Token("Lit", word, "literal")
                
            case(6):
                nextChar(file)
                
                if(isEOF(file)):
                    token = table.get(word)
                    if(token == None):
                        token = Token("id", word, None)
                        table.insert(word, token)
                        return token
                    else:
                        return token

                char = file[var.line][var.column]
                
                if(char in letters):
                    state = 6 
                    word += char
                    
                elif(char in digits):
                    state = 6 
                    word += char
                    
                elif (char == '_'):
                    state = 6 
                    word += char
                    
                else:
                    token = table.get(word)
                    if(token == None):
                        token = Token("id", word, None)
                        table.insert(word, token)
                        return token
                    else:
                        return token
            case(7):
                nextChar(file)
                
                if(isEOF(file)):
                    print('Erro: Esperado caráctere: } Linha: ' + str(var.line) + ' Coluna: ' + str(var.column))
                    nextChar(file)
                    return Token("ERRO", None, None)
                
                char = file[var.line][var.column]
                
                match(char):
                    case('}'):
                        state = 8  
                        word += char    
                    case(_):
                        state = 7
                        word += char
            case(8):
                state = 0
                word = str("")
                nextChar(file)
                   
            
            case(9):
                nextChar(file)

                if(isEOF(file)):
                    return Token("OPR", word, None)

                char = file[var.line][var.column]
                match(char):
                    case("="):
                        state = 10
                        word += char
                    case("-"):
                        state = 11
                        word += char
                    case(">"):
                        state = 12
                        word += char
                    case(_):
                        return Token("OPR", word, None)
            case(10):
                nextChar(file)
                return Token("OPR", word, None)
            case(11):
                nextChar(file)
                return Token("RCB", word, None)
            case(12):
                nextChar(file)
                return Token("OPR", word, None)
            case(13):
                nextChar(file)

                if(isEOF(file)):
                    return Token("OPR", word, None)

                char = file[var.line][var.column]
                
                if(char == "="):
                    state = 14
                    word += char
                else:
                    nextChar(file)
                    return Token("OPR", word, None)
            case(14):
                nextChar(file)
                return Token("OPR", word, None)
            case(15):
                nextChar(file)
                return Token("OPR", word, None)
            case(16):
                nextChar(file)
                return Token("OPM", word, None)
            case(17):
                nextChar(file)
                return Token("FC_P", word, None)
            case(18):
                nextChar(file)
                return Token("AB_P", word, None)
            case(19):
                nextChar(file)
                return Token("PT_V", word, None)
            case(20):
                nextChar(file)
                return Token("VIR", word, None)
            case(21):
                nextChar(file)
                state = 0
                word = str("")
                   
            case(22):
                nextChar(file)
                state = 0
                word = str("")
                   
            case(23):
                state = 0
                word = str("")
                nextChar(file)
                   
            case(24):
               return Token("EOF", "EOF", None)
            case(25):
                nextChar(file)

                if(isEOF(file)):
                    return Token("Num", word, "real")

                char = file[var.line][var.column]
                
                if(char in digits):
                    state = 25
                    word += char
                elif(char == "E"):
                    state = 26
                    word += char
                elif(char == "e"):
                    state = 26
                    word += char
                else:
                    state = 0
                    return Token("Num", word, "real")
            case(26):
                nextChar(file)

                if(isEOF(file)):
                    print('Erro: Esperado caráctere: numero | + | -". Linha: ' + str(var.line) + ' Coluna: ' + str(var.column))
                    return Token("ERRO", None, None)

                char = file[var.line][var.column]
                if(char in digits):
                    state = 28
                    word += char
                elif (char == "+" or char == "-"):
                    state = 27
                    word += char
                else:
                    print('Erro: Esperado caráctere: numero | + | -". Linha: ' + str(var.line) + ' Coluna: ' + str(var.column))
                    nextChar(file)
                    return Token("ERRO", None, None)
            case(27):
                nextChar(file)

                if(isEOF(file)):
                    print('Erro: Esperado caráctere: numero. Linha: ' + str(var.line) + ' Coluna: ' + str(var.column))
                    return Token("ERRO", None, None)

                char = file[var.line][var.column]
                if(char in digits):
                    state = 28
                    word += char
                else:
                    print('Erro: Esperado caráctere: numero. Linha: ' + str(var.line) + ' Coluna: ' + str(var.column))
                    nextChar(file)
                    return Token("ERRO", None, None)
            case(28):
                nextChar(file)

                if(isEOF(file)):
                    return Token("Num", word, "real")

                char = file[var.line][var.column]

                if(char in digits):
                    state = 28
                    word += char
                else:
                    state = 0
                    return Token("Num", word, "real")
            case _:
                print("Erro: caractere invalido. Linha: " + str(var.line) + " Coluna: " + str(var.column))
                return Token("ERRO", None, None)