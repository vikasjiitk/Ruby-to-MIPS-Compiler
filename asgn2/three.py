import codegenerator

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
    global Instr3AC
    Instr3AC[i].instrType = "Assignment"
    Instr3AC[i].output = words[2]
    Instr3AC[i].input1 = words[3]
#   return Instr3AC.output,Instr3AC.input1
def Arithmetic(i,words):
    global Instr3AC
    Instr3AC[i].instrType = "Arithmetic"
    Instr3AC[i].output = words[2]
    Instr3AC[i].input1 = words[3]
    Instr3AC[i].input2 = words[4]
#   return Instr3AC.output,Instr3AC.input1, Instr3AC.input2
def Ifgoto(i,words):
    global Instr3AC
    Instr3AC[i].instrType = "ifgoto"
    if words[2] in ["ble","blt","bge","bgt","beq","bne"]:
        Instr3AC[i].operator = words[2]
        Instr3AC[i].input1 = words[3]
        Instr3AC[i].input2 = words[4]
    else:
        Instr3AC[i].input1 = words[2]
    Instr3AC[i].target = words[-1]
def Function(i,words):
    global Instr3AC
    Instr3AC[i].instrType = "FunctionCall"
    Instr3AC[i].flabel = words[2]
    if len(words) == 4:
        Instr3AC[i].output = words[3]
def Return(i,words):
    global Instr3AC
    Instr3AC[i].instrType = "return"
    if len(words) == 3:
        Instr3AC[i].input1 = words[2]
def Label(i,words):
    global Instr3AC
    Instr3AC[i].instrType = "label"
    Instr3AC[i].flabel = words[2]
def Print(i,words):
    global Instr3AC
    Instr3AC[i].instrType  = "print"
    Instr3AC[i].input1 = words[2]
def getSymTables(initialInstr, finalInstr, blockLength):
    global Instr3AC
    global Dead
    global Infinite
    symtables = [dict() for x in range(blockLength+1)]
    for blockLine in range(initialInstr,finalInstr+1):
        if (Instr3AC[blockLine].input1.isdigit() == False and Instr3AC[blockLine].input1!= ""):
            if Instr3AC[blockLine].input1 not in symtables[0]:
                for k in range(blockLength+1):
                    symtables[k][Instr3AC[blockLine].input1] = [Dead, Infinite]
        if (Instr3AC[blockLine].input2.isdigit() == False and Instr3AC[blockLine].input2!= ""):
            if Instr3AC[blockLine].input2 not in symtables[0]:
                for k in range(blockLength+1):
                    symtables[k][Instr3AC[blockLine].input2] = [Dead, Infinite]
        if Instr3AC[blockLine].output not in symtables[0] and Instr3AC[blockLine].output!="":
                for k in range(blockLength+1):
                    symtables[k][Instr3AC[blockLine].output] = [Dead, Infinite]
    return symtables

def fillSymTables(symtables,initialInstr,finalInstr,blockLength):
    global Instr3AC
    global Dead
    global Live
    scan = blockLength-1
    for blockLine in range(finalInstr, initialInstr -1 , -1):
        if blockLine!=finalInstr:
            symtables[scan]=symtables[scan+1].copy()                                #copying the previous filled dictionary for further changes
        if (Instr3AC[blockLine].input1.isdigit() == False and Instr3AC[blockLine].input1!= ""):
            symtables[scan][Instr3AC[blockLine].input1] = [Live, blockLine]
        if (Instr3AC[blockLine].input2.isdigit() == False and Instr3AC[blockLine].input2!= ""):
            symtables[scan][Instr3AC[blockLine].input2] = [Live, blockLine]
        if (Instr3AC[blockLine].output!= ""):
            symtables[scan][Instr3AC[blockLine].output] = [Dead, 0]
        scan = scan-1
        #print 'symbol table before ' + str(blockLine)
        #print symtables[blockLine-initial]
        return symtables

def getVariables(NumInstr):
    global Instr3AC
    variables = []
    for i in range(NumInstr):
        if (Instr3AC[i].input1.isdigit() == False and Instr3AC[i].input1!= ""):
            variables.append(Instr3AC[i].input1)
        if (Instr3AC[i].input2.isdigit() == False and Instr3AC[i].input2!= ""):
            variables.append(Instr3AC[i].input2)
        if (Instr3AC[i].output.isdigit() == False and Instr3AC[i].output!= ""):
            variables.append(Instr3AC[i].output)
    variables = set(variables)
    return variables

def getInstrSet(f):
    global Instr3AC
    global Instr
    global leaders
    for line in f:
        line = line[:-1]
        words = line.split(',')
        Instr3AC.append(threeAddCode())
        Instr3AC[Instr].lineNo = int(words[0])
        Instr3AC[Instr].operator = words[1]
        #print words
        if words[1] == '=':
            Equal(Instr,words)
        elif words[1] in ['+','-','/','*','%']:
            Arithmetic(Instr,words)
        elif words[1] == 'ifgoto':
            leaders.append(Instr3AC[Instr].lineNo + 1)
            leaders.append(int(words[-1]))
            Ifgoto(Instr,words)
        elif words[1] == 'call':
            leaders.append(Instr3AC[Instr].lineNo + 1)
            Function(Instr, words)          
        elif words[1] == 'label':
            leaders.append(Instr3AC[Instr].lineNo)
            Label(Instr,words)
        elif words[1] == 'ret':
            Return(Instr,words)
        elif words[1] == 'print':
            Print(Instr,words)
        Instr = Instr+1
    leaders.append(Instr)
    leaders = sorted(set(leaders))
    return Instr

def fillDataSection(variables):
    global MIPSDatacode
    MIPSDatacode.append('.data')
    for var in variables:
        MIPSDatacode.append(var+': .word 0')
    MIPSDatacode.append('.text')    

f = open('/home/janish/Desktop/test/test1.txt','r')
# getInstrSet fills Instr3AC[] structure and also finds leaders in the 3AC instruction set
NumInstr = getInstrSet(f)
variables = getVariables(NumInstr)

fillDataSection(variables)

for blockNum in range(len(leaders)-1):
    initial = leaders[blockNum]
    final = leaders[blockNum+1] - 1
    blockLength = final - initial + 1
    # Building blockLength number of symbol tables (one for each program point)
    symtables = getSymTables(initial, final, blockLength)
    ## Backward scanning and filling symbol table for each program point
    symtables = fillSymTables(symtables,initial,final,blockLength)   
    codegenerator.initializeReg()    
    codegenerator.code_gen(initial,final)
    codegenerator.dumpReg()
for i in range(0,len(MIPSDatacode)):
    print MIPSDatacode[i]
for i in range(0,len(MIPScode)):
    print MIPScode[i]