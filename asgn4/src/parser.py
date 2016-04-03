#!/usr/bin/python
import ply.yacc as yacc
import sys
import lexer
from lexer import tokens
import symtable as st
import types
import TAC as tac
body = ""
filename = sys.argv[1]

def strType(var):
    try:
        if int(var) == float(var):
            return 'int'
    except:
        try:
            float(var)
            return 'float'
        except:
            return 'str'

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
		tree = tree[0]+"#"
	return tree

def printRightDeriv(tree):
	global body
	while(isinstance(tree, types.StringTypes) == False):
		tree = printSentential(tree,True)
		print body + "<br>"
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
				| VARIABLES DOT VARIABLES OPEN_PAREN arguments CLOSE_PAREN
				| VARIABLES DOT VARIABLES OPEN_PAREN CLOSE_PAREN
				| VARIABLES DOT VARIABLES arguments
				| CONSTANTS DOT KEYWORD_new OPEN_PAREN arguments CLOSE_PAREN
				| CONSTANTS DOT KEYWORD_new OPEN_PAREN CLOSE_PAREN
				| CONSTANTS DOT KEYWORD_new arguments
	'''
	i = 1
	p[0] = ['statement']
	while(i < len(p)):
		p[0].append(p[i])
		i = i+1

def p_func_defn(p):
	''' func_defn : KEYWORD_def fname OPEN_PAREN arguments CLOSE_PAREN func_stmts opt_terms KEYWORD_end
					| KEYWORD_def fname OPEN_PAREN CLOSE_PAREN func_stmts opt_terms KEYWORD_end
				   |  KEYWORD_def fname arguments func_stmts opt_terms KEYWORD_end
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
	'''class_func : KEYWORD_def fname OPEN_PAREN arguments CLOSE_PAREN class_method_stmts opt_terms KEYWORD_end
				  | KEYWORD_def fname arguments class_method_stmts opt_terms KEYWORD_end
				  | KEYWORD_def fname OPEN_PAREN CLOSE_PAREN class_method_stmts opt_terms KEYWORD_end
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
				    | puts_stmt
	'''
	i=1
	p[0] = ['class_method_stmt']
	while(i < len(p)):
		p[0].append(p[i])
		i = i+1

def p_class_method_mlhs(p):
	'''class_method_mlhs : class_method_mlhs terms SIGIL_AT
						  | SIGIL_AT
						  | SIGIL_DOUBLE_AT
	'''
	i=1
	p[0] = ['class_method_mlhs']
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

def p_arguments(p):
	'''arguments : arguments COMMA VARIABLES
				 | arguments COMMA CONSTANTS
				 | arguments COMMA func_arg_expr
				 | VARIABLES
				 | CONSTANTS
				 | func_arg_expr
				 | newline
	'''
	i=1
	p[0] = ['arguments']
	while(i < len(p)):
		if p[i] != '\n':
			p[0].append(p[i])
		else:
			p[0].append('NEWLINE')
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
				| KEYWORD_if expr3 opt_then gen_stmts opt_terms elsif_tail opt_else_stmt  KEYWORD_end
				| KEYWORD_while expr3 opt_do gen_stmts opt_terms KEYWORD_end
				| top_stmt KEYWORD_while expr3
				| KEYWORD_begin gen_stmts opt_terms KEYWORD_end KEYWORD_while expr3
				| top_stmt KEYWORD_until expr3
				| KEYWORD_until expr3 opt_do gen_stmts opt_terms KEYWORD_end
				| KEYWORD_begin gen_stmts opt_terms KEYWORD_end KEYWORD_until expr3
				| KEYWORD_for OPEN_PAREN multi_var CLOSE_PAREN KEYWORD_in for_range opt_do gen_stmts opt_terms KEYWORD_end
				| KEYWORD_for multi_var KEYWORD_in for_range opt_do gen_stmts opt_terms KEYWORD_end


	'''
	# i = 1
	# p[0] = ['top_stmt']
	# while(i < len(p)):
	# 	p[0].append(p[i])
	# 	i = i+1

def p_gen_stmts(p):
	'''gen_stmts : top_stmt
				| gen_stmts terms top_stmt
				| none
	'''
	i = 1
	p[0] = ['gen_stmts']
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

	# i = 1
	# p[0] = ['stmt']
	# while(i < len(p)):
	# 	p[0].append(p[i])
	# 	i = i+1

def p_func_call_stmt(p):
	'''func_call_stmt : fname OPEN_PAREN func_ret_arg CLOSE_PAREN
					  | fname func_ret_arg
	 				  | mlhs EQUAL fname OPEN_PAREN func_ret_arg CLOSE_PAREN
	 				  | mlhs EQUAL fname func_ret_arg
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
	# i = 1
	# p[0] = ['loop_stmt']
	# while(i < len(p)):
	# 	p[0].append(p[i])
	# 	i = i+1

