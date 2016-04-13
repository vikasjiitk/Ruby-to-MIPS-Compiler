MIPScode = []
MIPSDatacode = []
Instr3AC = []
NumRegister = 16
# NumRegister = 3
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
arrays={}
strings = {}
exit = False
paramReg = 0

def is_int(s):
    try:
        int(s)
        return True
    except ValueError:
        return False


def initializeReg():
    global RegAvail
    global RegConstant
    global AddDescriptor
    global RegDescriptor
    # RegAvail = ['$t0','$t1','$t2']
    RegAvail = ['$t0','$t1','$t2','$t3','$t4','$t5','$t6','$t7','$s0','$s1','$s2','$s3','$s4','$s5','$s6','$s7']
    RegConstant =[]
    RegDescriptor = {}
    for i in variables:
        AddDescriptor[i] = ['memory']
    # for i in arrays:
    #     AddDescriptor[i] = ['memory']

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
        if(is_int(var) == False):   # var passed is not a constant value
            if(not(Instr3AC[Instr].output == var and Instr3AC[Instr].input1 != var and Instr3AC[Instr].input2 != var)):
                MIPScode.append('lw '+reg+','+str(var))
            RegDescriptor[var] = reg
            # print var
            # print AddDescriptor
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
        if(is_int(var) == False):   # var passed is not a constant value
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
    global paramReg
    global Instr3AC
    global exit
    for Instr in range(initial,final+1):
        # if Instr3AC[Instr].instrType != 'label':
        #     MIPScode.append('L'+str(Instr3AC[Instr].lineNo)+': ')
        symTableNo = Instr - initial +1
        if Instr3AC[Instr].instrType == 'ifgoto':
            dumpReg()
            reg1 = getreg(Instr, Instr3AC[Instr].input1, symTableNo)
            if Instr3AC[Instr].operator in ["ble","blt","bge","bgt","beq","bne"]:
                reg2 = getreg(Instr, Instr3AC[Instr].input2, symTableNo)
                MIPScode.append(Instr3AC[Instr].operator + ' '+ reg1+','+reg2 + ','+ str(Instr3AC[Instr].target))
            else:
                reg2 = getreg(Instr, Instr3AC[Instr].input2, symTableNo)
                reg3 = getreg(Instr, '0', symTableNo)
                if(Instr3AC[Instr].operator == "bg"):
                    MIPScode.append('sub '+reg3+','+reg1+','+reg2)
                    MIPScode.append('bgtz ' + reg3 + ','+ str(Instr3AC[Instr].target)) #useless
                elif(Instr3AC[Instr].operator == "bl"):
                    MIPScode.append('sub '+reg3+','+reg2+','+reg1)
                    MIPScode.append('bgtz ' + reg3 + ','+ str(Instr3AC[Instr].target)) #useless
            freeReg(Instr, symTableNo)

        elif Instr3AC[Instr].instrType == 'FunctionCall':
            dumpReg()
            MIPScode.append('jal '+ Instr3AC[Instr].label)
            if Instr3AC[Instr].output != "":
                reg1 = getreg(Instr, Instr3AC[Instr].output, symTableNo)
                MIPScode.append('move '+ reg1 + ',$v1')
            freeReg(Instr, symTableNo)
            paramReg = 0

        elif Instr3AC[Instr].instrType == 'param':
            reg1 = getreg(Instr, Instr3AC[Instr].input1, symTableNo)
            MIPScode.append('move ' + '$a'+str(paramReg)+','+reg1)
            paramReg += 1

        elif Instr3AC[Instr].instrType == "funcarg":
            reg1 = getreg(Instr, Instr3AC[Instr].input1, symTableNo)
            MIPScode.append('move '+ reg1 + ',$a'+Instr3AC[Instr].input2)

        elif Instr3AC[Instr].instrType == 'label':
            MIPScode.append(Instr3AC[Instr].label + ": ")
            if Instr3AC[Instr].label == "main":
                exit = True
            freeReg(Instr, symTableNo)

        elif Instr3AC[Instr].instrType == 'flabel':
            MIPScode.append(Instr3AC[Instr].label + ": ")
            MIPScode.append('addi $sp,$sp,-4')
            MIPScode.append('sw $ra,0($sp)')
            freeReg(Instr, symTableNo)

        elif Instr3AC[Instr].instrType == 'goto':
            MIPScode.append("j "+ Instr3AC[Instr].label)
            # if Instr3AC[Instr].label == "main":
            #     exit = True
            freeReg(Instr, symTableNo)

        elif Instr3AC[Instr].instrType == 'exit':
            MIPScode.append('li $v0, 10')
            MIPScode.append('syscall')

        elif Instr3AC[Instr].instrType == 'return':
            if exit == True:
        		MIPScode.append('li $v0, 10')
        		MIPScode.append('syscall')
        		exit = False
            else:
                if Instr3AC[Instr].input1 != "":
                    reg1 = getreg(Instr, Instr3AC[Instr].input1, symTableNo)
                    MIPScode.append('move $v1, '+ reg1)
                    MIPScode.append('lw $ra,0($sp)')
                    MIPScode.append('addi $sp,$sp,4')
                    MIPScode.append('jr $ra')
                else:
                    MIPScode.append('lw $ra,0($sp)')
                    MIPScode.append('addi $sp,$sp,4')
                    MIPScode.append('jr $ra')
                freeReg(Instr, symTableNo)

        elif Instr3AC[Instr].instrType == 'print':
            MIPScode.append('li $v0, 1')
            reg1 = getreg(Instr, Instr3AC[Instr].input1, symTableNo)
            MIPScode.append('move $a0, '+ reg1)
            MIPScode.append('syscall')
            freeReg(Instr, symTableNo)

        elif Instr3AC[Instr].instrType == 'prints':
            MIPScode.append('li $v0, 4')
            reg1 = getreg(Instr, Instr3AC[Instr].input1, symTableNo)
            MIPScode.append('move $a0, '+ reg1)
            MIPScode.append('syscall')
            freeReg(Instr, symTableNo)

        elif Instr3AC[Instr].instrType == 'scan':
            reg1 = getreg(Instr, Instr3AC[Instr].output, symTableNo)
            MIPScode.append('li $v0,5')
            MIPScode.append('syscall')
            MIPScode.append('move '+reg1+', '+'$v0')
            freeReg(Instr, symTableNo)

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
            if(Instr3AC[Instr].input1 in arrays.keys()):
                arrays[Instr3AC[Instr].output] = "pointer"
                reg1 = getreg(Instr, Instr3AC[Instr].output, symTableNo)
                MIPScode.append('la ' + reg1 + ',' + Instr3AC[Instr].input1)
            elif (Instr3AC[Instr].input1 == '[]'):
                paramReg = paramReg
                # nothing has to be done
                # reg1 = getreg(Instr, Instr3AC[Instr].output, symTableNo)
                # MIPScode.append('la '+reg1+','+Instr3AC[Instr].output)
            elif(Instr3AC[Instr].output[-1] == ']'):
                ind = Instr3AC[Instr].output.find('[')
                index = Instr3AC[Instr].output[ind+1:-1]
                if(is_int(index) == False):
                    index += '1'
                myarray = Instr3AC[Instr].output[0:ind]
                myarray += '1'
                reg1 = getreg(Instr, Instr3AC[Instr].input1, symTableNo)
                reg2 = getreg(Instr, index, symTableNo)
                reg3 = getreg(Instr, '4', symTableNo)
                MIPScode.append('mult '+reg2+','+reg3)
                MIPScode.append('mflo '+reg2)
                if(arrays[myarray] == 'array'):
                    MIPScode.append('sw ' + reg1 + ',' + myarray + '('+reg2+')')
                else:
                    reg4 = getreg(Instr, myarray, symTableNo)
                    reg5 = getreg(Instr, '0', symTableNo)
                    MIPScode.append('add '+ reg5+','+reg4+','+reg2)
                    MIPScode.append('sw ' + reg1 + ',' + '0('+ reg5 +')')
            elif (Instr3AC[Instr].input1[-1] == ']'):
                ind = Instr3AC[Instr].input1.find('[')
                index = Instr3AC[Instr].input1[ind+1:-1]
                if(is_int(index) == False):
                    index += '1'
                myarray = Instr3AC[Instr].input1[0:ind]
                myarray += '1'
                # print 'myarray'+myarray
                reg1 = getreg(Instr, Instr3AC[Instr].output, symTableNo)
                reg2 = getreg(Instr, index, symTableNo)
                reg3 = getreg(Instr, '4', symTableNo)
                MIPScode.append('mult '+reg2+','+reg3)
                MIPScode.append('mflo '+reg2)
                if(arrays[myarray] == 'array'):
                    MIPScode.append('lw ' + reg1 + ',' + myarray + '('+reg2+')')
                else:
                    reg4 = getreg(Instr, myarray, symTableNo)
                    reg5 = getreg(Instr, '0', symTableNo)
                    MIPScode.append('add '+ reg5+','+reg4+','+reg2)
                    MIPScode.append('lw ' + reg1 + ',' + '0('+ reg5 +')')
            elif (Instr3AC[Instr].input1[0] == '"' or Instr3AC[Instr].input1[0] == "'"):  #handling string constants
                reg1 = getreg(Instr, Instr3AC[Instr].output, symTableNo)
                MIPScode.append('la '+reg1+','+strings[Instr3AC[Instr].input1[1:-2]])
            elif (is_int(Instr3AC[Instr].input1) == True):
                reg1 = getreg(Instr, Instr3AC[Instr].output, symTableNo)
                MIPScode.append('addi '+reg1+',$0,'+Instr3AC[Instr].input1)
            else:
                reg1 = getreg(Instr, Instr3AC[Instr].input1,symTableNo)
                reg3 = getreg(Instr, Instr3AC[Instr].output,symTableNo)
                MIPScode.append('move '+reg3+','+reg1)
            freeReg(Instr, symTableNo)

        elif Instr3AC[Instr].operator == '|':
            reg1 = getreg(Instr, Instr3AC[Instr].input1, symTableNo)
            reg2 = getreg(Instr, Instr3AC[Instr].input2, symTableNo)
            reg3 = getreg(Instr, Instr3AC[Instr].output, symTableNo)
            MIPScode.append('or '+reg3+','+reg1+','+reg2)
            freeReg(Instr, symTableNo)

        elif Instr3AC[Instr].operator == '&':
            reg1 = getreg(Instr, Instr3AC[Instr].input1, symTableNo)
            reg2 = getreg(Instr, Instr3AC[Instr].input2, symTableNo)
            reg3 = getreg(Instr, Instr3AC[Instr].output, symTableNo)
            MIPScode.append('and '+reg3+','+reg1+','+reg2)
            freeReg(Instr, symTableNo)

        elif Instr3AC[Instr].operator == '^':
            reg1 = getreg(Instr, Instr3AC[Instr].input1, symTableNo)
            reg2 = getreg(Instr, Instr3AC[Instr].input2, symTableNo)
            reg3 = getreg(Instr, Instr3AC[Instr].output, symTableNo)
            MIPScode.append('xor '+reg3+','+reg1+','+reg2)
            freeReg(Instr, symTableNo)

        elif Instr3AC[Instr].operator == '<<':
            reg1 = getreg(Instr, Instr3AC[Instr].input1, symTableNo)
            reg2 = getreg(Instr, Instr3AC[Instr].input2, symTableNo)
            reg3 = getreg(Instr, Instr3AC[Instr].output, symTableNo)
            MIPScode.append('sllv '+reg3+','+reg1+','+reg2)
            freeReg(Instr, symTableNo)

        elif Instr3AC[Instr].operator == '>>':
            reg1 = getreg(Instr, Instr3AC[Instr].input1, symTableNo)
            reg2 = getreg(Instr, Instr3AC[Instr].input2, symTableNo)
            reg3 = getreg(Instr, Instr3AC[Instr].output, symTableNo)
            MIPScode.append('srav '+reg3+','+reg1+','+reg2)
            freeReg(Instr, symTableNo)

        elif Instr3AC[Instr].operator == '~|':
            reg1 = getreg(Instr, Instr3AC[Instr].input1, symTableNo)
            reg2 = getreg(Instr, Instr3AC[Instr].input2, symTableNo)
            reg3 = getreg(Instr, Instr3AC[Instr].output, symTableNo)
            MIPScode.append('nor '+reg3+','+reg1+','+reg2)
            freeReg(Instr, symTableNo)

        elif Instr3AC[Instr].operator == '>>>':
            reg1 = getreg(Instr, Instr3AC[Instr].input1, symTableNo)
            reg2 = getreg(Instr, Instr3AC[Instr].input2, symTableNo)
            reg3 = getreg(Instr, Instr3AC[Instr].output, symTableNo)
            MIPScode.append('srlv '+reg3+','+reg1+','+reg2)
            freeReg(Instr, symTableNo)
