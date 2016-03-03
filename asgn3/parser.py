import ply.yacc as yacc

from lexer import tokens

def p_program(p):
	# '''program		: top_compstmt
	# '''
	'''program		: top_compstmt
	'''
	i = 1
	p[0] = ['program']
	while(i < len(p)):
		p[0].append(p[i])
		i = i+1

def p_top_compstmt(p):
	'''top_compstmt	: top_stmts opt_terms

	'''
	i = 1
	p[0] = ['top_compstmt']
	while(i < len(p)):
		p[0].append(p[i])
		i = i+1

def p_top_stmts(p):
	'''top_stmts	: none
		| top_stmt
		| top_stmts terms top_stmt
	'''
	i = 1
	p[0] = ['top_stmts']
	while(i < len(p)):
		p[0].append(p[i])
		i = i+1

def p_top_stmt(p):
	'''top_stmt	: stmt
				| KEYWORD_if expr3 opt_then top_compstmt elsif_tail opt_else_stmt KEYWORD_end
				| KEYWORD_while expr3 opt_do top_compstmt KEYWORD_end
	'''
    		# | KEYWORD_BEGIN BLOCK_BEGIN top_compstmt BLOCK_END
	i = 1
	p[0] = ['top_stmt']
	while(i < len(p)):
		p[0].append(p[i])
		i = i+1

def p_stmt(p):
	# '''stmt :   expr
	# 	    | matched_stmt
	# 		| unmatched_stmt
	# '''
	'''stmt :   expr
	'''
	i = 1
	p[0] = ['stmt']
	while(i < len(p)):
		p[0].append(p[i])
		i = i+1

def p_opt_else_stmt(p):
	'''opt_else_stmt : KEYWORD_else top_compstmt
					 | none
	'''
	i = 1
	p[0] = ['opt_else_stmt']
	while(i < len(p)):
		p[0].append(p[i])
		i = i+1

# def p_matched_stmt(p):
# 	'''matched_stmt :   KEYWORD_if expr3 KEYWORD_then top_compstmt elsif_tail KEYWORD_else top_compstmt KEYWORD_end
# 	'''
# 	i = 1
# 	p[0] = ['matched_stmt']
# 	while(i < len(p)):
# 		p[0].append(p[i])
# 		i = i+1
#
# def p_if_tail(p):
# 	'''if_tail :  KEYWORD_else top_compstmt
# 				| KEYWORD_elsif expr3 KEYWORD_then top_compstmt if_tail
# 	'''
# 	i = 1
# 	p[0] = ['if_tail']
# 	while(i < len(p)):
# 		p[0].append(p[i])
# 		i = i+1
#
def p_elsif_tail(p):
	'''elsif_tail :  none
				| KEYWORD_elsif expr3 opt_then top_compstmt elsif_tail
	'''
	i = 1
	p[0] = ['elsif_tail']
	while(i < len(p)):
		p[0].append(p[i])
		i = i+1

def p_opt_then(p):
	'''opt_then : KEYWORD_then
				| none
	'''
	i=1
	p[0] = ['opt_then']
	while(i < len(p)):
		p[0].append(p[i])
		i = i+1

def p_opt_do(p):
	'''opt_do : KEYWORD_do
				| none
	'''
	i=1
	p[0] = ['opt_do']
	while(i < len(p)):
		p[0].append(p[i])
		i = i+1
#
#
# def p_unmatched_stmt(p):
# 	'''unmatched_stmt :   KEYWORD_if expr3 KEYWORD_then top_compstmt elsif_tail KEYWORD_end
# 					  | KEYWORD_if expr3 KEYWORD_then matched_stmt KEYWORD_else unmatched_stmt
# 	'''
# 	i = 1
# 	p[0] = ['unmatched_stmt']
# 	while(i < len(p)):
# 		p[0].append(p[i])
# 		i = i+1


# def p_opt_else(p):
# 	'''opt_else :
# 	'''
# 	i = 1
# 	p[0] = ['opt_else']
# 	while(i < len(p)):
# 		p[0].append(p[i])
# 		i = i+1

def p_cond_while(p):
	'''
	'''

def p_expr(p):
	'''expr :   mlhs EQUAL mrhs
	'''
	i = 1
	p[0] = ['expr']
	while(i < len(p)):
		p[0].append(p[i])
		i = i+1

def p_mlhs(p):
	'''mlhs : VARIABLES
			| CONSTANTS
	'''
	i = 1
	p[0] = ['mlhs']
	while(i < len(p)):
		p[0].append(p[i])
		i = i+1

# def p_mlhs_item(p):
# 	'''mlhs_item    : lhs
# 		    | OPEN_PAREN mlhs CLOSE_PAREN
# 	'''
# 	i = 1
# 	p[0] = ['mlhs_item']
# 	while(i < len(p)):
# 		p[0].append(p[i])
# 		i = i+1
#
# def lhs(p):
# 	'''lhs  : user_variable
# 	'''
# 	i = 1
# 	p[0] = ['lhs']
# 	while(i < len(p)):
# 		p[0].append(p[i])
# 		i = i+1

