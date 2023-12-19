from scanner.Scanner import scanner
from collections import deque
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
            print("Erro sintático na linha " + str(var.line) + " e coluna " + str(var.column), "Posição invalida para:", token.getLexema())
            token = scanner(lines, symbolTable)
            continue

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
        else:
            # erro 
            print("Erro sintático na linha " + str(var.line) + " e coluna " + str(var.column))