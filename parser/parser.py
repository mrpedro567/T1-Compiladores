from scanner.Scanner import scanner
from collections import deque
from scanner.tokenClass import Token
import scanner.variables as var
import parser.productions as prod
import pandas as pd


def parse(lines, symbolTable): 
    stack = deque()
    stack.append(0)
    
    actionTable = pd.read_csv('parser/table/action.csv', index_col=0)
    gotoTable = pd.read_csv('parser/table/goto.csv', index_col=0)
    token = scanner(lines, symbolTable)


    while(True): 
        state = stack[-1]
        action = actionTable.iloc[state][token.getClasse()]
        
        if(isinstance(action, str) == False):
            

            match(state): 
                case 0: 
                    print("Erro sintático na linha " + str(var.line + 1) + " e coluna " + str(var.column + 1), "Esperado: Inicio", "Recebido: ", token.getLexema())
                    
                    token = Token("inicio", "inicio", "inicio")
                    
                    var.line = var.lastToken[0]
                    var.column = var.lastToken[1]
                    
                    continue
                case 2: 
                    print("Erro sintático na linha " + str(var.line + 1) + " e coluna " + str(var.column + 1), "Esperado: varinicio", "Recebido: ", token.getLexema())
                    
                    token = Token("varinicio", "varinicio", "varinicio")
                    
                    var.line = var.lastToken[0]
                    var.column = var.lastToken[1]
                    
                    continue
                case 11: 
                    print("Erro sintático na linha " + str(var.line + 1) + " e coluna " + str(var.column + 1), "Esperado: id, Recebido: ",  token.getLexema())

                    token = scanner(lines, symbolTable)
                    continue

                case 13: 
                    print("Erro sintático na linha " + str(var.line + 1) + " e coluna " + str(var.column + 1), "Esperado: atribuição", "Recebido: ", token.getLexema())
                    
                    token = Token("rcb", "<-", None)
                    
                    var.line = var.lastToken[0]
                    var.column = var.lastToken[1]
                    
                    continue
                
                case 16: 
                    print("Erro sintático na linha " + str(var.line + 1) + " e coluna " + str(var.column + 1), "Esperado: (", "Recebido: ", token.getLexema())
                    
                    token = Token("ab_p", "(", None)
                    
                    var.line = var.lastToken[0]
                    var.column = var.lastToken[1]
                    
                    continue

                case 17: 
                    print("Erro sintático na linha " + str(var.line + 1) + " e coluna " + str(var.column + 1), "Esperado: (", "Recebido: ", token.getLexema())
                    
                    token = Token("ab_p", "(", None)
                    
                    var.line = var.lastToken[0]
                    var.column = var.lastToken[1]
                    
                    continue

                case 20: 
                    print("Erro sintático na linha " + str(var.line + 1) + " e coluna " + str(var.column + 1), "Esperado: ;", "Recebido: ", token.getLexema())
                    
                    token = Token("pt_v", ";", None)
                    
                    var.line = var.lastToken[0]
                    var.column = var.lastToken[1]
                    
                    continue
                case 29: 
                    print("Erro sintático na linha " + str(var.line + 1) + " e coluna " + str(var.column + 1), "Esperado: ;", "Recebido: ", token.getLexema())
                    
                    token = Token("pt_v", ";", None)
                    
                    var.line = var.lastToken[0]
                    var.column = var.lastToken[1]
                    
                    continue
                case 30: 
                    print("Erro sintático na linha " + str(var.line + 1) + " e coluna " + str(var.column + 1), "Esperado: ;", "Recebido: ", token.getLexema())
                    
                    token = Token("pt_v", ";", None)
                    
                    var.line = var.lastToken[0]
                    var.column = var.lastToken[1]
                    
                    continue
                case _:  
                    print("Erro sintático na linha " + str(var.line) + " e coluna " + str(var.column), "Posição invalida para:", token.getLexema())
                    token = scanner(lines, symbolTable)
                    continue
        else: 
            var.lastToken = [var.line, var.column]

        if action[0] == 's':
            stack.append(int(action[1:]))
            token = scanner(lines, symbolTable)
        elif action[0] == 'r':
            production = prod.productions[int(action[1:])]
            
            for i in range(production[1]):
                stack.pop()
            
            state = stack[-1]

            goto = int(gotoTable.loc[state][production[0].split(' ')[0]])
            stack.append(goto)
    
            print(production[0])
        elif action == 'acc':
            break