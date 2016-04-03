class TAC:
    def __init__(self):
        self.code = []

    def emit(self, instrType, lis):
        if instrType == 'Assignment':   # lis = [des, src]
            self.code.append('=,'+str(lis[0])+','+str(lis[1]))
        if instrType == 'Arithmetic' or instrType == 'logical': # lis = [op, des, src1, src2]
            self.code.append(str(lis[0])+','+str(lis[1])+','+str(lis[2])+','+str(lis[3]))
        if instrType == 'print':  # lis = [src]
            self.code.append('print,'+str(lis[0]))
        if instrType == 'goto': # lis = [label]
            self.code.append('goto,'+str(lis[0]))
        if instrType == 'ifgoto': # lis = [rel, src1,src2, lablel]
            self.code.append('ifgoto,'+str(lis[0])+ ',' + str(lis[1])+','+str(lis[2])+','+str(lis[3]))
        if instrType == 'label': # lis = [label]
            self.code.append('label,'+str(lis[0]))
        if instrType == 'return': # lis = [src]
            self.code.append('return,'+str(lis[0]))
        if instrType == 'scan':  # lis = [src]
            self.code.append('scan,'+str(lis[0]))
        if instrType == 'exit':
            self.code.append('exit')

    def printTAC(self):
        for instr in self.code:
            print instr


        #FUNCTION
