import variables as var
from tokenClass import Token
from symbolTable import SymbolTable

def nextChar(file): 
    if(var.getColumn() == len(file[var.getLine()])):
        var.setColumn (0)
        var.setLine(var.getLine() + 1)
    else: 
        var.setColumn(var.getColumn() + 1)

def scanner(file, table):
    letters = list('ABCDEFGHIJKLMNOPKRSTUVWXYZabcdefghijklmnopqrstuvwxyz')
    digits = list('0123456789')
    state = 0
    word = str("")
    i = 1

    while(i == 1): 
        match(state):
            case(0):
                char = file[var.getLine()][var.getColumn()]

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
                    case('$'): 
                        state = 24
                        word += char
                    case(_):
                        print("Erro: Caractere invalido na linha: " + var.getLine() + " , coluna: " + var.getColumn())
                        i = 0
                        break
            case(1):
                nextChar(file)
                char = file[var.getLine()][var.getColumn()]
                if(char in digits):
                    state = 2
                    word += char
                    continue
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
                    nextChar(file)
                    state = 0
                    return Token("Num", word, "inteiro")
            case(2):
                nextChar(file)
                char = file[var.getLine()][var.getColumn()]
                if(char in digits):
                    state = 2
                    word += char
                elif(char == "."):
                    state = 3
                    word += char
                else:
                    nextChar(file)
                    state = 0
                    return Token("Num", word, "inteiro")
            case(3):
                nextChar(file)
                char = file[var.getLine()][var.getColumn()]
                if(char in digits):
                    state = 25
                    word += char
                else:
                    print('Erro: Esperado caráctere: ". Linha: ' + var.getLine() + ' Coluna: ' + var.getColumn())
            case(4):
                nextChar(file)
                char = file[var.getLine()][var.getColumn()]
                match(char):
                    case('"'):
                        state = 5
                        word += char
                    case('$'):
                        print('Erro: Esperado caráctere: ". Linha: ' + var.getLine() + ' Coluna: ' + var.getColumn())
                    case(_):
                        state = 4
                        word += char
            case(5):
                nextChar(file)
                token = table.get(word)
                if(token == None):
                    token = Token("Lit", word, "literal")
                    token = table.insert(word, token)
                    return token
                else:
                    return token
            case(6):
                nextChar(file)
                char = file[var.getLine()][var.getColumn()]
                if(char in letters):
                    state = 6 
                    word += char
                    continue
                elif(char in digits):
                    state = 6 
                    word += char
                    continue
                elif (char == '_'):
                    state = 6 
                    word += char
                    continue
                else:
                    token = table.get(word)
                    if(token == None):
                        token = Token("id", word, None)
                        token = table.insert(word, token)
                        return token
                    else:
                        return token
            case(7):
                nextChar(file)
                char = file[var.getLine()][var.getColumn()]
                match(char):
                    case('}'):
                        state = 8  
                        word += char    
                    case('$'):
                        print('Erro: Esperado caráctere: ". Linha: ' + var.getLine() + ' Coluna: ' + var.getColumn())
                    case(_):
                        state = 7
                        word += char
            case(8):
                state = 0
                word = str("")
                nextChar(file)
                continue   
            case(9):
                nextChar(file)
                char = file[var.getLine()][var.getColumn()]
                if(char == "="):
                    state = 10
                    word += char
                elif(char == "-"):
                    state = 11
                    word += char
                elif(char == ">"):
                    state = 12
                    word += char
                else:
                    nextChar(file)
                    state = 0
                    return Token("OPR", word, None)
            case(10):
                nextChar(file)
                state = 0
                return Token("OPR", word, None)
            case(11):
                nextChar(file)
                state = 0
                return Token("RCB", word, None)
            case(12):
                nextChar(file)
                state = 0
                return Token("OPR", word, None)
            case(13):
                nextChar(file)
                char = file[var.getLine()][var.getColumn()]
                if(char == "="):
                    state = 14
                    word += char
                else:
                    nextChar(file)
                    state = 0
                    return Token("OPR", word, None)
            case(14):
                nextChar(file)
                state = 0
                return Token("OPR", word, None)
            case(15):
                nextChar(file)
                state = 0
                return Token("OPR", word, None)
            case(16):
                nextChar(file)
                state = 0
                return Token("OPM", word, None)
            case(17):
                nextChar(file)
                state = 0
                return Token("FC_P", word, None)
            case(18):
                nextChar(file)
                state = 0
                return Token("AB_P", word, None)
            case(19):
                nextChar(file)
                state = 0
                return Token("PT_V", word, None)
            case(20):
                nextChar(file)
                state = 0
                return Token("VIR", word, None)
            case(21):
                state = 0
                word = str("")
                nextChar(file)
                continue   
            case(22):
                state = 0
                word = str("")
                nextChar(file)
                continue   
            case(23):
                state = 0
                word = str("")
                nextChar(file)
                continue   
            case(24):
               #EOF
            case(25):
                nextChar(file)
                char = file[var.getLine()][var.getColumn()]
                if(char in digits):
                    state = 25
                    word += char
                elif(char == "E"):
                    state = 26
                    word += char
                elif(char == "e"):
                    state = 26
                    word += char
                else
                    nextChar(file)
                    state = 0
                    return Token("Num", word, "real")
            case(26):
                nextChar(file)
                char = file[var.getLine()][var.getColumn()]
                if(char in digits):
                    state = 28
                    word += char
                elif (char == "+" or char == "-"):
                    state = 27
                    word += char
                else:
                    print('Erro: Esperado caráctere: ". Linha: ' + var.getLine() + ' Coluna: ' + var.getColumn())
            case(27):
                nextChar(file)
                char = file[var.getLine()][var.getColumn()]
                if(char in digits):
                    state = 28
                    word += char
                else:
                    print('Erro: Esperado caráctere: ". Linha: ' + var.getLine() + ' Coluna: ' + var.getColumn())
            case(28):
                nextChar(file)
                state = 0
                return Token("Num", word, "real")
            case _:
                return [word, state]