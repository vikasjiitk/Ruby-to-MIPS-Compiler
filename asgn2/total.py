MIPScode = []
MIPSDatacode = []
Instr3AC = []
NumRegister = 16
RegAvail = []
RegConstant = []
RegDescriptor = {}
AddDescriptor = {}
Dead = 0
Live = 1
leaders = [0]
Instr=0
Infinite = 10000000000
def initializeReg():
    global RegAvail
    global RegConstant
    global AddDescriptor
    global RegDescriptor
    RegAvail = ['$t0','$t1','$t2','$t3','$t4','$t5','$t6','$t7','$s0','$s1','$s2','$s3','$s4','$s5','$s6','$s7']
    RegConstant =[]
    RegDescriptor = {}
    for i in variables:
        AddDescriptor[i] = ['memory']

def dumpReg():
    global MIPScode
    global RegDescriptor
    for var in RegDescriptor:
        MIPScode.append('sw '+RegDescriptor[reg]+','+var)

def freeReg(Instr, symTableNo):
    global MIPScode
    global Instr3AC
    global RegDescriptor
    global RegConstant
    global AddDescriptor
    global Dead
    global RegAvail
    RegAvail = RegAvail+ RegConstant
    RegConstant =[]
    InstrVAR = [Instr3AC[Instr].input1,Instr3AC[Instr].input2, Instr3AC[Instr].output]
    for var in InstrVAR:
        if var in RegDescriptor:
            if symtables[symTableNo][var][0] == Dead:
                reg = RegDescriptor[var]
                del RegDescriptor[var]
                MIPScode.append('sw '+reg+','+var)
                AddDescriptor[var] = ['memory']
                RegAvail.append(reg)

def giveOperator(op):
    if op == '+':
        return 'add'
    elif op == '-':
        return 'sub'
    elif op == '*':
        return 'mul'
    elif op == '/':
        return 'div'
    else:
        return 0

def getreg(Instr, var, symTableNo):
    global MIPScode
    global RegConstant
    global RegDescriptor
    global AddDescriptor
    global RegAvail
    if (var in RegDescriptor):
        return RegDescriptor[var]
    if RegAvail: # there is a register in RegAvail       
    
        reg = RegAvail.pop()
        if(var.isdigit() == False):   # var passed is not a constant value
            MIPScode.append('lw '+reg+','+str(var))
            RegDescriptor[var] = reg            
            AddDescriptor[var].append('register')
        else:
            MIPScode.append('addi '+reg+',$0,'+var)
            RegConstant.append(reg)
        return reg
    else:
        InstrVAR = [Instr3AC[Instr].input1,Instr3AC[Instr].input2, Instr3AC[Instr].output]
        farthestNextUse = 0
        for VAR in symtables[symTableNo]:
            if VAR not in InstrVAR:
                if (symtables[symTableNo][VAR][1] > farthestNextUse):
                    farthestVar = VAR
                    farthestNextUse = symtables[symTableNo][VAR][1]
        
        reg = RegDescriptor[farthestVar]
        MIPScode.append('sw '+reg+','+farthestVar)
        AddDescriptor[farthestVar] = ['memory']
        del RegDescriptor[farthestVar]
        if(var.isdigit() == False):   # var passed is not a constant value
            MIPScode.append('lw '+reg+','+var)
            RegDescriptor[var] = reg
            AddDescriptor[var].append('register')
        else:
            MIPScode.append('addi '+reg+',$0,'+var)
            RegConstant.append(reg)
        return reg

