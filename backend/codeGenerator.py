import scanner.variables as var

def init(): 
    with open("PROGRAMA.C", 'a+') as f:
        f.seek(0)  
        var.fileLines = f.readlines()

        if(len(var.fileLines) > 0):
            var.fileLines.clear()
        
        var.fileLines.insert(0, "#include <stdio.h>\n\n")
        var.fileLines.insert(1, "int main() {\n")
        var.fileLines.insert(2, "\t// TMP\n")
        var.fileLines.insert(3, "\n")

def write_to_file():
    if(var.error == False):
        with open("PROGRAMA.C", 'w') as f:
            f.writelines(var.fileLines)
            f.write("\n\t return 0;\n")
            f.write("}")

def r5(): 
    return 
    # if(var.error == False):
    #     index = var.fileLines.index("int main() {\n")
    #     var.lineInserted = index + 1
    #     var.fileLines.insert(index + 1, "\t // #L1")

        

def r6():
    if(var.error == False):
        var.lineInserted = len(var.fileLines) - 1
        var.fileLines[var.lineInserted] = var.fileLines[var.lineInserted] + ";\n"
        return

def r8(id):
    if(var.error == False):
        var.lineInserted = len(var.fileLines) - 1
        if(id["tipo"] == "literal"):
            var.fileLines[var.lineInserted] = var.fileLines[var.lineInserted] + id["lexema"] + " [256] "
        else:
            var.fileLines[var.lineInserted] = var.fileLines[var.lineInserted] + id["lexema"] + " "        
    return

def r7(id):
    if(var.error == False):
        var.lineInserted = len(var.fileLines) - 1
        if(id["tipo"] == "literal"):
            var.fileLines[var.lineInserted] = var.fileLines[var.lineInserted] + id["lexema"] + " [256], "
        else:
            var.fileLines[var.lineInserted] = var.fileLines[var.lineInserted] + id["lexema"] + ", "        
    return

def rTipo(tipo):  
    if(var.error == False):
        match(tipo): 
            case "inteiro":
                var.fileLines.append("\tint ")
            case "real":
                var.fileLines.append("\tfloat ")
            case "literal":
                var.fileLines.append("\tchar ")    
            case _: 
                print(tipo)

def r13(token): 
    if(var.error == False):
        if(token["tipo"] == "literal"):
            var.fileLines.append('\tscanf("%s", ' + token["lexema"] + ');\n')
        elif(token["tipo"] == "inteiro"):
            var.fileLines.append('\tscanf("%d", &' + token["lexema"] + ');\n')
        elif(token["tipo"] == "real"):
            var.fileLines.append('\tscanf("%lf", &' + token["lexema"] + ');\n')
        return
    else: 
        return
    
def r14(token):
    if(var.error == False):
        var.fileLines.append('\tprintf( ' + token["lexema"] + ' );\n')

def r19(l1, l2): 
    if(var.error == False):
        var.fileLines.append("\t" + l1['lexema'] + ' = ' + l2['lexema'] + ';\n')
        return 
    
def r20(tmp, l1, l2, opm):
    if(var.error == False):
        tmpLine = var.fileLines.index("\t// TMP\n")
        match (tmp["tipo"]): 
            case "inteiro":
                var.fileLines.insert(tmpLine + 1, "\t" + 'int '+ tmp['lexema'] + ';\n')
            case "real":
                var.fileLines.insert(tmpLine + 1, "\t" + 'float '+ tmp['lexema'] + ';\n')
            case _:
                var.fileLines.insert(tmpLine + 1, "\t" + 'char '+ tmp['lexema'] + '[256];\n')
        var.fileLines.append("\t" + tmp['lexema'] + '=' + l1['lexema'] + opm['lexema'] + l2['lexema'] + ';\n')

def r25(): 
    if(var.error == False):
        var.fileLines.append("}\n")

def r26():
    if(var.error == False):
        opr = var.semanticStack.pop()
        var.fileLines.append("if(" + opr['lexema'] + "){\n")

def r27(l1, oprd, l2, tmp): 
    if(var.error == False):
        tmpLine = var.fileLines.index("\t// TMP\n")
        
        var.fileLines.insert(tmpLine + 1, "\t" + 'bool '+ tmp['lexema'] + ';\n')
        var.fileLines.append("\t" + tmp['lexema'] + '=' + l1['lexema'] + oprd['lexema'] + l2['lexema'] + ';\n')
        var.semanticStack.append(tmp)