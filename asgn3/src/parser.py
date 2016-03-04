#!/usr/bin/python
import ply.yacc as yacc
import sys
from lexer import tokens
import types
body = ""
filename = sys.argv[1]

def printSentential(tree,counter):
	global body
	allLeaves = True
	for i in range(1,len(tree)):
		if(isinstance(tree[i], types.StringTypes) == True):
			#print tree[i]
			if "#" in tree[i]:
				tree[i] = tree[i][:-1]
				body = body + "<b>" + " " + tree[i] + "</b>"
			else:
				body = body + " " + tree[i]
		else:
			tree[i] = printSentential(tree[i], (allLeaves and counter))
			allLeaves = False
	if(allLeaves == True and counter == True):
		tree = tree[0]+"#"												### Mark the non-terminal(tree[0]) as the one which was reduced
	return tree

def printRightDeriv(tree):
	global body
	while(isinstance(tree, types.StringTypes) == False):
		tree = printSentential(tree,True)
		print body + "<br>"
		#print ('\n')
		body = ""
	print "<b>" + tree[:-1] + "</b>" + "<br>"

def p_program(p):
	'''program		: top_top_compstmt
	'''
	i = 1
	p[0] = ['program']
	while(i < len(p)):
		p[0].append(p[i])
		i = i+1

def p_top_top_compstmt(p):
	'''top_top_compstmt : statements opt_terms
	'''
	i = 1
	p[0] = ['top_top_compstmt']
	while(i < len(p)):
		p[0].append(p[i])
		i = i+1

def p_statements(p):
	'''statements : statement
				| statements terms statement
				| none
	'''
	i = 1
	p[0] = ['statements']
	while(i < len(p)):
		p[0].append(p[i])
		i = i+1

def p_statement(p):
	'''statement : top_compstmt
				| func_defn
				| class_defn
				| CONSTANTS DOT VARIABLES opt_oparen arguments opt_cparen
				| CONSTANTS DOT KEYWORD_new opt_oparen arguments opt_cparen
	'''
	i = 1
	p[0] = ['statement']
	while(i < len(p)):
		p[0].append(p[i])
		i = i+1

def p_func_defn(p):
	''' func_defn : KEYWORD_def fname opt_oparen arguments opt_cparen func_stmts opt_terms KEYWORD_end
	'''
	i = 1
	p[0] = ['func_defn']
	while(i < len(p)):
		p[0].append(p[i])
		i = i+1

def p_class_defn(p):
	'''class_defn : KEYWORD_class CONSTANTS newline class_stmts opt_terms KEYWORD_end
	'''
	i = 1
	p[0] = ['class_defn']
	while(i < len(p)):
		if p[i]!= '\n':
			p[0].append(p[i])
		else:
			p[0].append("NEWLINE")
		i = i+1

# def p_class_method_stmts(p):
# 	''' class_method_stmts : class_method_stmt
# 				   | class_method_stmts terms class_method_stmt
# 				   | none
# 	'''
# 	i=1
# 	p[0] = ['class_method_stmts']
# 	while(i < len(p)):
# 		p[0].append(p[i])
# 		i = i+1

# def p_class_method_stmt(p):
# 	''' class_method_stmt : class_method_mlhs EQUAL class_method_mrhs
# 					|  class_method_mlhs
# 				    | KEYWORD_return class_method_ret_arg
# 	'''
# 	i=1
# 	p[0] = ['class_method_stmt']
# 	while(i < len(p)):
# 		p[0].append(p[i])
# 		i = i+1
def p_class_stmts(p):
	'''class_stmts :  class_stmt
					|  class_stmts terms class_stmt
					| none
	'''
	i = 1
	p[0] = ['class_stmts']
	while(i < len(p)):
		p[0].append(p[i])
		i = i+1


def p_class_stmt(p):
	'''class_stmt :  class_mlhs EQUAL class_mrhs
					|  class_func
	'''
	i = 1
	p[0] = ['class_stmt']
	while(i < len(p)):
		p[0].append(p[i])
		i = i+1

def p_class_mrhs(p):
	'''class_mrhs : literal
	'''
	i = 1
	p[0] = ['class_mrhs']
	while(i < len(p)):
		p[0].append(p[i])
		i = i+1