def p_exit_stmt(p):
    ''' exit_stmt : KEYWORD_exit'''
    TAC.emit("exit")
# p[0] = TODO
# i = 1
# p[0] = ['exit_stmt']
# while(i < len(p)):
# 	p[0].append(p[i])
# 	i = i+1

def p_puts_stmt(p):
    '''puts_stmt : KEYWORD_puts mrhs
				 | KEYWORD_puts expr
    '''
    TAC.emit("print", p[2]["place"])
    # p[0] = TODO
	# i = 1
	# p[0] = ['puts_stmt']
	# while(i < len(p)):
	# 	p[0].append(p[i])
	# 	i = i+1

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
	'''opt_else_stmt : KEYWORD_else gen_stmts opt_terms
					 | none
	'''
	i = 1
	p[0] = ['opt_else_stmt']
	while(i < len(p)):
		p[0].append(p[i])
		i = i+1


def p_elsif_tail(p):
	'''elsif_tail :  none
				| KEYWORD_elsif expr3 opt_then gen_stmts opt_terms elsif_tail
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
		if p[i]!= '\n':
				p[0].append(p[i])
		else:
			p[0].append("NEWLINE")
		i = i+1

def p_opt_do(p):
	'''opt_do : KEYWORD_do
				| newline
	'''
	i=1
	p[0] = ['opt_do']
	while(i < len(p)):
		if p[i]!= '\n':
				p[0].append(p[i])
		else:
			p[0].append("NEWLINE")
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

def p_for_range(p):
	'''for_range : OPEN_PAREN INT_CONSTANTS DOUBLEDOT INT_CONSTANTS CLOSE_PAREN
				| INT_CONSTANTS DOUBLEDOT INT_CONSTANTS
				| OPEN_PAREN INT_CONSTANTS TRIPLEDOT INT_CONSTANTS CLOSE_PAREN
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
    '''expr :   mlhs EQUAL mrhs
    '''
    #type-check
    ST.update(p[1]["place"], "type", p[3]["type"])
    TAC.emit('Assignment', [p[1]["place"], p[3]["place"]])
    p[0] = p[1]
	# i = 1
	# p[0] = ['expr']
	# while(i < len(p)):
	# 	p[0].append(p[i])
	# 	i = i+1

# def p_MLHS(p):
# 	'''MLHS : mlhs
# 			| MLHS COMMA mlhs
# 	'''
# 	i=1
# 	p[0] = ['MLHS']
# 	while(i < len(p)):
# 		p[0].append(p[i])
# 		i = i+1
#
# def p_MRHS(p):
# 	'''MRHS : mrhs
# 			| MRHS COMMA mrhs
#
# 	'''
# 	i=1
# 	p[0] = ['MRHS']
# 	while(i < len(p)):
# 		p[0].append(p[i])
# 		i = i+1

def p_mlhs(p):
    '''mlhs : VARIABLES
    		| CONSTANTS
    		| array
    '''
    if(isinstance(p[1],dict)):
        p[0] = p[1]
    else:
        ST.update(p[1],"declare", True)
        var_dict = ST.varlookup(p[1])
        p[0] = {"place":p[1], "type": var_dict["type"]}

	# i = 1
	# p[0] = ['mlhs']
	# while(i < len(p)):
	# 	p[0].append(p[i])
	# 	i = i+1

