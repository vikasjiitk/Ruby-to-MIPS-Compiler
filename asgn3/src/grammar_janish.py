def p_arg(p):
	'''	ARG	: LHS EQUAL ARG			
			| LHS OP_ASGN ARG
			| ARG DOUBLEDOT ARG
			| ARG TRIPLEDOT ARG
			| ARG PLUS ARG
			| ARG MINUS ARG
			| ARG MULTIPLY ARG
			| ARG DIV ARG
			| ARG MOD ARG
			| ARG DOUBLESTAR ARG
			| PLUS ARG
			| MINUS ARG
			| ARG PIPE ARG
			| ARG BITXOR ARG
			| ARG BITAND ARG
			| ARG IFF ARG
			| ARG GREATER ARG
			| ARG GREATEREQUAL ARG
			| ARG LESS ARG
			| ARG LESSEQUAL ARG
			| ARG DOUBLEEQUAL ARG
			| ARG TRIPLEEQUAL ARG
			| ARG NOTEQUAL ARG			
			| BITNOT ARG
			| BITCOMP ARG
			| ARG SHIFTL ARG
			| ARG SHIFTR ARG
			| ARG LOGICALAND ARG
			| ARG LOGICALOR ARG
			| KEYWORD_definedQ ARG
			| PRIMARY '''
	i = 1
	p[0] = ('ARG',)
	while(i < len(p)):						
		p[0] = p[0] + (p[i],)		
		i = i+1

def p_primary(p):
	'''PRIMARY	: OPEN_PAREN COMPSTMT CLOSE_PAREN
				| LITERAL
				| VARIABLE
				| PRIMARY DOUBLE_COLON IDENTIFIER
				| DOUBLE_COLON IDENTIFIER
				| PRIMARY OPEN_BRACKET [ARGS] CLOSE_BRACKET
				| OPEN_BRACKET [ARGS [COMMA]] CLOSE_BRACKET
				| BLOCK_BEGIN [(ARGS|ASSOCS) [COMMA]] BLOCK_END
				| KEYWORD_return [OPEN_PAREN [CALL_ARGS] CLOSE_PAREN]
				| KEYWORD_yield [OPEN_PAREN [CALL_ARGS] CLOSE_PAREN]
				| KEYWORD_definedQ OPEN_PAREN ARG CLOSE_PAREN
		        | FUNCTION
				| FUNCTION BLOCK_BEGIN [PIPE [BLOCK_VAR] PIPE] COMPSTMT BLOCK_END
				| KEYWORD_if EXPR THEN
				  COMPSTMT
				  (KEYWORD_elsif EXPR THEN COMPSTMT)*
				  [KEYWORD_else COMPSTMT]
				  KEYWORD_end
				| KEYWORD_unless EXPR THEN
				  COMPSTMT
				  [KEYWORD_else COMPSTMT]
				  KEYWORD_end
				| KEYWORD_while EXPR DO COMPSTMT KEYWORD_end
				| KEYWORD_until EXPR DO COMPSTMT KEYWORD_end
				| KEYWORD_case COMPSTMT
				  (KEYWORD_when WHEN_ARGS THEN COMPSTMT)+
				  [KEYWORD_else COMPSTMT]
				  KEYWORD_end
				| KEYWORD_for BLOCK_VAR KEYWORD_in EXPR DO
				  COMPSTMT
				  KEYWORD_end
				| KEYWORD_begin
				  COMPSTMT
				  [KEYWORD_rescue [ARGS] DO COMPSTMT]+
				  [KEYWORD_else COMPSTMT]
				  [KEYWORD_ensure COMPSTMT]
				  KEYWORD_end
				| KEYWORD_class IDENTIFIER [LESS IDENTIFIER]
				  COMPSTMT
				  KEYWORD_end
				| KEYWORD_module IDENTIFIER
				  COMPSTMT
				  KEYWORD_end
				| KEYWORD_def FNAME ARGDECL
				  COMPSTMT
				  KEYWORD_end
				| KEYWORD_def SINGLETON (DOT|DOUBLE_COLON) FNAME ARGDECL
				  COMPSTMT
				  KEYWORD_end '''
	i = 1
	p[0] = ('ARG',)
	while(i < len(p)):						
		p[0] = p[0] + (p[i],)		
		i = i+1


def printRightDeriv(tree):
	allLeaves = True
	for i in range(1,len(tree)):
		if(len(tree[i]) == 1):
			print tree[i]
		else:
			allLeaves = False
			printRightDeriv(tree[i])

	if(allLeaves == True):




