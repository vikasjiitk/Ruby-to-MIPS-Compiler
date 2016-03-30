class TAC:
    def __init__(self):
        self.code = []

    def emit(instrType, lis):
        if instrType == 'Assignment':   # lis = [des, src]
            self.code.append('=,')
