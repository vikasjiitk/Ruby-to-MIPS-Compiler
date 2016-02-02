
f = open('input.txt','r')

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
	instrType = "FunctionCall"
	Instr3AC[i].input1 = words[2]
def Return(i,words):
	instrType = "return"
	if len(words) == 3:
		Instr3AC[i].input1 = words[2]
def Label(i,words):
	instrType = "label"_

leaders = [1]
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
	i = i+1
leaders.append(i)
print leaders
leaders = sorted(set(leaders))
NumInstr = i
for blockNum in range(len(leaders)):
	initial = leaders[blockNum]	
	final = leaders[blockNum+1] - 1
	n = final - initial + 1
	symtables = [dict() for x in range(n)]
	for j in range(initial,final+1):
		if (Instr3AC[j].input1.isdigit() == False and Instr3AC[j].input1!= ""):
			if Instr3AC[j].input1 not in symtables[0]:
				for k in range(n):
					symtables[k][Instr3AC[j].input1] = [Dead, 0]
		if (Instr3AC[j].input1.isdigit() == False and Instr3AC[j].input1!= ""):
			if Instr3AC[j].input2 not in symtables[0]:
				for k in range(n):
					symtables[k][Instr3AC[j].input2] = [Dead, 0]
		if Instr3AC[j].output not in symtables[0]:
				for k in range(n):
					symtables[k][Instr3AC[j].output] = [Dead, 0]
	#Backward scanning
	scan = n-1
	for j in range(final, initial -1 , -1):
		if j!=final:
			symtables[scan]=symtables[scan+1].copy()								#copying the previous filled dictionary for further changes 
		if (Instr3AC[j].input1.isdigit() == False and Instr3AC[j].input1!= ""):
			symtables[scan][Instr3AC[j].input1] = [Live, j]
		if (Instr3AC[j].input2.isdigit() == False and Instr3AC[j].input2!= ""):
			symtables[scan][Instr3AC[j].input2] = [Live, j]
		if (Instr3AC[j].output!= ""):
			symtables[scan][Instr3AC[j].output] = [Dead, 0]			
		scan = scan-1


print leaders
print Instr3AC[1].lineNo
print Instr3AC[1].operator
print Instr3AC[1].input1
print Instr3AC[1].input2
print Instr3AC[1].output