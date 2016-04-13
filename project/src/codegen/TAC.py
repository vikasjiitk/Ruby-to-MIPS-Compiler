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
    label = ""

def Equal(i,words):
    # global cg.Instr3AC
    cg.Instr3AC[i].instrType = "Assignment"
    cg.Instr3AC[i].output = words[1]
    cg.Instr3AC[i].input1 = words[2]

def Arithmetic(i,words):
    cg.Instr3AC[i].instrType = "Arithmetic"
    if words[0] in ['+','-','/','*','%']:
        cg.Instr3AC[i].output = words[1]
        cg.Instr3AC[i].input1 = words[2]
        cg.Instr3AC[i].input2 = words[3]
    else:
        cg.Instr3AC[i].operator = words[0][0]
        cg.Instr3AC[i].output = cg.Instr3AC[i].input1 = words[1]
        cg.Instr3AC[i].input2 = words[2]

def Logical(i, words):
    cg.Instr3AC[i].instrType = "logical"
    cg.Instr3AC[i].output = words[1]
    cg.Instr3AC[i].input1 = words[2]
    cg.Instr3AC[i].input2 = words[3]

def Ifgoto(i,words):
    cg.Instr3AC[i].instrType = "ifgoto"
    if words[1] in ["ble","blt","bge","bgt","beq","bne","bg","bl"]:
        cg.Instr3AC[i].operator = words[1]
        cg.Instr3AC[i].input1 = words[2]
        cg.Instr3AC[i].input2 = words[3]
    else:
        cg.Instr3AC[i].input1 = words[1]
    cg.Instr3AC[i].target = words[-1]

def Function(i,words):
    cg.Instr3AC[i].instrType = "FunctionCall"
    cg.Instr3AC[i].label = words[1]
    if len(words) == 3:
        cg.Instr3AC[i].output = words[2]

def Return(i,words):
    cg.Instr3AC[i].instrType = "return"
    if len(words) == 2:
        cg.Instr3AC[i].input1 = words[1]

def Label(i,words):
    cg.Instr3AC[i].instrType = "label"
    cg.Instr3AC[i].label = words[1]

def fLabel(i,words):
    cg.Instr3AC[i].instrType = "flabel"
    cg.Instr3AC[i].label = words[1]

def Print(i,words):
    cg.Instr3AC[i].instrType  = "print"
    cg.Instr3AC[i].input1 = words[1]

def Prints(i,words):
    cg.Instr3AC[i].instrType  = "prints"
    cg.Instr3AC[i].input1 = words[1]


def Scan(i,words):
    cg.Instr3AC[i].instrType = "scan"
    cg.Instr3AC[i].output = words[1]

def Goto(i,words):
    cg.Instr3AC[i].instrType = "goto"
    cg.Instr3AC[i].label = words[1]

def Exit(i,words):
    cg.Instr3AC[i].instrType = "exit"

def param(i, words):
    cg.Instr3AC[i].instrType = "param"
    cg.Instr3AC[i].input1 = words[1]

def funcarg(i, words):
    cg.Instr3AC[i].instrType = "funcarg"
    cg.Instr3AC[i].input1 = words[1]
    cg.Instr3AC[i].input2 = words[2]

