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
            RegDescriptor[farthestVar] = ''
            return Regno

        return x

    if Instr3AC[i].instrType == 'Assignment':                                   ## x = y
        y = Instr3AC[i].input1
        x = Instr3AC[i].output
        if y.isdigit() == False and y != '':
            if (('register' in AddDescriptor[y]) and (symtables[symTableNo][y] == DEAD):               ## x =y
                for Regno in range(NumRegister):
                    if y == RegDescriptor[Regno]:
                        return Regno
            for Regno in range(NumRegister):
                if(RegDescriptor[Regno] == ''):
                    return Regno
            if( symtables[symTableNo][x] == LIVE):
                farthestNextUse = 0
                for Var in symtables[symTableNo]:
                    if (symtables[symTableNo][Var][2] > farthestNextUse):
                        farthestVar = Var
                        farthestNextUse = symtables[symTableNo][Var][2]
                for Regno in range(NumRegister):
                    if farthestVar == RegDescriptor[Regno]:
                        break
                print 'move %s t%d' % (farthestVar, Regno)                                      # moving contents of register to memory
                AddDescriptor[farthestVar] = ['memory']
                RegDescriptor[farthestVar] = ''
                return Regno
        else:                                                                                           ### x =2                                             
            if (('register' in AddDescriptor[x]) and (symtables[symTableNo][x] == DEAD):
                for Regno in range(NumRegister):
                    if x == RegDescriptor[Regno]:
                        return Regno
                for Regno in range(NumRegister):
                    if(RegDescriptor[Regno] == ''):
                        return Regno

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
                RegDescriptor[farthestVar] = ''
                return Regno



#CODE GENERATION ALGORITHM
def code_gen(initial,final):
    for i in range(initial,final+1):
        if Instr3AC[i].instrType in ['Arithmetic']:
            L = getreg(i,i-initial+1)