def code_gen(initial, final):
    global MIPScode
    global Instr3AC
    for Instr in range(initial,final+1):
        symTableNo = Instr - initial +1
        if Instr3AC[Instr].instrType == 'ifgoto':
            reg1 = getreg(Instr, Instr3AC[Instr].input1, symTableNo)            
            if Instr3AC[Instr].operator in ["ble","blt","bge","bgt","beq","bne"]:
                reg2 = getreg(Instr, Instr3AC[Instr].input2, symTableNo)
                MIPScode.append('L'+str(Instr3AC[Instr].lineNo)+': '+Instr3AC[Instr].operator + ' '+ reg1+','+reg2 + ',' +'L' + str(Instr3AC[Instr].lineNo))
            else :
                MIPScode.append('L'+str(Instr3AC[Instr].lineNo)+': '+'bgtz ' + reg1 + ','+'L' + str(Instr3AC[Instr].lineNo))
            freeReg(Instr, symTableNo) 

        elif Instr3AC[Instr].instrType == 'FunctionCall':
            MIPScode.append('L'+str(Instr3AC[Instr].lineNo)+': '+'jal '+ Instr3AC[Instr].flabel) 
            if Instr3AC[Instr].output != "":                
                reg1 = getreg(Instr, Instr3AC[Instr].output, symTableNo)
                MIPScode.append('move '+ reg1 + ',$v1')         
            freeReg(Instr, symTableNo)

        elif Instr3AC[Instr].instrType == 'label':
            MIPScode.append(Instr3AC[Instr].flabel + ": ")
            freeReg(Instr, symTableNo)

        elif Instr3AC[Instr].instrType == 'return':            
            if Instr3AC[Instr].input1 != "":
                reg1 = getreg(Instr, Instr3AC[Instr].input1, symTableNo)
                MIPScode.append('L'+str(Instr3AC[Instr].lineNo)+': '+'move $v1, '+ reg1)
                MIPScode.append('jr $ra')
            else:
                MIPScode.append('L'+str(Instr3AC[Instr].lineNo)+': '+'jr $ra')
            freeReg(Instr, symTableNo)
        elif Instr3AC[Instr].instrType == 'print':
            MIPScode.append('L'+str(Instr3AC[Instr].lineNo)+': '+'li $v0, 1')

            reg1 = getreg(Instr, Instr3AC[Instr].input1, symTableNo)
            MIPScode.append('move $a0, '+ reg1)
            MIPScode.append('syscall')
        elif Instr3AC[Instr].operator == '+':
            reg1 = getreg(Instr, Instr3AC[Instr].input1, symTableNo)
            reg2 = getreg(Instr, Instr3AC[Instr].input2, symTableNo)
            reg3 = getreg(Instr, Instr3AC[Instr].output, symTableNo)
            MIPScode.append('L'+str(Instr3AC[Instr].lineNo)+': '+'add '+reg3+','+reg1+','+reg2)
            freeReg(Instr, symTableNo)

        elif Instr3AC[Instr].operator == '-':
            reg1 = getreg(Instr, Instr3AC[Instr].input1, symTableNo)
            reg2 = getreg(Instr, Instr3AC[Instr].input2, symTableNo)
            reg3 = getreg(Instr, Instr3AC[Instr].output, symTableNo)
            MIPScode.append('L'+str(Instr3AC[Instr].lineNo)+': '+'sub '+reg3+','+reg1+','+reg2)
            freeReg(Instr, symTableNo)

        elif Instr3AC[Instr].operator == '*':
            reg1 = getreg(Instr, Instr3AC[Instr].input1, symTableNo)
            reg2 = getreg(Instr, Instr3AC[Instr].input2, symTableNo)
            reg3 = getreg(Instr, Instr3AC[Instr].output, symTableNo)
            MIPScode.append('L'+str(Instr3AC[Instr].lineNo)+': '+'mult '+reg1+','+reg2)
            MIPScode.append('mflo '+reg3)
            freeReg(Instr, symTableNo)

        elif Instr3AC[Instr].operator == '/':
            reg1 = getreg(Instr, Instr3AC[Instr].input1, symTableNo)
            reg2 = getreg(Instr, Instr3AC[Instr].input2, symTableNo)
            reg3 = getreg(Instr, Instr3AC[Instr].output, symTableNo)
            MIPScode.append('L'+str(Instr3AC[Instr].lineNo)+': '+'div '+reg1+','+reg2)
            MIPScode.append('mflo '+reg3)
            freeReg(Instr, symTableNo)

        elif Instr3AC[Instr].operator == '%':
            reg1 = getreg(Instr, Instr3AC[Instr].input1, symTableNo)
            reg2 = getreg(Instr, Instr3AC[Instr].input2, symTableNo)
            reg3 = getreg(Instr, Instr3AC[Instr].output, symTableNo)
            MIPScode.append('L'+str(Instr3AC[Instr].lineNo)+': '+'div '+reg1+','+reg2)
            MIPScode.append('mfhi '+reg3)
            freeReg(Instr, symTableNo)

        elif Instr3AC[Instr].operator == '=':
            if (Instr3AC[Instr].input1.isdigit() == True):
                reg1 = getreg(Instr, Instr3AC[Instr].output, symTableNo)
                MIPScode.append('L'+str(Instr3AC[Instr].lineNo)+': '+'addi '+reg1+',$0,'+Instr3AC[Instr].input1)
            else:
                reg1 = getreg(Instr, Instr3AC[Instr].input1)
                reg3 = getreg(Instr, Instr3AC[Instr].ouput)
                MIPScode.append('L'+str(Instr3AC[Instr].lineNo)+': '+'move '+reg3+','+reg1)
            freeReg(Instr, symTableNo)


#import codegenerator.py



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
    initializeReg()    
    code_gen(initial,final)
    dumpReg()
for i in range(0,len(MIPSDatacode)):
    print MIPSDatacode[i]
for i in range(0,len(MIPScode)):
    print MIPScode[i]