def p_mrhs(p):
	'''mrhs :   expr1
			| str_expr
			| KEYWORD_gets
			| OPEN_BRACKET CLOSE_BRACKET
			| VARIABLES DOT VARIABLES OPEN_PAREN arguments CLOSE_PAREN
			| VARIABLES DOT VARIABLES OPEN_PAREN CLOSE_PAREN
			| VARIABLES DOT VARIABLES
			| CONSTANTS DOT KEYWORD_new OPEN_PAREN arguments CLOSE_PAREN
			| CONSTANTS DOT KEYWORD_new
			| CONSTANTS DOT KEYWORD_new OPEN_PAREN CLOSE_PAREN

	'''
	if (len(p)==2):
		if p[1] == 'gets':
		    temp_name = ST.newtemp({"type":"none"})
		    TAC.emit('Assignment', [temp_name, "scan"])
		    p[0] = {"place": temp_name, "type": "none"}
		else:
		    p[0] = p[1]
	elif (len(p) == 3):
		temp_name = ST.newtemp({"type" : "array"})
		TAC.emit('Assignment', [temp_name, "[]"])
		p[0] = {"place": temp_name, "type": "array"}
	# i = 1
	# p[0] = ['mrhs']
	# while(i < len(p)):
	# 	p[0].append(p[i])
	# 	i = i+1

def p_str_expr(p):
	'''str_expr : STRING_CONSTANTS
	'''
	temp_name = ST.newtemp({"type" : "string"})
	TAC.emit('Assignment', [temp_name, p[1]])
	p[0] = {"place": temp_name, "type": "string"}
	# i = 1
	# p[0] = ['str_expr']
	# while(i < len(p)):
	# 	p[0].append(p[i])
	# 	i = i+1

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

	if (isinstance(p[1],dict)):
		TAC.emit('Assignment',[temp_name, p[1]["place"]])
		p[0] = p[1]
	elif p[1] == 'TRUE':
		temp_name = ST.newtemp({"type" : "bool"})
		TAC.emit('Assignment', [temp_name, '1'])
		p[0] = {"place": temp_name, "type": "bool"}
	elif p[1] == 'FALSE':
		temp_name = ST.newtemp({"type" : "bool"})
		TAC.emit('Assignment', [temp_name, '0'])
		p[0] = {"place": temp_name, "type": "bool"}
	else:
		TAC.emit('Assignment',[temp_name, p[1]])
		if (strType(p[1])=='int'):
		    temp_name = ST.newtemp({"type" : "int"})
		    p[0] = {"place": temp_name, "type": "int"}

		elif (strType(p[1])=='float'):
		    temp_name = ST.newtemp({"type" : "float"})
		    p[0] = {"place": temp_name, "type": "float"}

		elif (strType(p[1])=='str'):
		    temp_name = ST.newtemp({"type" : "string"})
		    p[0] = {"place": temp_name, "type": "string"}


	# i = 1
	# p[0] = ['primary']
	# while(i < len(p)):
	# 	p[0].append(p[i])
	# 	i = i+1

def p_expr1(p):
	'''expr1 : expr3
	'''
	p[0] = p[1]
	# i = 1
	# p[0] = ['expr1']
	# while(i < len(p)):
	# 	p[0].append(p[i])
	# 	i = i+1

# def p_expr2(p):
# 	'''expr2 : expr7 DOUBLEDOT expr7
# 			 | expr7 TRIPLEDOT expr7
# 			 | expr3
# 	'''
# 	i = 1
# 	p[0] = ['expr2']
# 	while(i < len(p)):
# 		p[0].append(p[i])
# 		i = i+1

