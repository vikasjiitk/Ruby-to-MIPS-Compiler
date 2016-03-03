


def p_when_args(p):
	'''WHEN_ARGS	: ARGS [COMMA MULTIPLY ARG]
					| MULTIPLY ARG'''
	if (len(p) == 5):
		p[0] = ('WHEN_ARGS',p[2],p[1],p[3])
	elif(len(p)==3):
		p[0] = ('WHEN_ARGS',p[1],p[2] )	


def p_then(p):
	'''THEN		: TERM
				| KEYWORD_then
				| TERM KEYWORD_then'''
	if(len(p)==2)
		p[0] = ('THEN',p[1])
	elif (len(p) ==3)
		p[0] = ('THEN', p[1],p[2])	 			

def p_do(p):
	'''DO		: TERM
				| KEYWORD_do
				| TERM KEYWORD_do'''
	if(len(p)==2)
		p[0] = ('DO',p[1])
	elif (len(p) ==3)
		p[0] = ('DO', p[1],p[2])			

def p_block_var(p):
	'''BLOCK_VAR	: LHS
					| MLHS'''
	p[0] = ('BLOCK_VAR',p[1])				


def p_mlhs(p):
	'''MLHS		: MLHS_ITEM COMMA [MLHS_ITEM (COMMA MLHS_ITEM)*] [MULTIPLY [LHS]]
                | MULTIPLY LHS'''
    p[0] = ('MLHS',)
    int i=1;
    while (i<len(p))
    	p[0] += (p[i],)         

def p_mlhs_item(p):
	'''MLHS_ITEM	: LHS
					| OPEN_PAREN MLHS CLOSE_PAREN'''
    p[0] = ('MLHS_ITEM',)
    int i=1;
    while (i<len(p))
    	p[0] += (p[i],)         


def p_lhs(p):
	'''LHS		: VARIABLE
				| PRIMARY OPEN_BRACKET [ARGS] CLOSE_BRACKET
				| PRIMARY DOT IDENTIFIER'''
    p[0] = ('LHS',)
    int i=1;
    while (i<len(p))
    	p[0] += (p[i],)         


def p_mrhs(p):
	'''MRHS		: ARGS [COMMA MULTIPLY ARG]
				| MULTIPLY ARG'''
    p[0] = ('MRHS',)
    int i=1;
    while (i<len(p))
    	p[0] += (p[i],)         


def p_call_args(p):
	'''CALL_ARGS	: ARGS
					| ARGS [COMMA ASSOCS] [COMMA MULTIPLY ARG] [COMMA BITAND ARG]
					| ASSOCS [COMMA MULTIPLY ARG] [COMMA BITAND ARG]
					| MULTIPLY ARG [COMMA BITAND ARG]
					| BITAND ARG
					| COMMAND'''
    p[0] = ('CALL_ARGS',)
    int i=1;
    while (i<len(p))
    	p[0] += (p[i],)         


def p_args(p):
	'''ARGS 		: ARG (COMMA ARG)*'''
	p[0] = ('ARGS',)
    int i=1;
    while (i<len(p))
    	p[0] += (p[i],)         
