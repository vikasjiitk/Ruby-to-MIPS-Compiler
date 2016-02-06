import sys
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
def getsymtables(initialInstr, finalInstr, blockLength):

    cg.symtables = [dict() for x in range(blockLength+1)]
    for blockLine in range(initialInstr,finalInstr+1):
        if (cg.Instr3AC[blockLine].input1.isdigit() == False and cg.Instr3AC[blockLine].input1!= ""):
            if cg.Instr3AC[blockLine].input1 not in cg.symtables[0]:
                for k in range(blockLength+1):
                    cg.symtables[k][cg.Instr3AC[blockLine].input1] = [cg.Dead, cg.Infinite]
        if (cg.Instr3AC[blockLine].input2.isdigit() == False and cg.Instr3AC[blockLine].input2!= ""):
            if cg.Instr3AC[blockLine].input2 not in cg.symtables[0]:
                for k in range(blockLength+1):
                    cg.symtables[k][cg.Instr3AC[blockLine].input2] = [cg.Dead, cg.Infinite]
        if cg.Instr3AC[blockLine].output not in cg.symtables[0] and cg.Instr3AC[blockLine].output!="":
                for k in range(blockLength+1):
                    cg.symtables[k][cg.Instr3AC[blockLine].output] = [cg.Dead, cg.Infinite]
    return cg.symtables

def fillsymtables(symtables,initialInstr,finalInstr,blockLength):

    scan = blockLength-1
    for blockLine in range(finalInstr, initialInstr -1 , -1):
        if blockLine!=finalInstr:
            symtables[scan]=cg.symtables[scan+1].copy()      #copying the previous filled dictionary for further changes
        if (cg.Instr3AC[blockLine].output!= ""):
            symtables[scan][cg.Instr3AC[blockLine].output] = [cg.Dead, 0]
        if (cg.Instr3AC[blockLine].input1.isdigit() == False and cg.Instr3AC[blockLine].input1!= ""):
            symtables[scan][cg.Instr3AC[blockLine].input1] = [cg.Live, blockLine]
        if (cg.Instr3AC[blockLine].input2.isdigit() == False and cg.Instr3AC[blockLine].input2!= ""):
            symtables[scan][cg.Instr3AC[blockLine].input2] = [cg.Live, blockLine]

        scan = scan-1

    return symtables

def getVariables(NumInstr):

    cg.variables = []
    for i in range(NumInstr):
        if (cg.Instr3AC[i].input1.isdigit() == False and cg.Instr3AC[i].input1!= ""):
            cg.variables.append(cg.Instr3AC[i].input1)
        if (cg.Instr3AC[i].input2.isdigit() == False and cg.Instr3AC[i].input2!= ""):
            cg.variables.append(cg.Instr3AC[i].input2)
        if (cg.Instr3AC[i].output.isdigit() == False and cg.Instr3AC[i].output!= ""):
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
        elif words[1] in ['+','-','/','*','%']:
            Arithmetic(cg.Instr,words)
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
        if(cg.Instr3AC[cg.Instr].input1.isdigit() == False and cg.Instr3AC[cg.Instr].input1.isdigit() != "" ):
            cg.Instr3AC[cg.Instr].input1 += '1'
        if(cg.Instr3AC[cg.Instr].input2.isdigit() == False and cg.Instr3AC[cg.Instr].input2.isdigit() != "" ):
            cg.Instr3AC[cg.Instr].input2 += '1'
        if(cg.Instr3AC[cg.Instr].output.isdigit() == False and cg.Instr3AC[cg.Instr].output.isdigit() != "" ):
            cg.Instr3AC[cg.Instr].output += '1'
        cg.Instr = cg.Instr+1
    cg.leaders.append(cg.Instr)
    cg.leaders = sorted(set(cg.leaders))
    return cg.Instr

def fillDataSection(variables):
    # global cg.MIPSDatacode
    cg.MIPSDatacode.append('.data')
    for var in cg.variables:
        cg.MIPSDatacode.append(var+': .word 0')
    cg.MIPSDatacode.append('.text')
filename = sys.argv[1]
f = open(filename,'r')
# getInstrSet fills cg.Instr3AC[] structure and also finds cg.leaders in the 3AC instruction set
NumInstr = getInstrSet(f)
cg.variables = getVariables(NumInstr)

fillDataSection(cg.variables)

for blockNum in range(len(cg.leaders)-1):
    initial = cg.leaders[blockNum]
    final = cg.leaders[blockNum+1] - 1
    blockLength = final - initial + 1
    # Building blockLength number of symbol tables (one for each program point)
    cg.symtables = getsymtables(initial, final, blockLength)
    # print cg.symtables
    ## Backward scanning and filling symbol table for each program point
    cg.symtables = fillsymtables(cg.symtables,initial,final,blockLength)
    # print cg.symtables
    cg.initializeReg()
    cg.code_gen(initial,final)
    cg.dumpReg()
for i in range(0,len(cg.MIPSDatacode)):
    print cg.MIPSDatacode[i]
for i in range(0,len(cg.MIPScode)):
    print cg.MIPScode[i]
