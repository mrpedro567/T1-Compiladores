import variables as var

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
                    nextChar(file)

                if(char in digits):
                    state = 1
                    word.append(char)
                    nextChar(file)

                match(char):
                    case("'"):
                        state = 4  
                        nextChar(file)
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
                return [word, state]
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
                return [word, state]
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
                
    if (char in digits):
        state = 1
        word.append(char)
        c = c +1
        if (file[l][c] in digits):
            state = 2
            word.append(file[l][c])
            c = c + 1
            while (file[l][c] in digits):
                word.append(file[l][c])
                c = c + 1
            if (file[l][c] == '.'):
                word.append(file[l][c])
                c = c + 1
                if (file[l][c] in digits):
                    state = 25
                    word.append(file[l][c])
                    c = c + 1
                    while (file[l][c] in digits):
                        word.append(file[l][c])
                        c = c + 1
                    if(file[l][c] == 'E' or file[l][c] == 'e'):
                        word.append(file[l][c])
                        c = c + 1
                        if (file[l][c] in digits):
                            state = 26  
                            word.append(file[l][c])
                        elif (file[l][c] == '+' or file[l][c] == '-'):
                            word.append(file[l][c])
                            c = c + 1
                            if (file[l][c] in digits):
                                state = 26
                                word.append(file[l][c])
        elif (file[l][c] == '.'):
            word.append(file[l][c])
            c = c + 1
            if (file[l][c] in digits):
                state = 25
                word.append(file[l][c])
                c = c + 1
                while (file[l][c] in digits):
                    word.append(file[l][c])
                    c = c + 1
                if(file[l][c] == 'E' or file[l][c] == 'e'):
                    word.append(file[l][c])
                    c = c + 1
                    if (file[l][c] in digits):
                        state = 26  
                        word.append(file[l][c])
                    elif (file[l][c] == '+' or file[l][c] == '-'):
                        word.append(file[l][c])
                        c = c + 1
                        if (file[l][c] in digits):
                            state = 26
                            word.append(file[l][c])
        elif (file[l][c] == 'E' or file[l][c] == 'e'):
            word.append(file[l][c])
            c = c + 1
            if (file[l][c] in digits):
                state = 26  
                word.append(file[l][c])
            elif (file[l][c] == '+' or file[l][c] == '-'):
                word.append(file[l][c])
                c = c + 1
                if (file[l][c] in digits):
                    state = 26
                    word.append(file[l][c])
    elif (char in letters):
        state = 6 
        word.append(char)
        while (file[l][c] in letters):
            c = c + 1
            word.append(file[l][c])
    elif (char == '+' or char == '-' or char == '*' or char == '/'):
        state = 16
        word.append(file[l][c])
    elif (char == ')'):
        state = 17
        word.append(file[l][c])
    elif (char == '('):
        state = 18
        word.append(file[l][c])
    elif (char == ';'):
        state = 19
        word.append(file[l][c])
    elif (char == ','):
        state = 20
        word.append(file[l][c])
    elif (char == ' '):
        state = 21
        word.append(file[l][c])
    elif (char == '\t'):
        state = 22
        word.append(file[l][c])
    elif (char == '\n'):
        state = 23
        word.append(file[l][c])
    elif (char == ')'):
        state = 17
        word.append(file[l][c])
    elif (char == '='):
        state = 15
        word.append(file[l][c])
    elif (char == '>'):
        state = 13
        word.append(file[l][c])
        c = c + 1
        if (file[l][c] == '='):
            state = 14
            word.append(file[l][c])
    elif (char == '<'):
        state = 9
        word.append(file[l][c])
        c = c + 1
        if (file[l][c] == '='):
            state = 10
            word.append(file[l][c])
        elif (file[l][c] == '>'):
            state = 12
            word.append(file[l][c])
        elif (file[l][c] == '-'):
            state = 11
            word.append(file[l][c])
    elif (char == '{'):
        word.append(file[l][c])
        c = c + 1
        while (file[l][c] != '}'):
            word.append(file[l][c])
            c = c + 1
        if (file[l][c] == '}'):
            state = 8
            word.append(file[l][c])
    elif (char == '"'):
        word.append(file[l][c])
        c = c + 1
        while (file[l][c] != '"'):
            word.append(file[l][c])
            c = c + 1
        if (file[l][c] == '"'):
            state = 5
            word.append(file[l][c])
        
    return [word, state]
                
                
    
    