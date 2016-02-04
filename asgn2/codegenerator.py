def initializeReg:
    RegAvail = ['$t0','$t1','$t2','$t3','$t4','$t5','$t6','$t7','$s0','$s1','$s2','$s3','$s4','$s5','$s6','$s7']
    RegConstant =[]
    for i in variables:
        AddDescriptor[i] = ['memory']

def dumpReg:
    for reg in RegDescriptor:
        MIPScode.append('sw '+reg+','+RegDescriptor[reg])

def freeReg(Instr, symTableNo):
    RegAvail.append(RegConstant)
    RegConstant =[]
    InstrVAR = [Instr3AC[Instr].input1,Instr3AC[Instr].input2, Instr3AC[Instr].output]
    for var in InstrVAR:
        if var in RegDescriptor:
            if symtables[symTableNo][var][0] == DEAD:
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
    if (var in RegDescriptor):
        return RegDescriptor[var]
    if RegAvail: # there is a register in RegAvail
        reg = RegAvail.pop()
        if(var.isdigit() == False)   # var passed is not a constant value
            MIPScode.append('lw '+reg+','+var)
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
        if(var.isdigit() == False)   # var passed is not a constant value
            MIPScode.append('lw '+reg+','+var)
            RegDescriptor[var] = reg
            AddDescriptor[var].append('register')
        else:
            MIPScode.append('addi '+reg+',$0,'+var)
            RegConstant.append(reg)
        return reg

def code_gen(initial, final):
    for Instr in range(initial,final+1):
        symTableNo = Instr - initial + 1
        if Instr3AC[Instr].instrType == 'ifgoto':
            reg1 = getreg(Instr, Instr3AC[Instr].input1, symTableNo)            
            if Instr3AC[Instr].operator in ["ble","blt","bge","bgt","beq","bne"]:
                reg2 = getreg(Instr, Instr3AC[Instr].input2, symTableNo)
                MIPScode.append('L'+Instr3AC[Instr].operator + reg1+','+reg2 + ',' +'L' + str(Instr3AC[Instr].lineNo))
            else :
                MIPScode.append('bgtz ' + reg1 + ','+'L' + str(Instr3AC[Instr].lineNo))
            freeReg(Instr, symTableNo) 

        elif Instr3AC[Instr].instrType == 'FunctionCall':
            MIPScode.append('jal '+ Instr3AC[Instr].flabel) 
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
                MIPScode.append('move $v1, '+ reg1)
            MIPScode.append('jr $ra')
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
            if (Instr3AC[Instr].input1.isdigit() == True):
                reg1 = getreg(Instr, Instr3AC[Instr].output, symTableNo)
                MIPScode.append('addi '+reg1+',$0,'+Instr3AC[Instr].input1)
            else:
                reg1 = getreg(Instr, Instr3AC[Instr].input1)
                reg3 = getreg(Instr, Instr3AC[Instr].ouput)
                MIPScode.append('move '+reg3+','+reg1)
            freeReg(Instr, symTableNo)