def p_literal(p):
	''' literal : INT_CONSTANTS
				| FLOAT_CONSTANTS
				| STRING_CONSTANTS
				| BOOLEAN_CONSTANTS
				| CHAR_CONSTANTS
				| SIGIL_AT
				| SIGIL_DOUBLE_AT
	'''
	i = 1
	p[0] = ['literal']
	while(i < len(p)):
		p[0].append(p[i])
		i = i+1

def p_class_mlhs(p):
	'''class_mlhs : class_mlhs terms SIGIL_DOUBLE_AT
				   | SIGIL_DOUBLE_AT
	'''
	i = 1
	p[0] = ['class_mlhs']
	while(i < len(p)):
		p[0].append(p[i])
		i = i+1


def p_class_func(p):
	'''class_func : KEYWORD_def fname opt_oparen arguments opt_cparen class_method_stmts opt_terms KEYWORD_end
	'''
	i = 1
	p[0] = ['class_func']
	while(i < len(p)):
		p[0].append(p[i])
		i = i+1

def p_class_method_stmts(p):
	''' class_method_stmts : class_method_stmt
				   | class_method_stmts terms class_method_stmt
				   | none
	'''
	i=1
	p[0] = ['class_method_stmts']
	while(i < len(p)):
		p[0].append(p[i])
		i = i+1

def p_class_method_stmt(p):
	''' class_method_stmt : class_method_mlhs EQUAL class_method_mrhs
				    | KEYWORD_return class_method_ret_arg
	'''
	i=1
	p[0] = ['class_method_stmt']
	while(i < len(p)):
		p[0].append(p[i])
		i = i+1

def p_class_method_mlhs(p):
	'''class_method_mlhs : class_method_mlhs terms SIGIL_AT
						  | SIGIL_AT
	'''
	i=1
	p[0] = ['class_method_stmt']
	while(i < len(p)):
		p[0].append(p[i])
		i = i+1

def p_class_method_mrhs(p):
	'''class_method_mrhs : literal
						 | VARIABLES
	'''
	i=1
	p[0] = ['class_method_mrhs']
	while(i < len(p)):
		p[0].append(p[i])
		i = i+1

def p_class_method_ret_arg(p):
	'''class_method_ret_arg : class_method_arg_expr
				 | literal
				 | class_method_ret_arg COMMA class_method_arg_expr
				 | class_method_ret_arg COMMA literal

	'''
	i=1
	p[0] = ['class_method_ret_arg']
	while(i < len(p)):
		p[0].append(p[i])
		i = i+1

def p_class_method_arg_expr(p):
	'''class_method_arg_expr : SIGIL_AT EQUAL literal
							 | SIGIL_DOUBLE_AT EQUAL literal
	'''
	p[0] = ['class_method_arg_expr']
	while(i < len(p)):
		p[0].append(p[i])
		i = i+1




def p_fname(p):
	'''fname : VARIABLES
			 | CONSTANTS
	'''
	p[0] = ['fname']
	i=1
	while(i < len(p)):
		p[0].append(p[i])
		i = i+1

def p_argments(p):
	'''arguments : arguments COMMA VARIABLES
				 | arguments COMMA CONSTANTS
				 | arguments COMMA func_arg_expr
				 | VARIABLES
				 | CONSTANTS
				 | func_arg_expr
	'''
	i=1
	p[0] = ['arguments']
	while(i < len(p)):
		p[0].append(p[i])
		i = i+1

def p_func_arg_expr(p):
	'''func_arg_expr : VARIABLES EQUAL primary
					 | CONSTANTS EQUAL primary
	'''
	i=1
	p[0] = ['func_arg_expr']
	while(i < len(p)):
		p[0].append(p[i])
		i = i+1

def p_top_compstmt(p):
	'''top_compstmt	: top_stmts
	'''
	i = 1
	p[0] = ['top_compstmt']
	while(i < len(p)):
		p[0].append(p[i])
		i = i+1

def p_top_stmts(p):
	''' top_stmts : top_stmt
	'''
	i = 1
	p[0] = ['top_stmts']
	while(i < len(p)):
		p[0].append(p[i])
		i = i+1

