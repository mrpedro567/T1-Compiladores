from scanner.Scanner import scanner
from collections import deque
from scanner.tokenClass import Token
import scanner.variables as var
import parser.productions as prod
import pandas as pd
import backend.codeGenerator as codeGen



def parse(lines, symbolTable): 
    stack = deque()
    var.semanticStack = deque()
    stack.append(0)
    
    actionTable = pd.read_csv('parser/table/action.csv', index_col=0)
    gotoTable = pd.read_csv('parser/table/goto.csv', index_col=0)
    token = scanner(lines, symbolTable)
    codeGen.init()

    while(True): 
        if(token.getClasse() == "ERRO"):
            var.error = True
            token = scanner(lines, symbolTable)
            continue;
        
        state = stack[-1]
        action = actionTable.iloc[state][token.getClasse()]
        
        if(isinstance(action, str) == False):
            var.error = True

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
            validateSemanticS(action[1:], symbolTable, token)
            token = scanner(lines, symbolTable)
        elif action[0] == 'r':
            production = prod.productions[int(action[1:])]
            
            for i in range(production[1]):
                stack.pop()
            
            state = stack[-1]

            goto = int(gotoTable.loc[state][production[0].split(' ')[0]])
            stack.append(goto)
    
            print(production[0])
            validateSemanticR(production[2], symbolTable, token)
        elif action == 'acc':
            codeGen.write_to_file()
            break

def validateSemanticR(rule, symbolTable, token):
    
    match(rule):
        case 5:
            codeGen.r5()
            return
        case 6: 
            codeGen.r6()
            return
        
        case 7: 
            # idToken = var.semanticStack.pop()
            # codeGen.r7(idToken)
            return
        case 8:   
            idToken = var.semanticStack.pop()
            codeGen.r8(idToken)      
            var.semanticStack.append(idToken)
            return
        case 9:
            tipo = var.semanticStack.pop()
            codeGen.rTipo(tipo["tipo"])
            var.semanticStack.append(tipo)
            return
        case 10:
            tipo = var.semanticStack.pop()
            codeGen.rTipo(tipo["tipo"])
            var.semanticStack.append(tipo)
            return
        case 11:
            tipo = var.semanticStack.pop()
            codeGen.rTipo(tipo["tipo"])
            var.semanticStack.append(tipo)
            return
        case 13: 
            idToken = var.semanticStack.pop()
            codeGen.r13(idToken)
        case 14: 
            idToken = var.semanticStack.pop()
            codeGen.r14(idToken)
        case 15: 
            return
        case 16: 
            return
        case 17: 
            return
        case 19: 
            ld1 = var.semanticStack.pop()
            ld2 = var.semanticStack.pop()
            if(ld1["tipo"] != ld2["tipo"]):
                print("Erro semântico na linha " + str(var.line + 1) + " e coluna " + str(var.column + 1), "Tipos incompatíveis: ", ld1["tipo"], " e ", ld2["tipo"])
                var.error = True
                return

            codeGen.r19(ld2, ld1)
        case 20: 
            l1 = var.semanticStack.pop()
            opm = var.semanticStack.pop()
            l2 = var.semanticStack.pop()
            if(l1["tipo"] != l2["tipo"]):
                print("Erro semântico na linha " + str(var.line + 1) + " e coluna " + str(var.column + 1), "Tipos incompatíveis: ", l1["tipo"], " e ", l2["tipo"])
                var.error = True
                return
            
            tx = {}
            tx["tipo"] = l1["tipo"]
            tx["lexema"] = "T" + str(var.tmpCounter)
            var.tmpCounter += 1
            codeGen.r20(tx, l1, l2, opm)

            var.semanticStack.append(tx)
        case 25: 
            codeGen.r25()
        case 26: 
            codeGen.r26()
        case 27: 
            l1 = var.semanticStack.pop()
            oprd = var.semanticStack.pop()
            l2 = var.semanticStack.pop()

            if(l1["tipo"] != l2["tipo"]):
                print("Erro semântico na linha " + str(var.line + 1) + " e coluna " + str(var.column + 1), "Tipos incompatíveis: ", l1["tipo"], " e ", l2["tipo"])
                var.error = True
                return
            
            tx = {}
            tx["tipo"] = l1["tipo"]
            tx["lexema"] = "T" + str(var.tmpCounter)
            var.tmpCounter += 1
            codeGen.r27(l2, oprd, l1, tx)
        case _: 
            return