def getVariables(NumInstr):
    cg.variables = []
    stringNo = 0;
    for i in range(NumInstr):
        if(cg.Instr3AC[i].input1=='[]'): #a=[] handling arrays
            cg.arrays[cg.Instr3AC[i].output] = "array";
        else:    #handling int variables and strings
            if (cg.is_int(cg.Instr3AC[i].input1) == False and cg.Instr3AC[i].input1!= "" and (not cg.Instr3AC[i].input1[-1] == ']') ):
                if not(cg.Instr3AC[i].input1[0] == '"' or cg.Instr3AC[i].input1[0] == "'"):
                    if(cg.Instr3AC[i].input1 not in cg.arrays.keys()):
                        cg.variables.append(cg.Instr3AC[i].input1)
                else:   #handling string constants
                    cg.strings[cg.Instr3AC[i].input1[1:-2]] = 'str'+str(stringNo)
                    stringNo += 1
            if (cg.is_int(cg.Instr3AC[i].input2) == False and cg.Instr3AC[i].input2!= "" and (not cg.Instr3AC[i].input2[-1] == ']')):
                if not(cg.Instr3AC[i].input2[0] == '"' or cg.Instr3AC[i].input2[0] == "'"):
                    cg.variables.append(cg.Instr3AC[i].input2)
            if ((cg.is_int(cg.Instr3AC[i].output) == False and cg.Instr3AC[i].output!= "" )and (not cg.Instr3AC[i].output[-1] == ']')):
                if not(cg.Instr3AC[i].output[0] == '"' or cg.Instr3AC[i].output[0] == "'"):
                    cg.variables.append(cg.Instr3AC[i].output)
    cg.variables = set(cg.variables)
    return cg.variables

def getInstrSet(f):
    lin = 0
    for line in f:
        if line[-1] == '\n':
            line = line[:-1]
        words = line.split(',')
        # for i in range(len(words)):
        #     if(words[i] == 'b'):
        #         words[i] = 'belikejanish'
        cg.Instr3AC.append(threeAddCode())
        cg.Instr3AC[cg.Instr].lineNo = lin
        lin += 1
        cg.Instr3AC[cg.Instr].operator = words[0]
        #print words
        if words[0] == '=':
            Equal(cg.Instr,words)
        elif words[0] in ['+','-','/','*','%','+=', '-=', '*=', '/=', '%=']:
            Arithmetic(cg.Instr,words)
        elif words[0] in ['^','|','&','<<','>>','~|','>>>']:
            Logical(cg.Instr,words)
        elif words[0] == 'ifgoto':
            cg.leaders.append(cg.Instr3AC[cg.Instr].lineNo + 1)
            # cg.leaders.append(int(words[-1]))
            Ifgoto(cg.Instr,words)
        elif words[0] == 'call':
            cg.leaders.append(cg.Instr3AC[cg.Instr].lineNo + 1)
            Function(cg.Instr, words)
        elif words[0] == 'label':
            cg.leaders.append(cg.Instr3AC[cg.Instr].lineNo)
            Label(cg.Instr,words)
        elif words[0] == 'flabel':
            cg.leaders.append(cg.Instr3AC[cg.Instr].lineNo)
            fLabel(cg.Instr,words)
        elif words[0] == 'return':
            Return(cg.Instr,words)
        elif words[0] == 'print':
            Print(cg.Instr,words)
        elif words[0] == 'scan':
            Scan(cg.Instr,words)
        elif words[0] == 'goto':
            Goto(cg.Instr,words)
        elif words[0] == 'exit':
            Exit(cg.Instr,words)
        elif words[0] == 'prints':
            Prints(cg.Instr,words)
        elif words[0] == 'param':
            param(cg.Instr, words)
        elif words[0] == 'funcarg':
            funcarg(cg.Instr, words)

        if((not cg.Instr3AC[cg.Instr].input1=='[]') and cg.is_int(cg.Instr3AC[cg.Instr].input1) == False and (cg.Instr3AC[cg.Instr].input1) != ""  and (not cg.Instr3AC[cg.Instr].input1[-1] == ']')):
            cg.Instr3AC[cg.Instr].input1 += '1'
        if((cg.is_int(cg.Instr3AC[cg.Instr].input2) == False and (cg.Instr3AC[cg.Instr].input2) != "") and (not cg.Instr3AC[cg.Instr].input2[-1] == ']')):
            cg.Instr3AC[cg.Instr].input2 += '1'
        if(cg.is_int(cg.Instr3AC[cg.Instr].output) == False and (cg.Instr3AC[cg.Instr].output) != "" and (not cg.Instr3AC[cg.Instr].output[-1] == ']')):
            cg.Instr3AC[cg.Instr].output += '1'
        cg.Instr = cg.Instr+1
    cg.leaders.append(cg.Instr)
    cg.leaders = sorted(set(cg.leaders))
    return cg.Instr