def p_mrhs(p):
	'''mrhs :   expr1
	'''
	i = 1
	p[0] = ['mrhs']
	while(i < len(p)):
		p[0].append(p[i])
		i = i+1

# def p_args(p):
# 	'''args :   arg
# 	'''
# 	i = 1
# 	p[0] = ['args']
# 	while(i < len(p)):
# 		p[0].append(p[i])
# 		i = i+1
#
# def p_arg(p):
# 	'''	arg	: LHS EQUAL arg
# 			| LHS OP_ASGN arg
# 			| arg DOUBLEDOT arg
# 			| arg TRIPLEDOT arg
# 			| arg PLUS arg
# 			| arg MINUS arg
# 			| arg MULTIPLY arg
# 			| arg DIV arg
# 			| arg MOD arg
# 			| arg DOUBLESTAR arg
# 			| PLUS arg
# 			| MINUS arg
# 			| arg PIPE arg
# 			| arg BITXOR arg
# 			| arg BITAND arg
# 			| arg IFF arg
# 			| arg GREATER arg
# 			| arg GREATEREQUAL arg
# 			| arg LESS arg
# 			| arg LESSEQUAL arg
# 			| arg DOUBLEEQUAL arg
# 			| arg TRIPLEEQUAL arg
# 			| arg NOTEQUAL arg
# 			| BITNOT arg
# 			| BITCOMP arg
# 			| arg SHIFTL arg
# 			| arg SHIFTR arg
# 			| arg LOGICALAND arg
# 			| arg LOGICALOR arg
# 			| KEYWORD_definedQ arg
# 			| primary '''
# 	i = 1
# 	p[0] = ['arg']
# 	while(i < len(p)):
# 		p[0].append(p[i])
# 		i = i+1

def p_primary(p):
	'''primary  :   INT_CONSTANTS
		|   FLOAT_CONSTANTS
		|   STRING_CONSTANTS
		|   CHAR_CONSTANTS
		|   BOOLEAN_CONSTANTS
		|   CONSTANTS
		|   VARIABLES
	'''
	i = 1
	p[0] = ['primary']
	while(i < len(p)):
		p[0].append(p[i])
		i = i+1

def user_variable(p):
	'''user_variable	: VARIABLES
		| CONSTANTS
	'''
	i = 1
	p[0] = ['user_variable']
	while(i < len(p)):
		p[0].append(p[i])
		i = i+1

# def p_op(p):
#     '''op		: PIPE
#     		| BITXOR
#     		| BITAND
#     		| EQUAL
#     		| DOUBLEEQUAL
#     		| GREATER
#     		| GREATEREQUAL
#     		| LESS
#     		| LESSEQUAL
#     		| NOTEQUAL
#     		| SHIFTL
#     		| SHIFTR
#     		| PLUS
#     		| MINUS
#     		| MULTIPLY
#     		| DIV
#     		| MOD
#     		| DOUBLESTAR
#     		| BITNOT
#     		| BITCOMP
#     '''
# 	i = 1
# 	p[0] = ['arg']
# 	while(i < len(p)):
# 		p[0].append(p[i])
# 		i = i+1
#
# def p_resords(p):
#     '''reswords	: KEYWORD__LINE__ | KEYWORD__FILE__ | KEYWORD__ENCODING__
#     		| KEYWORD_BEGIN | KEYWORD_END
#     		| KEYWORD_alias | KEYWORD_and | KEYWORD_begin
#     		| KEYWORD_break | KEYWORD_case | KEYWORD_class | KEYWORD_def
#     		| KEYWORD_definedQ | KEYWORD_do | KEYWORD_else | KEYWORD_elsif
#     		| KEYWORD_end | KEYWORD_ensure | KEYWORD_false
#     		| KEYWORD_for | KEYWORD_in | KEYWORD_module | KEYWORD_next
#     		| KEYWORD_nil | KEYWORD_not | KEYWORD_or | KEYWORD_redo
#     		| KEYWORD_rescue | KEYWORD_retry | KEYWORD_return | KEYWORD_self
#     		| KEYWORD_super | KEYWORD_then | KEYWORD_true | KEYWORD_undef
#     		| KEYWORD_when | KEYWORD_yield | KEYWORD_if | KEYWORD_unless
#     		| KEYWORD_while | KEYWORD_until
#     '''


def p_expr1(p):
	'''expr1 : expr3 QUESTION_MARK expr2 COLON expr2
			 | expr2
	'''
	i = 1
	p[0] = ['expr1']
	while(i < len(p)):
		p[0].append(p[i])
		i = i+1