# def getreg(instrNo, symTableNo):
#     if Instr3AC[i].instrType in ['Arithmetic']:
#         y = Instr3AC[i].input1
#         if (('register' in AddDescriptor[y]) and (symtables[symTableNo][y] == DEAD):
#                 for Regno in range(NumRegister):
#                     if y == RegDescriptor[Regno]:
#                         return Regno
#
#         for Regno in range(NumRegister):
#             if(RegDescriptor[Regno] == ''):
#                 return Regno
#
#         x = Instr3AC[i].output
#         if( symtables[symTableNo][x] == LIVE):
#             farthestNextUse = 0
#             for Var in symtables[symTableNo]:
#                 if (symtables[symTableNo][Var][2] > farthestNextUse):
#                     farthestVar = Var
#                     farthestNextUse = symtables[symTableNo][Var][2]
#             for Regno in range(NumRegister):
#                 if farthestVar == RegDescriptor[Regno]:
#                     break
#             print 'move %s t%d' % (farthestVar, Regno)                          # moving contents of register to memory
#             AddDescriptor[farthestVar] = ['memory']
#             RegDescriptor[farthestVar] = ''
#             return Regno
#
#         return x
#
#     if Instr3AC[i].instrType == 'Assignment':                                   ## x = y
#         y = Instr3AC[i].input1
#         x = Instr3AC[i].output
#         if y.isdigit() == False and y != '':
#             if (('register' in AddDescriptor[y]) and (symtables[symTableNo][y] == DEAD):               ## x =y
#                 for Regno in range(NumRegister):
#                     if y == RegDescriptor[Regno]:
#                         return Regno
#             for Regno in range(NumRegister):
#                 if(RegDescriptor[Regno] == ''):
#                     return Regno
#             if( symtables[symTableNo][x] == LIVE):
#                 farthestNextUse = 0
#                 for Var in symtables[symTableNo]:
#                     if (symtables[symTableNo][Var][2] > farthestNextUse):
#                         farthestVar = Var
#                         farthestNextUse = symtables[symTableNo][Var][2]
#                 for Regno in range(NumRegister):
#                     if farthestVar == RegDescriptor[Regno]:
#                         break
#                 print 'move %s t%d' % (farthestVar, Regno)                                      # moving contents of register to memory
#                 AddDescriptor[farthestVar] = ['memory']
#                 RegDescriptor[farthestVar] = ''
#                 return Regno
#         else:                                                                                           ### x =2
#             if (('register' in AddDescriptor[x]) and (symtables[symTableNo][x] == DEAD):
#                 for Regno in range(NumRegister):
#                     if x == RegDescriptor[Regno]:
#                         return Regno
#                 for Regno in range(NumRegister):
#                     if(RegDescriptor[Regno] == ''):
#                         return Regno
#
#                 if( symtables[symTableNo][x] == LIVE):
#                 farthestNextUse = 0
#                 for Var in symtables[symTableNo]:
#                     if (symtables[symTableNo][Var][2] > farthestNextUse):
#                         farthestVar = Var
#                         farthestNextUse = symtables[symTableNo][Var][2]
#                 for Regno in range(NumRegister):
#                     if farthestVar == RegDescriptor[Regno]:
#                         break
#                 print 'move %s t%d' % (farthestVar, Regno)                          # moving contents of register to memory
#                 AddDescriptor[farthestVar] = ['memory']
#                 RegDescriptor[farthestVar] = ''
#                 return Regno

#CODE GENERATION ALGORITHM
# def code_gen(initial,final):
#     for i in range(initial,final+1):
#         if Instr3AC[i].instrType in ['Arithmetic']:
#             x = Instr3AC[i].output
#             y = Instr3AC[i].input1
#             L = getreg(i,i-initial+1)
#
#             if (RegDescriptor[L] != y):
#                 if ('register' in AddDescriptor[y]):
#                     for Regno in range(NumRegister):
#                         if (y == RegDescriptor[Regno]):
#                             break
#                     Y = Regno
#                     print 'move $t%d, $t%d',%(L,Y)
#                 else:
#                     Y = y
#                     print 'lw $t%d, %s($zero)',%(L,Y)
#             z = Instr3AC[i].input2
#             op = giveOperator(Instr3AC[i].operator)
#             if(op == 0):
#                 raise Exception("operator not correct")
#             if ('register' in AddDescriptor[z]):
#                 for Regno in range(NumRegister):
#                     if (z == RegDescriptor[Regno]):
#                         break
#                 Z = Regno
#                 print '%s $t%d $t%d',%(op,L,Z)
#             else:
#                 Z = z
#                 print 'lw $t%d, '
#                 print '%s t%d %s',%(op,L,Z)
#             RegDescriptor[L] = x
#             AddDescriptor[x].append('register')
#             for Regno in range(NumRegister):
#                 if(Regno != L) and RegDescriptor[Regno] == x:
#                     RegDescriptor[Regno] = ''
#             symTableNo = i-initial+1
#             if (symtables[symTableNo][y][2] == 0):
#                 for Regno in range(NumRegister):
#                     if(RegDescriptor[Regno]==y):
#                         RegDescriptor[Regno] = ''
#             if (symtables[symTableNo][z][2] == 0):
#                 for Regno in range(NumRegister):
#                     if(RegDescriptor[Regno]==z):
#                         RegDescriptor[Regno] = ''
#
#         elif Instr3AC[i].instrType in ['Assignment']:
#         	x = Instr3AC[i].output
#             y = Instr3AC[i].input1
#             L = getreg(i,i-initial+1)
#             if(y.isdigit()==False):