def validateSemanticS(rule, symbolTable, token): 
    match(rule):
        case "50": 
            tipo = var.semanticStack.pop()

            idToken = symbolTable.get(token.getLexema())
            idToken.setTipo(tipo["tipo"])

            symbolTable.insert(idToken.getLexema(), idToken)

            L = {}
            L["tipo"] = token.getTipo()
            L["lexema"] = token.getLexema()
            L["classe"] = token.getClasse()

            var.semanticStack.append(L)
    
            if(tipo["classe"] == "id"):
                # var.semanticStack.append(tipo)
                codeGen.r7(tipo)
            
            return
        case "22":
            L = {}
            L["tipo"] = token.getTipo()
            L["lexema"] = token.getLexema()
            L["classe"] = token.getClasse()
            var.semanticStack.append(L)
        case "23": 
            L = {}
            L["tipo"] = token.getTipo()
            L["lexema"] = token.getLexema()
            L["classe"] = token.getClasse()
            var.semanticStack.append(L)
        case "24": 
            L = {}
            L["tipo"] = token.getTipo()
            L["lexema"] = token.getLexema()
            L["classe"] = token.getClasse()
            var.semanticStack.append(L)
        case "11": 
            L = {}
            L["tipo"] = token.getTipo()
            L["lexema"] = token.getLexema()
            L["classe"] = token.getClasse()
            var.semanticStack.append(L)
        case "29": 
            if(token.getTipo() == None): 
                print("Erro semântico na linha " + str(var.line + 1) + " e coluna " + str(var.column + 1), "Variável não declarada: ", token.getLexema())
                var.error = True
                return
            else:
                L = {}
                L["tipo"] = token.getTipo()
                L["lexema"] = token.getLexema()
                L["classe"] = token.getClasse()
                var.semanticStack.append(L)
        case "33": 
            if(token.getTipo() == None):
                print("Erro semântico na linha " + str(var.line + 1) + " e coluna " + str(var.column + 1), "Variável não declarada: ", token.getLexema())
                var.error = True
                return
            
            L = {}
            L["tipo"] = token.getTipo()
            L["lexema"] = token.getLexema()
            L["classe"] = token.getClasse()
            var.semanticStack.append(L)
        case "32":
            if(token.getTipo() == None):
                print("Erro semântico na linha " + str(var.line + 1) + " e coluna " + str(var.column + 1), "Variável não declarada: ", token.getLexema())
                var.error = True
                return
            
            L = {}
            L["tipo"] = token.getTipo()
            L["lexema"] = token.getLexema()
            L["classe"] = token.getClasse()
            var.semanticStack.append(L)
        case "31":
            if(token.getTipo() == None):
                print("Erro semântico na linha " + str(var.line + 1) + " e coluna " + str(var.column + 1), "Variável não declarada: ", token.getLexema())
                var.error = True
                return
            
            L = {}
            L["tipo"] = token.getTipo()
            L["lexema"] = token.getLexema()
            L["classe"] = token.getClasse()
            var.semanticStack.append(L)
        case "13":
            if(token.getTipo() == None):
                print("Erro semântico na linha " + str(var.line + 1) + " e coluna " + str(var.column + 1), "Variável não declarada: ", token.getLexema())
                var.error = True
                return
            
            L = {}
            L["tipo"] = token.getTipo()
            L["lexema"] = token.getLexema()
            L["classe"] = token.getClasse()
            var.semanticStack.append(L)
        case "55":
            L = {}
            L["tipo"] = token.getTipo()
            L["lexema"] = token.getLexema()
            L["classe"] = token.getClasse()
            var.semanticStack.append(L)
        case "56":
            L = {}
            L["tipo"] = token.getTipo()
            L["lexema"] = token.getLexema()
            L["classe"] = token.getClasse()
            var.semanticStack.append(L)
        case "72": 
            L = {}
            L["tipo"] = token.getTipo()
            L["lexema"] = token.getLexema()
            L["classe"] = token.getClasse()
            var.semanticStack.append(L)
        case "67": 
            L = {}
            L["tipo"] = token.getTipo()
            L["lexema"] = token.getLexema()
            L["classe"] = token.getClasse()
            var.semanticStack.append(L)
        case _: 
            return