class Symtable:
    
    def __init__(self):
        self.vardict = {}
        self.funcdict = {}

    def varlookup(var):
        if var in self.vardict.keys():
            return self.vardict[var]

    def funclookup(func):
        if func in self.funcdict.keys():
            return self.vardict[func]

    def varinsert(var, lis):
        self.vardict[var] = lis

    def funcinsert(var, lis):
        self.vardict[func] = lis
