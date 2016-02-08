import codegenerator as cg

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
