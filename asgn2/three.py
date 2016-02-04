f = open('input.txt','r')
MIPScode = []
Instr3AC = []
i=0
Dead = 0
Live = 1
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
	Instr3AC[i].instrType = "Assignment"
	Instr3AC[i].output = words[2]
	Instr3AC[i].input1 = words[3]
#	return Instr3AC.output,Instr3AC.input1
def Arithmetic(i,words):
	Instr3AC[i].instrType = "Arithmetic"
	Instr3AC[i].output = words[2]
	Instr3AC[i].input1 = words[3]
	Instr3AC[i].input2 = words[4]
#	return Instr3AC.output,Instr3AC.input1, Instr3AC.input2
def Ifgoto(i,words):
	Instr3AC[i].instrType = "Ifgoto"
	if words[2] in ["ble","blt","bge","bgt","beq","bne"]:
		Instr3AC[i].operator = words[2]
		Instr3AC[i].input1 = words[3]
		Instr3AC[i].input2 = words[4]
	else:
		Instr3AC[i].input1 = words[2]
	Instr3AC[i].target = words[-1]
def Function(i,words):
	Instr3AC[i].instrType = "FunctionCall"
	Instr3AC[i].flabel = words[2]
def Return(i,words):
	Instr3AC[i].instrType = "return"
	if len(words) == 3:
		Instr3AC[i].input1 = words[2]
def Label(i,words):
	Instr3AC[i].instrType = "label"
	Instr3AC[i].flabel = words[2]
def Print(i,words):
	Instr3AC[i].instrType  = "print"
	Instr3AC[i].input1 = words[2]

leaders = [0]
for line in f:
	line = line[:-1]
	words = line.split(',')
	Instr3AC.append(threeAddCode())
	Instr3AC[i].lineNo = int(words[0])
	Instr3AC[i].operator = words[1]
	print words
	if words[1] == '=':
		Equal(i,words)
	elif words[1] in ['+','-','/','*','%']:
		Arithmetic(i,words)
	elif words[1] == 'ifgoto':
		leaders.append(Instr3AC[i].lineNo + 1)
		leaders.append(int(words[-1]))
		Ifgoto(i,words)
	elif words[1] == 'call':
		leaders.append(Instr3AC[i].lineNo + 1)
		Function(i, words)
	elif words[1] == 'label':
		leaders.append(Instr3AC[i].lineNo)
		Label(i,words)
	elif words[1] == 'ret':
		Return(i,words)
	elif words[1] == 'print':
		Print(i,words)
	i = i+1
leaders.append(i)
# print leaders
leaders = sorted(set(leaders))
NumInstr = i
# Building blockLength number of symbol tables (one for each program point)

variables = []
for i in range(NumInstr):
	if (Instr3AC[i].input1.isdigit() == False and Instr3AC[i].input1!= ""):
		variables.append(Instr3AC[i].input1)
	if (Instr3AC[i].input2.isdigit() == False and Instr3AC[i].input2!= ""):
		variables.append(Instr3AC[i].input2)
	if (Instr3AC[i].output.isdigit() == False and Instr3AC[i].output!= ""):
		variables.append(Instr3AC[i].output)

variables = set(variables)
MIPScode.append('.data')
for var in variables:
	MIPScode.append(var+': .word 0')
print MIPScode
for blockNum in range(len(leaders)-1):
	initial = leaders[blockNum]
	final = leaders[blockNum+1] - 1
	blockLength = final - initial + 1
	symtables = [dict() for x in range(blockLength)]
	for blockLine in range(initial,final+1):

		if (Instr3AC[blockLine].input1.isdigit() == False and Instr3AC[blockLine].input1!= ""):
			if Instr3AC[blockLine].input1 not in symtables[0]:
				for k in range(blockLength):
					symtables[k][Instr3AC[blockLine].input1] = [Dead, 0]
		if (Instr3AC[blockLine].input2.isdigit() == False and Instr3AC[blockLine].input2!= ""):
			if Instr3AC[blockLine].input2 not in symtables[0]:
				for k in range(blockLength):
					symtables[k][Instr3AC[blockLine].input2] = [Dead, 0]
		if Instr3AC[blockLine].output not in symtables[0] and Instr3AC[blockLine].output!="":
				for k in range(blockLength):
					symtables[k][Instr3AC[blockLine].output] = [Dead, 0]
	# print 'SYMBOL TABLE: '
	# print symtables
	#Backward scanning and filling symbol table for each program point
	scan = blockLength-1
	for blockLine in range(final, initial -1 , -1):
		if blockLine!=final:
			symtables[scan]=symtables[scan+1].copy()								#copying the previous filled dictionary for further changes
		if (Instr3AC[blockLine].input1.isdigit() == False and Instr3AC[blockLine].input1!= ""):
			symtables[scan][Instr3AC[blockLine].input1] = [Live, blockLine]
		if (Instr3AC[blockLine].input2.isdigit() == False and Instr3AC[blockLine].input2!= ""):
			symtables[scan][Instr3AC[blockLine].input2] = [Live, blockLine]
		if (Instr3AC[blockLine].output!= ""):
			symtables[scan][Instr3AC[blockLine].output] = [Dead, 0]
		scan = scan-1
		print 'symbol table before ' + str(blockLine)
		print symtables[blockLine-initial]

	initializeReg()
	code_gen(initial,final)
	dumpReg()


#	print symtables