def p_expr3(p):
	'''expr3 : expr3 LOGICALOR expr4
			 | expr4
	'''
	if (len(p)==2):
		p[0] = {"place": p[1]["place"], "type": p[1]["type"]}
	else:
		temp_name = ST.newtemp({"type" : "bool"})
		label_name = ST.newlabel()
		label_name2 = ST.newlabel()
		TAC.emit('logical', ['|',temp_name, p[1]["place"], p[2]["place"]])
		TAC.emit('ifgoto',["bne",temp_name,'0',label_name])
		TAC.emit('Assignment', [temp_name, '0'])
		TAC.emit('goto', [label_name2])
		TAC.emit('label',[label_name])
		TAC.emit('Assignment', [temp_name, '1'])
		TAC.emit('label', [label_name2])
		p[0] = {"place": temp_name, "type": "bool"}

	# i = 1
	# p[0] = ['expr3']
	# while(i < len(p)):
	# 	p[0].append(p[i])
	# 	i = i+1

def p_expr4(p):
	'''expr4 : expr4 LOGICALAND expr5
			 | expr5
	'''
	if (len(p)==2):
		p[0] = {"place": p[1]["place"], "type": p[1]["type"]}
	else:
		temp_name = ST.newtemp({"type" : "bool"})
		label_name = ST.newlabel()
		label_name2 = ST.newlabel()
		TAC.emit('logical', ['&',temp_name, p[1]["place"], p[2]["place"]])
		TAC.emit('ifgoto',["bne",temp_name,'0',label_name])
		TAC.emit('Assignment', [temp_name, '0'])
		TAC.emit('goto', [label_name2])
		TAC.emit('label',[label_name])
		TAC.emit('Assignment', [temp_name, '1'])
		TAC.emit('label', [label_name2])
		p[0] = {"place": temp_name, "type": "bool"}
	# i = 1
	# p[0] = ['expr4']
	# while(i < len(p)):
	# 	p[0].append(p[i])
	# 	i = i+1

def p_expr5(p):
	'''expr5 : expr6 DOUBLEEQUAL expr6
			 | expr6 NOTEQUAL expr6
			 | expr6
	'''
	if (len(p)==2):
		p[0] = {"place": p[1]["place"], "type": p[1]["type"]}
	else:
		temp_name = ST.newtemp({"type" : "bool"})
		label_name = ST.newlabel()
		label_name2 = ST.newlabel()
		if (p[2] == '=='):
			TAC.emit('ifgoto',["beq",p[1]["place"],p[3]["place"],label_name])
		else:
			TAC.emit('ifgoto',["bne",p[1]["place"],p[3]["place"],label_name])
		TAC.emit('Assignment', [temp_name, '0'])
		TAC.emit('goto', [label_name2])
		TAC.emit('label',[label_name])
		TAC.emit('Assignment', [temp_name, '1'])
		TAC.emit('label', [label_name2])
		p[0] = {"place": temp_name, "type": "bool"}
	# i = 1
	# p[0] = ['expr5']
	# while(i < len(p)):
	# 	p[0].append(p[i])
	# 	i = i+1

def p_expr6(p):
	'''expr6 : expr7 LESSEQUAL expr7
		| expr7 LESS expr7
		| expr7 GREATER expr7
		| expr7 GREATEREQUAL expr7
		| expr7
		| BOOLEAN_CONSTANTS
	'''
	if (len(p)==2):
		if(p[1]=="TRUE"):
			temp_name = ST.newtemp({"type" : "bool"})
			TAC.emit('Assignment',[temp_name, '1'])
			p[0] = {"place": temp_name, "type": "bool"}
		elif(p[1]=="FALSE"):
			temp_name = ST.newtemp({"type" : "bool"})
			TAC.emit('Assignment',[temp_name, '0'])
			p[0] = {"place": temp_name, "type": "bool"}
		else:
			p[0] = {"place": p[1]["place"], "type": p[1]["type"]}
	else:
		temp_name = ST.newtemp({"type" : "bool"})
		label_name = ST.newlabel()
		label_name2 = ST.newlabel()
		if (p[2]=="<="):
			TAC.emit('ifgoto',["ble",p[1]["place"],p[3]["place"],label_name])
		elif (p[2]=="<"):
			TAC.emit('ifgoto',["bl",p[1]["place"],p[3]["place"],label_name])
		elif (p[2]==">"):
			TAC.emit('ifgoto',["bg",p[1]["place"],p[3]["place"],label_name])
		elif (p[2]==">="):
			TAC.emit('ifgoto',["bge",p[1]["place"],p[3]["place"],label_name])
		TAC.emit('Assignment', [temp_name, '0'])
		TAC.emit('goto', [label_name2])
		TAC.emit('label',[label_name])
		TAC.emit('Assignment', [temp_name, '1'])
		TAC.emit('label', [label_name2])
		p[0] = {"place": temp_name, "type": "bool"}
	# i = 1
	# p[0] = ['expr6']
	# while(i < len(p)):
	# 	p[0].append(p[i])
	# 	i = i+1

