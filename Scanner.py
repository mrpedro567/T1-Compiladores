import variables as var
from tokenClass import Token

def nextChar(file): 
    if(var.getColumn() == len(file[var.getLine()])):
        var.setColumn (0)
        var.setLine(var.getLine() + 1)
    else: 
        var.setColumn(var.getColumn() + 1)

def scanner(file):
    letters = list('ABCDEFGHIJKLMNOPKRSTUVWXYZabcdefghijklmnopqrstuvwxyz')
    digits = list('0123456789')
    state = 0
    word = []
    i = 1

    while(i == 1): 
        match(state):
            case(0):
                char = file[var.getLine()][var.getColumn()]

                if(char in letters):
                    state = 6 
                    word.append(char)
                    continue

                if(char in digits):
                    state = 1
                    word.append(char)
                    continue

                match(char):
                    case('"'):
                        state = 4  
                        word.append(char)
                    case('{'):
                        state = 7
                        word.append(char)
                    case('<'): 
                        state = 9
                        word.append(char)
                    case('>'):
                        state = 13
                        word.append(char)
                    case('='):
                        state = 15
                        word.append(char)
                    case('+'):
                        state = 16
                        word.append(char)
                    case('-'):
                        state = 16
                        word.append(char)
                    case('*'):
                        state = 16
                        word.append(char)
                    case('/'):
                        state = 16
                        word.append(char)
                    case('('):
                        state = 18
                        word.append(char)
                    case(')'):
                        state = 17
                        word.append(char)
                    case(';'):
                        state = 19
                        word.append(char)
                    case(','):
                        state = 20
                        word.append(char)
                    case(' '):
                        state = 21
                        word.append(char)
                    case('\t'):
                        state = 22
                        word.append(char)
                    case('\n'):
                        state = 23
                        word.append(char)
                    case('$'): 
                        state = 24
                        word.append(char)
                    case(_):
                        print("Erro: Caractere invalido na linha: " + var.getLine() + " , coluna: " + var.getColumn())
                        i = 0
                        break;
            case(1):
                return [word, state]
            case(2):
                return [word, state]
            case(3):
                return [word, state]
            case(4):
                nextChar(file)
                char = file[var.getLine()][var.getColumn()]

                match(char):
                    case('"'):
                        state = 5
                        word.append(char)
                    case('$'):
                        print('Erro: Esperado caráctere: ". Linha: ' + var.getLine() + ' Coluna: ' + var.getColumn())
                    case(_):
                        state = 4
                        word.append(char)
            case(5):
                return [word, state]
            case(6):
                return [word, state]
            case(7):
                return [word, state]
            case(8):
                return [word, state]
            case(9):
                return [word, state]
            case(10):
                return [word, state]
            case(11):
                return [word, state]
            case(12):
                return [word, state]
            case(13):
                return [word, state]
            case(14):
                return [word, state]
            case(15):
                return [word, state]
            case(16):
                nextChar(file)
                state = 0
                return Token("OPM", word, None)
            case(17):
                return [word, state]
            case(18):
                return [word, state]
            case(19):
                return [word, state]
            case(20):
                return [word, state]
            case(21):
                return [word, state]
            case(22):
                return [word, state]
            case(23):
                return [word, state]
            case(24):
                return [word, state]
            case(25):
                return [word, state]
            case(26):
                return [word, state]
            case _:
                return [word, state]