def p_expr2(p):
	'''expr2 : expr7 DOUBLEDOT expr7
			 | expr7 TRIPLEDOT expr7
			 | expr3
	'''
	i = 1
	p[0] = ['expr2']
	while(i < len(p)):
		p[0].append(p[i])
		i = i+1

def p_expr3(p):
	'''expr3 : expr3 LOGICALOR expr4
			 | expr4
	'''
	i = 1
	p[0] = ['expr3']
	while(i < len(p)):
		p[0].append(p[i])
		i = i+1

def p_expr4(p):
	'''expr4 : expr4 LOGICALAND expr5
			 | expr5
	'''
	i = 1
	p[0] = ['expr4']
	while(i < len(p)):
		p[0].append(p[i])
		i = i+1

def p_expr5(p):
	'''expr5 : expr6 IFF expr6
			 | expr6 DOUBLEEQUAL expr6
			 | expr6 TRIPLEEQUAL expr6
			 | expr6 NOTEQUAL expr6
			 | expr6
	'''
	i = 1
	p[0] = ['expr5']
	while(i < len(p)):
		p[0].append(p[i])
		i = i+1

def p_expr6(p):
	'''expr6 : expr7 LESSEQUAL expr7
		| expr7 LESS expr7
		| expr7 GREATER expr7
		| expr7 GREATEREQUAL expr7
		| expr7
	'''
	i = 1
	p[0] = ['expr6']
	while(i < len(p)):
		p[0].append(p[i])
		i = i+1

def p_expr7(p):
	'''expr7 : expr7 BITXOR expr8
		| expr7 PIPE expr8
		| expr8
	'''
    	i = 1
	p[0] = ['expr7']
	while(i < len(p)):
		p[0].append(p[i])
		i = i+1

def p_expr8(p):
	'''expr8 : expr8 BITAND expr9
		| expr9
	'''
	i = 1
	p[0] = ['expr8']
	while(i < len(p)):
		p[0].append(p[i])
		i = i+1

def p_expr9(p):
	'''expr9 : expr9 SHIFTL expr10
		| expr9 SHIFTR expr10
		| expr10
	'''
	i = 1
	p[0] = ['expr9']
	while(i < len(p)):
		p[0].append(p[i])
		i = i+1

def p_expr10(p):
	'''expr10 : expr10 PLUS expr11
		| expr10 MINUS expr11
		| expr11
	'''
	i = 1
	p[0] = ['expr10']
	while(i < len(p)):
		p[0].append(p[i])
		i = i+1

def p_expr11(p):
	'''expr11 : expr11 MULTIPLY expr12
		| expr11 DIV expr12
		| expr11 MOD expr12
		| expr12
	'''
	i = 1
	p[0] = ['expr11']
	while(i < len(p)):
		p[0].append(p[i])
		i = i+1

def p_expr12(p):
	'''expr12 : expr13 DOUBLESTAR expr12
			| expr13
	'''
	i = 1
	p[0] = ['expr12']
	while(i < len(p)):
		p[0].append(p[i])
		i = i+1


def p_expr13(p):
	'''expr13 : OPEN_PAREN expr1 CLOSE_PAREN
			  | uexpr INT_CONSTANTS
			  |  uexpr  FLOAT_CONSTANTS
			  |   CONSTANTS
			  |   VARIABLES
	'''
	i = 1
	p[0] = ['expr13']
	while(i < len(p)):
		p[0].append(p[i])
		i = i+1


def p_uexpr(p):
	'''uexpr : none
			  |  PLUS
			  |   MINUS
			  | BITNOT
			  | BITCOMP
	'''
	i = 1
	p[0] = ['uexpr']
	while(i < len(p)):
		p[0].append(p[i])
		i = i+1



def p_opt_terms(p):
	'''opt_terms : none
	   | terms
	'''
	i = 1
	p[0] = ['opt_terms']
	while(i < len(p)):
		p[0].append(p[i])
		i = i+1

def p_terms(p):
	'''terms : term
		| terms term
	'''
	i = 1
	p[0] = ['terms']
	while(i < len(p)):
		p[0].append(p[i])
		i = i+1

def p_term(p):
	'''term : DELIM
			| newline
	'''
	i = 1
	p[0] = ['term']
	while(i < len(p)):
		if p[i] != '\n':
			p[0].append(p[i])
		else:
			p[0].append('NEWLINE')
		i = i+1

def p_none(p):
	'''none :
	'''
	i = 1
	p[0] = ['none']
	while(i < len(p)):
		p[0].append(p[i])
		i = i+1

yacc.yacc()

# while True:
#    try:
# #       s = raw_input('test > ')
s= "a=2 \n if a==2 then a=3; end \n while a>1 do a =a-1; end"
# except EOFError:
#     break
# if not s: continue
result = yacc.parse(s)
print(result)
