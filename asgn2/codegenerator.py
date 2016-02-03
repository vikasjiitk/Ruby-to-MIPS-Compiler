NumRegister = 8
RegDescriptor = ['' for x in range(NumRegister)]
# print RegDescriptor
variables = []
for i in range(NumInstr):
    variables.append(Instr3AC[i].input1)
    variables.append(Instr3AC[i].input2)
    variables.append(Instr3AC[i].output)

variables = set(variables)
AddDescriptor = {}
for i in variables:
    AddDescriptor[i] = ['memory']

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
def getreg(instrNo, symTableNo):
    if Instr3AC[i].instrType in ['Arithmetic']:
        y = Instr3AC[i].input1
        if (('register' in AddDescriptor[y]) and (symtables[symTableNo][y] == DEAD):
                for Regno in range(NumRegister):
                    if y == RegDescriptor[Regno]:
                        return Regno

        for Regno in range(NumRegister):
            if(RegDescriptor[Regno] == ''):
                return Regno

        x = Instr3AC[i].output
        if( symtables[symTableNo][x] == LIVE):
            farthestNextUse = 0
            for Var in symtables[symTableNo]:
                if (symtables[symTableNo][Var][2] > farthestNextUse):
                    farthestVar = Var
                    farthestNextUse = symtables[symTableNo][Var][2]
            for Regno in range(NumRegister):
                if farthestVar == RegDescriptor[Regno]:
                    break
            print 'move %s t%d' % (farthestVar, Regno)                          # moving contents of register to memory
            AddDescriptor[farthestVar] = ['memory']
            return Regno

        return x

#CODE GENERATION ALGORITHM
def code_gen(initial,final):
    for i in range(initial,final+1):
        if Instr3AC[i].instrType in ['Arithmetic']:
            x = Instr3AC[i].output
            y = Instr3AC[i].input1
            L = getreg(i,i-initial+1)

            if (RegDescriptor[L] != y):
                if ('register' in AddDescriptor[y]):
                    for Regno in range(NumRegister):
                        if (y == RegDescriptor[Regno]):
                            break
                    Y = Regno
                    print 'move t%d t%d',%(L,Y)
                else:
                    Y = y
                    print 'move t%d %s',%(L,Y)
            z = Instr3AC[i].input2
            op = giveOperator(Instr3AC[i].operator)
            if(op == 0):
                raise Exception("operator not correct")
            if ('register' in AddDescriptor[z]):
                for Regno in range(NumRegister):
                    if (z == RegDescriptor[Regno]):
                        break
                Z = Regno
                print '%s t%d t%d',%(op,L,Z)
            else:
                Z = z
                print '%s t%d %s',%(op,L,Z)
            RegDescriptor[L] = x
            AddDescriptor[x].append('register')
            for Regno in range(NumRegister):
                if(Regno != L) and RegDescriptor[Regno] == x:
                    RegDescriptor[Regno] = ''
            symTableNo = i-initial+1
            if (symtables[symTableNo][y][2] == 0):
                for Regno in range(NumRegister):
                    if(RegDescriptor[Regno]==y):
                        RegDescriptor[Regno] = ''
            if (symtables[symTableNo][z][2] == 0):
                for Regno in range(NumRegister):
                    if(RegDescriptor[Regno]==z):
                        RegDescriptor[Regno] = ''