def p_top_stmt(p):
	'''top_stmt	: stmt
				| KEYWORD_if expr3 opt_then gen_stmts opt_terms elsif_tail opt_else_stmt KEYWORD_end
				| KEYWORD_while expr3 opt_do gen_stmts opt_terms KEYWORD_end
				| top_stmt KEYWORD_while expr3
				| KEYWORD_begin gen_stmts opt_terms KEYWORD_end KEYWORD_while expr3
				| top_stmt KEYWORD_until expr3
				| KEYWORD_until expr3 opt_do gen_stmts opt_terms KEYWORD_end
				| KEYWORD_begin gen_stmts opt_terms KEYWORD_end KEYWORD_until expr3
				| KEYWORD_for opt_oparen multi_var opt_cparen KEYWORD_in for_range opt_do gen_stmts opt_terms KEYWORD_end

	'''
	i = 1
	p[0] = ['top_stmt']
	while(i < len(p)):
		p[0].append(p[i])
		i = i+1

def p_gen_stmts(p):
	'''gen_stmts : top_stmt
				| gen_stmts terms top_stmt
				| none
	'''
	i = 1
	p[0] = ['top_stmt']
	while(i < len(p)):
		p[0].append(p[i])
		i = i+1

def p_stmt(p):
	'''stmt :   expr
			| expr1
			| puts_stmt
			| loop_stmt
			| exit_stmt
			| func_call_stmt
	'''
				# | func_call_stmt
	i = 1
	p[0] = ['stmt']
	while(i < len(p)):
		p[0].append(p[i])
		i = i+1

def p_func_call_stmt(p):
	'''func_call_stmt : fname opt_oparen func_ret_arg opt_cparen
	 				  | MLHS EQUAL fname opt_oparen func_ret_arg opt_cparen
	'''
	i = 1
	p[0] = ['func_call_stmt']
	while(i < len(p)):
		p[0].append(p[i])
		i = i+1

def p_loop_stmt(p):
	''' loop_stmt : KEYWORD_break
					| KEYWORD_next
					| KEYWORD_redo
	'''
	i = 1
	p[0] = ['loop_stmt']
	while(i < len(p)):
		p[0].append(p[i])
		i = i+1

def p_exit_stmt(p):
	''' exit_stmt : KEYWORD_exit
	'''
	i = 1
	p[0] = ['exit_stmt']
	while(i < len(p)):
		p[0].append(p[i])
		i = i+1

def p_puts_stmt(p):
	'''puts_stmt : KEYWORD_puts mrhs
				 | KEYWORD_puts expr
	'''
	i = 1
	p[0] = ['puts_stmt']
	while(i < len(p)):
		p[0].append(p[i])
		i = i+1

def p_func_stmts(p):
	''' func_stmts : func_stmt
				   | func_stmts terms func_stmt
				   | none
	'''
	i=1
	p[0] = ['func_stmts']
	while(i < len(p)):
		p[0].append(p[i])
		i = i+1

def p_func_stmt(p):
	''' func_stmt : top_stmt
				  | KEYWORD_return func_ret_arg
	'''
	i=1
	p[0] = ['func_stmt']
	while(i < len(p)):
		p[0].append(p[i])
		i = i+1

def p_func_ret_arg(p):
	'''func_ret_arg : func_arg_expr
				 | primary
				 | func_ret_arg COMMA func_arg_expr
				 | func_ret_arg COMMA primary

	'''
	i=1
	p[0] = ['func_ret_arg']
	while(i < len(p)):
		p[0].append(p[i])
		i = i+1

def p_opt_else_stmt(p):
	'''opt_else_stmt : KEYWORD_else gen_stmts
					 | none
	'''
	i = 1
	p[0] = ['opt_else_stmt']
	while(i < len(p)):
		p[0].append(p[i])
		i = i+1


def p_elsif_tail(p):
	'''elsif_tail :  none
				| KEYWORD_elsif expr3 opt_then gen_stmts elsif_tail
	'''
	i = 1
	p[0] = ['elsif_tail']
	while(i < len(p)):
		p[0].append(p[i])
		i = i+1

def p_opt_then(p):
	'''opt_then : KEYWORD_then
				| newline
	'''
	i=1
	p[0] = ['opt_then']
	while(i < len(p)):
		p[0].append(p[i])
		i = i+1

def p_opt_do(p):
	'''opt_do : KEYWORD_do
				| newline
	'''
	i=1
	p[0] = ['opt_do']
	while(i < len(p)):
		p[0].append(p[i])
		i = i+1

def p_multi_var(p):
	'''multi_var  : VARIABLES
				| CONSTANTS
				| array
				| multi_var COMMA VARIABLES
				| multi_var COMMA CONSTANTS
	'''
	i=1
	p[0] = ['multi_var']
	while(i < len(p)):
		p[0].append(p[i])
		i = i+1

