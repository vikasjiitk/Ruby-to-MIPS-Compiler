MIPScode = []
MIPSDatacode = []
Instr3AC = []
# NumRegister = 16
NumRegister = 3
RegAvail = []
RegConstant = []
RegDescriptor = {}
AddDescriptor = {}
symtables = []
Dead = 0
Live = 1
leaders = [0]
Instr=0
Infinite = 10000000000
variables =[]
exit = False
def initializeReg():
    global RegAvail
    global RegConstant
    global AddDescriptor
    global RegDescriptor
    RegAvail = ['$t0','$t1','$t2']
    # RegAvail = ['$t0','$t1','$t2','$t3','$t4','$t5','$t6','$t7','$s0','$s1','$s2','$s3','$s4','$s5','$s6','$s7']
    RegConstant =[]
    RegDescriptor = {}
    for i in variables:
        AddDescriptor[i] = ['memory']

def dumpReg():
    global MIPScode
    global RegDescriptor
    VARS =[]
    for var in RegDescriptor:
        reg = RegDescriptor[var]
        MIPScode.append('sw '+reg+','+var)
        AddDescriptor[var]=['memory']
        VARS.append(var)
        RegAvail.append(reg)
    for var in VARS:
        del RegDescriptor[var]


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
                # print symtables[symTableNo-2]
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
            if(not(Instr3AC[Instr].output == var and Instr3AC[Instr].input1 != var and Instr3AC[Instr].input2 != var)):
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
            if (VAR not in InstrVAR and VAR in RegDescriptor):
                if (symtables[symTableNo][VAR][1] > farthestNextUse):
                    farthestVar = VAR
                    farthestNextUse = symtables[symTableNo][VAR][1]

        reg = RegDescriptor[farthestVar]
        MIPScode.append('sw '+reg+','+farthestVar)
        AddDescriptor[farthestVar] = ['memory']
        del RegDescriptor[farthestVar]
        if(var.isdigit() == False):   # var passed is not a constant value
            if(not(Instr3AC[Instr].output == var and Instr3AC[Instr].input1 != var and Instr3AC[Instr].input2 != var)):
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
    global exit
    for Instr in range(initial,final+1):
        if Instr3AC[Instr].instrType != 'label':
            MIPScode.append('L'+str(Instr3AC[Instr].lineNo)+': ')
        symTableNo = Instr - initial +1
        if Instr3AC[Instr].instrType == 'ifgoto':
            dumpReg()
            reg1 = getreg(Instr, Instr3AC[Instr].input1, symTableNo)
            if Instr3AC[Instr].operator in ["ble","blt","bge","bgt","beq","bne"]:
                reg2 = getreg(Instr, Instr3AC[Instr].input2, symTableNo)
                MIPScode.append(Instr3AC[Instr].operator + ' '+ reg1+','+reg2 + ',' +'L' + str(Instr3AC[Instr].target))
            else :
                MIPScode.append('bgtz ' + reg1 + ','+'L' + str(Instr3AC[Instr].lineNo))
            freeReg(Instr, symTableNo)

        elif Instr3AC[Instr].instrType == 'FunctionCall':
            dumpReg()
            MIPScode.append('jal '+ Instr3AC[Instr].flabel)
            if Instr3AC[Instr].output != "":
                reg1 = getreg(Instr, Instr3AC[Instr].output, symTableNo)
                MIPScode.append('move '+ reg1 + ',$v1')
            freeReg(Instr, symTableNo)

        elif Instr3AC[Instr].instrType == 'label':
            MIPScode.append(Instr3AC[Instr].flabel + ": ")
            if Instr3AC[Instr].flabel == "main":
                exit = True
            freeReg(Instr, symTableNo)

        elif Instr3AC[Instr].instrType == 'return':
        	if exit == True:
        		MIPScode.append('li $v0, 10')
        		MIPScode.append('syscall')
        		exit = False
        	else:
	            if Instr3AC[Instr].input1 != "":
	                reg1 = getreg(Instr, Instr3AC[Instr].input1, symTableNo)
	                MIPScode.append('move $v1, '+ reg1)
	                MIPScode.append('jr $ra')
	            else:
	                MIPScode.append('jr $ra')
	            freeReg(Instr, symTableNo)
        elif Instr3AC[Instr].instrType == 'print':
            MIPScode.append('li $v0, 1')

            reg1 = getreg(Instr, Instr3AC[Instr].input1, symTableNo)
            MIPScode.append('move $a0, '+ reg1)
            MIPScode.append('syscall')
        elif Instr3AC[Instr].operator == '+':
            reg1 = getreg(Instr, Instr3AC[Instr].input1, symTableNo)
            reg2 = getreg(Instr, Instr3AC[Instr].input2, symTableNo)
            reg3 = getreg(Instr, Instr3AC[Instr].output, symTableNo)
            MIPScode.append('add '+reg3+','+reg1+','+reg2)
            freeReg(Instr, symTableNo)

        elif Instr3AC[Instr].operator == '-':
            reg1 = getreg(Instr, Instr3AC[Instr].input1, symTableNo)
            reg2 = getreg(Instr, Instr3AC[Instr].input2, symTableNo)
            reg3 = getreg(Instr, Instr3AC[Instr].output, symTableNo)
            MIPScode.append('sub '+reg3+','+reg1+','+reg2)
            freeReg(Instr, symTableNo)

        elif Instr3AC[Instr].operator == '*':
            reg1 = getreg(Instr, Instr3AC[Instr].input1, symTableNo)
            reg2 = getreg(Instr, Instr3AC[Instr].input2, symTableNo)
            reg3 = getreg(Instr, Instr3AC[Instr].output, symTableNo)
            MIPScode.append('mult '+reg1+','+reg2)
            MIPScode.append('mflo '+reg3)
            freeReg(Instr, symTableNo)

        elif Instr3AC[Instr].operator == '/':
            reg1 = getreg(Instr, Instr3AC[Instr].input1, symTableNo)
            reg2 = getreg(Instr, Instr3AC[Instr].input2, symTableNo)
            reg3 = getreg(Instr, Instr3AC[Instr].output, symTableNo)
            MIPScode.append('div '+reg1+','+reg2)
            MIPScode.append('mflo '+reg3)
            freeReg(Instr, symTableNo)

        elif Instr3AC[Instr].operator == '%':
            reg1 = getreg(Instr, Instr3AC[Instr].input1, symTableNo)
            reg2 = getreg(Instr, Instr3AC[Instr].input2, symTableNo)
            reg3 = getreg(Instr, Instr3AC[Instr].output, symTableNo)
            MIPScode.append('div '+reg1+','+reg2)
            MIPScode.append('mfhi '+reg3)
            freeReg(Instr, symTableNo)

        elif Instr3AC[Instr].operator == '=':
            if (Instr3AC[Instr].input1.isdigit() == True):
                reg1 = getreg(Instr, Instr3AC[Instr].output, symTableNo)
                MIPScode.append('addi '+reg1+',$0,'+Instr3AC[Instr].input1)
            else:
                reg1 = getreg(Instr, Instr3AC[Instr].input1,symTableNo)
                reg3 = getreg(Instr, Instr3AC[Instr].output,symTableNo)
                MIPScode.append('move '+reg3+','+reg1)
            freeReg(Instr, symTableNo)