def p_expr7(p):
	'''expr7 : expr7 BITXOR expr8
		| expr7 PIPE expr8
		| expr8
	'''
	if (len(p)==2):
		p[0] = {"place": p[1]["place"], "type": p[1]["type"]}
	else:
		temp_name = ST.newtemp({"type" : "int"})
		TAC.emit('logical',[p[2],temp_name,p[1]["place"],p[3]["place"]])
		p[0] = {"place": temp_name, "type": p[1]["type"]}
	# i = 1
	# p[0] = ['expr7']
	# while(i < len(p)):
	# 	p[0].append(p[i])
	# 	i = i+1

def p_expr8(p):
	'''expr8 : expr8 BITAND expr9
		| expr9
	'''
	if (len(p)==2):
		p[0] = {"place": p[1]["place"], "type": p[1]["type"]}
	else:
		temp_name = ST.newtemp({"type" : "int"})
		TAC.emit('logical',[p[2],temp_name,p[1]["place"],p[3]["place"]])
		p[0] = {"place": temp_name, "type": p[1]["type"]}
	# i = 1
	# p[0] = ['expr8']
	# while(i < len(p)):
	# 	p[0].append(p[i])
	# 	i = i+1

def p_expr9(p):
	'''expr9 : expr9 SHIFTL expr10
		| expr9 SHIFTR expr10
		| expr10
	'''
	if (len(p)==2):
		p[0] = {"place": p[1]["place"], "type": p[1]["type"]}
	else:
		temp_name = ST.newtemp({"type" : "int"})
		TAC.emit('logical',[p[2],temp_name,p[1]["place"],p[3]["place"]])
		p[0] = {"place": temp_name, "type": p[1]["type"]}
	# i = 1
	# p[0] = ['expr9']
	# while(i < len(p)):
	# 	p[0].append(p[i])
	# 	i = i+1

def p_expr10(p):
	'''expr10 : expr10 PLUS expr11
		| expr10 MINUS expr11
		| expr11
	'''
	if (len(p)==2):
		p[0] = {"place": p[1]["place"], "type": p[1]["type"]}
	else:
		temp_name = ST.newtemp({"type" : "int"})
		TAC.emit('Arithmetic',[p[2],temp_name,p[1]["place"],p[3]["place"]])
		p[0] = {"place": temp_name, "type": p[1]["type"]}
	# i = 1
	# p[0] = ['expr10']
	# while(i < len(p)):
	# 	p[0].append(p[i])
	# 	i = i+1

def p_expr11(p):
	'''expr11 : expr11 MULTIPLY expr13
		| expr11 DIV expr13
		| expr11 MOD expr13
		| expr13
	'''
	if (len(p)==2):
		p[0] = {"place": p[1]["place"], "type": p[1]["type"]}
	else:
		temp_name = ST.newtemp({"type" : "int"})
		TAC.emit('Arithmetic',[p[2],temp_name,p[1]["place"],p[3]["place"]])
		p[0] = {"place": temp_name, "type": p[1]["type"]}
	# i = 1
	# p[0] = ['expr11']
	# while(i < len(p)):
	# 	p[0].append(p[i])
	# 	i = i+1