def p_opt_oparen(p):
	'''opt_oparen : OPEN_PAREN
				| none
	'''
	i=1
	p[0] = ['opt_oparen']
	while(i < len(p)):
		p[0].append(p[i])
		i = i+1

def p_opt_cparen(p):
	'''opt_cparen : CLOSE_PAREN
				| none
	'''
	i=1
	p[0] = ['opt_cparen']
	while(i < len(p)):
		p[0].append(p[i])
		i = i+1

def p_for_range(p):
	'''for_range : INT_CONSTANTS DOUBLEDOT INT_CONSTANTS
				| INT_CONSTANTS TRIPLEDOT INT_CONSTANTS
				| VARIABLES
				| array
				| CONSTANTS
	'''
	i=1
	p[0] = ['for_range']
	while(i < len(p)):
		p[0].append(p[i])
		i = i+1

def p_expr(p):
	'''expr :   MLHS EQUAL MRHS
	'''
	i = 1
	p[0] = ['expr']
	while(i < len(p)):
		p[0].append(p[i])
		i = i+1

def p_MLHS(p):
	'''MLHS : mlhs
			| MLHS COMMA mlhs
	'''
	i=1
	p[0] = ['MLHS']
	while(i < len(p)):
		p[0].append(p[i])
		i = i+1

def p_MRHS(p):
	'''MRHS : mrhs
			| MRHS COMMA mrhs

	'''
	i=1
	p[0] = ['MRHS']
	while(i < len(p)):
		p[0].append(p[i])
		i = i+1

def p_mlhs(p):
	'''mlhs : VARIABLES
			| CONSTANTS
			| array
	'''
	i = 1
	p[0] = ['mlhs']
	while(i < len(p)):
		p[0].append(p[i])
		i = i+1

def p_mrhs(p):
	'''mrhs :   expr1
			| str_expr
			| KEYWORD_gets
			| OPEN_BRACKET func_ret_arg CLOSE_BRACKET
			| CONSTANTS DOT VARIABLES OPEN_PAREN arguments CLOSE_PAREN
			| CONSTANTS DOT VARIABLES
			| CONSTANTS DOT KEYWORD_new OPEN_PAREN arguments CLOSE_PAREN
			| CONSTANTS DOT KEYWORD_new

	'''
	#	| CONSTANTS DOT KEYWORD_new opt_oparen arguments opt_cparen
	i = 1
	p[0] = ['mrhs']
	while(i < len(p)):
		p[0].append(p[i])
		i = i+1

def p_str_expr(p):
	'''str_expr : str_expr PLUS STRING_CONSTANTS
				| STRING_CONSTANTS
	'''
	i = 1
	p[0] = ['str_expr']
	while(i < len(p)):
		p[0].append(p[i])
		i = i+1

def p_primary(p):
	'''primary  :   INT_CONSTANTS
		|   FLOAT_CONSTANTS
		|   STRING_CONSTANTS
		|   CHAR_CONSTANTS
		|   BOOLEAN_CONSTANTS
		|   CONSTANTS
		|   VARIABLES
		|	array
	'''
	i = 1
	p[0] = ['primary']
	while(i < len(p)):
		p[0].append(p[i])
		i = i+1

# def user_variable(p):
# 	'''user_variable	: VARIABLES
# 		| CONSTANTS
#		| array
# 	'''
# 	i = 1
# 	p[0] = ['user_variable']
# 	while(i < len(p)):
# 		p[0].append(p[i])
# 		i = i+1

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
		| BOOLEAN_CONSTANTS
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
			  | array
	'''
	i = 1
	p[0] = ['expr13']
	while(i < len(p)):
		p[0].append(p[i])
		i = i+1

def p_array(p):
	'''array : VARIABLES OPEN_BRACKET expr7 CLOSE_BRACKET
			 | VARIABLES OPEN_BRACKET expr7 DOUBLEDOT expr7 CLOSE_BRACKET
			 | VARIABLES OPEN_BRACKET expr7 TRIPLEDOT expr7 CLOSE_BRACKET
	'''
	i = 1
	p[0] = ['array']
	while(i < len(p)):
		p[0].append(p[i])
		i = i+1
def p_uexpr(p):
	'''uexpr : none
			  | PLUS
			  | MINUS
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
#data = "a+3+4; a[1] \n a=[1,2,2]"
with open(filename,'r') as myfile:
	data=myfile.read()
result = yacc.parse(data)

printRightDeriv(result)
