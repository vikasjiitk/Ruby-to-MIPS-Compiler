#!/usr/bin/python
import sys
import codegenerator as cg
import TAC as tac
import symtables as st

def fillDataSection(variables):

    cg.MIPSDatacode.append('.data')
    for var in variables:
        cg.MIPSDatacode.append(var+': .word 0')
    cg.MIPSDatacode.append('.text')


filename = sys.argv[1]
f = open(filename,'r')
# getInstrSet fills cg.Instr3AC[] structure and also finds cg.leaders in the 3AC instruction set
NumInstr = tac.getInstrSet(f)
cg.variables = tac.getVariables(NumInstr)

fillDataSection(cg.variables)

for blockNum in range(len(cg.leaders)-1):
    initial = cg.leaders[blockNum]
    final = cg.leaders[blockNum+1] - 1
    blockLength = final - initial + 1
    # Building blockLength number of symbol tables (one for each program point)
    cg.symtables = st.getsymtables(initial, final, blockLength)

    ## Backward scanning and filling symbol table for each program point
    cg.symtables = st.fillsymtables(cg.symtables,initial,final,blockLength)

    cg.initializeReg()
    cg.code_gen(initial,final)
    cg.dumpReg()

for i in range(0,len(cg.MIPSDatacode)):
    print cg.MIPSDatacode[i]

for i in range(0,len(cg.MIPScode)):
    print cg.MIPScode[i]