# def p_expr12(p):
# 	'''expr12 : expr13 DOUBLESTAR expr12
# 			| expr13
# 	'''
# 	temp_name = ST.newtemp()
# 	TAC.emit('')
	# i = 1
	# p[0] = ['expr12']
	# while(i < len(p)):
	# 	p[0].append(p[i])
	# 	i = i+1


def p_expr13(p):
    '''expr13 : OPEN_PAREN expr1 CLOSE_PAREN
    		  | uexpr INT_CONSTANTS
    		  | uexpr  FLOAT_CONSTANTS
    		  | CONSTANTS
    		  | VARIABLES
    		  | array
    '''
    if(len(p)==2):
        if (isinstance(p[1],dict)):   ## ARRAY
            TAC.emit('Assignment', [temp_name, p[1]["place"]])
            p[0] = p[1]
        else:              ## constants, variables
            temp_name = ST.newtemp({})
            TAC.emit('Assignment', [temp_name, p[1]])
            var_dict = ST.varlookup(p[1])
            if (var_dict["declare"] == False):
                print("declaration error: variable", p[1], 'not declared.')
            p[0] = {"place": temp_name, "type": var_dict["type"]}
            ST.update(temp_name, "type", var_dict["type"])
    		# if(p[0]["type"]=="none"):
    		# 	print ("ERROR")
    elif (len(p)==3):
    	print (p[1],p[2])
    	temp_name = ST.newtemp({})
    	TAC.emit('Assignment', [temp_name, p[1]+p[2]])
    	if (strType(p[2])=="int"):
    		ST.update(temp_name,"type","integer")
    		p[0] = {"place": temp_name, "type": "integer"}
    	if (strType(p[2])=="float"):
    		ST.update(temp_name,"type","float")
    		p[0] = {"place": temp_name, "type": "float"}
    elif (len(p)==4):
    	p[0] = {"place": p[2]["place"], "type": p[2]["type"]}
	# i = 1
	# p[0] = ['expr13']
	# while(i < len(p)):
	# 	p[0].append(p[i])
	# 	i = i+1

def p_array(p):
    '''array : VARIABLES OPEN_BRACKET expr7 CLOSE_BRACKET
    '''
    var_dict = ST.varlookup(p[1])
    if(var_dict["declare"]==False):
        print("declaration error: variable", p[1], 'not declared.')
    elif(var_dict["type"] != "array"):
        print(p[1], 'is not array type.')
    temp_name = ST.newtemp({"type" : "none"})
    TAC.emit('Assignment', [temp_name, p[1]+p[2]+p[3]["place"]+p[4]])
    p[0] = {"place": temp_name, "type": "none"}
# 	i = 1
# 	p[0] = ['array']
# 	while(i < len(p)):
# 		p[0].append(p[i])
# 		i = i+1
def p_uexpr(p):
	'''uexpr : none
			  | PLUS
			  | MINUS
			  | BITNOT
			  | BITCOMP
	'''
	if p[0] == '+':
		p[0] = ""
	else:
		# print p[1]
		p[0]=p[1]
	# i = 1
	# p[0] = ['uexpr']
	# while(i < len(p)):
	# 	p[0].append(p[i])
	# 	i = i+1

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
	p[0] = ""
	# i = 1
	# p[0] = ['none']
	# while(i < len(p)):
	# 	p[0].append(p[i])
	# 	i = i+1

ST = st.Symtable()

myfile = open(filename,'r')
inputArray = myfile.readlines()
myfile.close()
ldata = ""
for i in range(0,len(inputArray)):
	ldata = ldata + inputArray[i]

lexer.Lexer.input(ldata)

while True:
	found = 0
	tok = lexer.Lexer.token()
	if not tok:
		break
	# print tok.value
	if tok.type == 'VARIABLES':
		if not(tok.value in ST.vardict.keys()):
			ST.vardict[tok.value]= {"type":"none", "declare" : False}

# print ST.vardict
yacc.yacc()
pdata = ""
myfile = open(filename,'r')
for line in myfile.readlines():
	if line!='\n':
		pdata = pdata + line

TAC = tac.TAC()

result = yacc.parse(pdata)

TAC.printTAC()

# printRightDeriv(result)
