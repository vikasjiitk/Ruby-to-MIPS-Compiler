import codegenerator as cg

class threeAddCode:
    instrType = ""
    input1 = ""
    input2 = ""
    output = ""
    target = ""
    operator = ""
    lineNo = 0
    leader = False
    flabel = ""

def Equal(i,words):
    # global cg.Instr3AC
    cg.Instr3AC[i].instrType = "Assignment"
    cg.Instr3AC[i].output = words[2]
    cg.Instr3AC[i].input1 = words[3]

def Arithmetic(i,words):
    cg.Instr3AC[i].instrType = "Arithmetic"
    if words[1] in ['+','-','/','*','%']:
        cg.Instr3AC[i].output = words[2]
        cg.Instr3AC[i].input1 = words[3]
        cg.Instr3AC[i].input2 = words[4]
    else:
        cg.Instr3AC[i].operator = words[1][0]
        cg.Instr3AC[i].output = cg.Instr3AC[i].input1 = words[2]
        cg.Instr3AC[i].input2 = words[3]

def Logical(i, words):
    cg.Instr3AC[i].instrType = "logical"
    cg.Instr3AC[i].output = words[2]
    cg.Instr3AC[i].input1 = words[3]
    cg.Instr3AC[i].input2 = words[4]

def Ifgoto(i,words):
    cg.Instr3AC[i].instrType = "ifgoto"
    if words[2] in ["ble","blt","bge","bgt","beq","bne"]:
        cg.Instr3AC[i].operator = words[2]
        cg.Instr3AC[i].input1 = words[3]
        cg.Instr3AC[i].input2 = words[4]
    else:
        cg.Instr3AC[i].input1 = words[2]
    cg.Instr3AC[i].target = words[-1]

def Function(i,words):
    cg.Instr3AC[i].instrType = "FunctionCall"
    cg.Instr3AC[i].flabel = words[2]
    if len(words) == 4:
        cg.Instr3AC[i].output = words[3]

def Return(i,words):
    cg.Instr3AC[i].instrType = "return"
    if len(words) == 3:
        cg.Instr3AC[i].input1 = words[2]

def Label(i,words):
    cg.Instr3AC[i].instrType = "label"
    cg.Instr3AC[i].flabel = words[2]

def Print(i,words):
    cg.Instr3AC[i].instrType  = "print"
    cg.Instr3AC[i].input1 = words[2]

def Scan(i,words):
    cg.Instr3AC[i].instrType = "scan"
    cg.Instr3AC[i].output = words[2]

def getVariables(NumInstr):

    cg.variables = []
    for i in range(NumInstr):
        if (cg.is_int(cg.Instr3AC[i].input1) == False and cg.Instr3AC[i].input1!= ""):
            cg.variables.append(cg.Instr3AC[i].input1)
        if (cg.is_int(cg.Instr3AC[i].input2) == False and cg.Instr3AC[i].input2!= ""):
            cg.variables.append(cg.Instr3AC[i].input2)
        if (cg.is_int(cg.Instr3AC[i].output) == False and cg.Instr3AC[i].output!= ""):
            cg.variables.append(cg.Instr3AC[i].output)
    cg.variables = set(cg.variables)
    return cg.variables

def getInstrSet(f):

    for line in f:
        if line[-1] == '\n':
            line = line[:-1]
        words = line.split(',')
        # for i in range(len(words)):
        #     if(words[i] == 'b'):
        #         words[i] = 'belikejanish'
        cg.Instr3AC.append(threeAddCode())
        cg.Instr3AC[cg.Instr].lineNo = int(words[0])
        cg.Instr3AC[cg.Instr].operator = words[1]
        #print words
        if words[1] == '=':
            Equal(cg.Instr,words)
        elif words[1] in ['+','-','/','*','%','+=', '-=', '*=', '/=', '%=']:
            Arithmetic(cg.Instr,words)
        elif words[1] in ['^','|','&','<<','>>','~|','>>>']:
            Logical(cg.Instr,words)
        elif words[1] == 'ifgoto':
            cg.leaders.append(cg.Instr3AC[cg.Instr].lineNo + 1)
            cg.leaders.append(int(words[-1]))
            Ifgoto(cg.Instr,words)
        elif words[1] == 'call':
            cg.leaders.append(cg.Instr3AC[cg.Instr].lineNo + 1)
            Function(cg.Instr, words)
        elif words[1] == 'label':
            cg.leaders.append(cg.Instr3AC[cg.Instr].lineNo)
            Label(cg.Instr,words)
        elif words[1] == 'ret':
            Return(cg.Instr,words)
        elif words[1] == 'print':
            Print(cg.Instr,words)
        elif words[1] == 'scan':
            Scan(cg.Instr,words)

        if(cg.is_int(cg.Instr3AC[cg.Instr].input1) == False and cg.is_int(cg.Instr3AC[cg.Instr].input1) != "" ):
            cg.Instr3AC[cg.Instr].input1 += '1'
        if(cg.is_int(cg.Instr3AC[cg.Instr].input2) == False and cg.is_int(cg.Instr3AC[cg.Instr].input2) != "" ):
            cg.Instr3AC[cg.Instr].input2 += '1'
        if(cg.is_int(cg.Instr3AC[cg.Instr].output) == False and cg.is_int(cg.Instr3AC[cg.Instr].output) != "" ):
            cg.Instr3AC[cg.Instr].output += '1'
        cg.Instr = cg.Instr+1
    cg.leaders.append(cg.Instr)
    cg.leaders = sorted(set(cg.leaders))
    return cg.Instr
