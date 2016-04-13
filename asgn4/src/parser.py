#!/usr/bin/python
import ply.yacc as yacc
import sys
import lexer
from lexer import tokens
import symtable as st
import types
import TAC as tac
import warnings
def fxn():
    warnings.warn("deprecated", DeprecationWarning)

with warnings.catch_warnings():
    warnings.simplefilter("ignore")
    fxn()
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

def p_top_top_compstmt(p):
	'''top_top_compstmt : statements opt_terms
	'''

def p_statements(p):
	'''statements : statement
				| statements terms statement

	'''

def p_statement(p):
    '''statement : top_stmt
			| func_defn
			| class_defn
			| VARIABLES DOT VARIABLES OPEN_PAREN arguments CLOSE_PAREN
			| VARIABLES DOT VARIABLES OPEN_PAREN CLOSE_PAREN
			| VARIABLES DOT VARIABLES arguments
			| CONSTANTS DOT KEYWORD_new OPEN_PAREN arguments CLOSE_PAREN
			| CONSTANTS DOT KEYWORD_new OPEN_PAREN CLOSE_PAREN
			| CONSTANTS DOT KEYWORD_new arguments
            '''
    if(isinstance(p[1],dict)):
        if("loop" in p[1].keys()):
            print("ERROR: break statement out of loop")
            TAC.error = True

def p_class_defn(p):
	'''class_defn : KEYWORD_class CONSTANTS newline class_stmts opt_terms KEYWORD_end
	'''

def p_class_stmts(p):
	'''class_stmts :  class_stmt
					|  class_stmts terms class_stmt
					| none
	'''

def p_class_stmt(p):
	'''class_stmt :  class_mlhs EQUAL class_mrhs
					|  class_func
	'''

def p_class_mrhs(p):
	'''class_mrhs : literal
	'''

def p_literal(p):
	''' literal : INT_CONSTANTS
				| FLOAT_CONSTANTS
				| STRING_CONSTANTS
				| BOOLEAN_CONSTANTS
				| CHAR_CONSTANTS
				| SIGIL_AT
				| SIGIL_DOUBLE_AT
	'''


def p_class_mlhs(p):
	'''class_mlhs : class_mlhs terms SIGIL_DOUBLE_AT
				   | SIGIL_DOUBLE_AT
	'''



def p_class_func(p):
	'''class_func : KEYWORD_def fname OPEN_PAREN arguments CLOSE_PAREN class_method_stmts opt_terms KEYWORD_end
				  | KEYWORD_def fname arguments class_method_stmts opt_terms KEYWORD_end
				  | KEYWORD_def fname OPEN_PAREN CLOSE_PAREN class_method_stmts opt_terms KEYWORD_end
	'''


def p_class_method_stmts(p):
	''' class_method_stmts : class_method_stmt
				   | class_method_stmts terms class_method_stmt
				   | none
	'''


def p_class_method_stmt(p):
	''' class_method_stmt : class_method_mlhs EQUAL class_method_mrhs
				    | KEYWORD_return class_method_ret_arg
				    | puts_stmt
	'''

def p_class_method_mlhs(p):
	'''class_method_mlhs : class_method_mlhs terms SIGIL_AT
						  | SIGIL_AT
						  | SIGIL_DOUBLE_AT
	'''


def p_class_method_mrhs(p):
	'''class_method_mrhs : literal
						 | VARIABLES
	'''


def p_class_method_ret_arg(p):
	'''class_method_ret_arg : class_method_arg_expr
				 | literal
				 | class_method_ret_arg COMMA class_method_arg_expr
				 | class_method_ret_arg COMMA literal

	'''

def p_class_method_arg_expr(p):
	'''class_method_arg_expr : SIGIL_AT EQUAL literal
							 | SIGIL_DOUBLE_AT EQUAL literal
	'''

def p_func_defn(p):
    ''' func_defn : KEYWORD_def fname OPEN_PAREN arguments M_13 CLOSE_PAREN func_stmts opt_terms KEYWORD_end M_14
					| KEYWORD_def fname OPEN_PAREN CLOSE_PAREN M_18 func_stmts opt_terms KEYWORD_end M_15
                    '''
    global ST
    print p[2]["fname"]
    print ST.vardict
    print ST.funcdict
    global globalST
    ST = globalST
    global localST
    localST = st.Symtable("local")


def p_fname(p):
    '''fname : VARIABLES
		 | CONSTANTS
         '''
    global no_special_reg
    global localST
    global ST
    ST = localST
    label_name = ST.newlabel()
    TAC.emit("goto", [label_name])
    TAC.emit("flabel", [p[1]])
    p[0] = {"label": label_name,"fname":p[1]}
    no_special_reg = 0


def p_arguments(p):
    '''arguments : VARIABLES M_12 COMMA arguments
				 | CONSTANTS M_12 COMMA arguments
				 | VARIABLES M_12
				 | CONSTANTS M_12
                 '''
    if(len(p)==3):
        p[0]=1
    else:
        p[0]=p[4]+1

def p_M_12(p):
    '''M_12 : '''
    vardict = globalST.varlookup(p[-1])
    if(vardict != False):
        print ("Function Argument cannot be a declared same name as global variable")
    ST.varinsert(p[-1], {"type":"none", "declare":True})

    global no_special_reg
    if(no_special_reg > 3):
        print("no of arguments greater than 4")
    TAC.emit("func_arg", [p[-1], no_special_reg])
    no_special_reg += 1

def p_M_13(p):
    '''M_13 : '''
    global no_special_reg
    no_special_reg = 0
    globalST.funcinsert(p[-3]["fname"],{"num":p[-1]})

def p_M_18(p):
    '''M_18 : '''
    global no_special_reg
    no_special_reg = 0
    globalST.funcinsert(p[-3]["fname"],{"num":0})

def p_M_14(p):
    '''M_14 : '''
    TAC.emit("return", [0])
    TAC.emit("label", [p[-8]["label"]])

def p_M_15(p):
    '''M_15 : '''
    TAC.emit("return", [0])
    TAC.emit("label", [p[-7]["label"]])

def p_func_call_stmt(p):
    '''func_call_stmt : fname2 OPEN_PAREN call_arg CLOSE_PAREN M_17
    | mlhs EQUAL fname2 OPEN_PAREN call_arg CLOSE_PAREN M_17'''
    if(len(p)==6):
        TAC.emit('call', [p[1],''])
    else:
        TAC.emit('call', [p[3], p[1]["place"]])

def p_M_17(p):
    '''M_17 : '''
    funcdict = globalST.funclookup(p[-4])
    if(funcdict==False):
        print ('ERROR:',p[-4], 'not defined')
        TAC.error = True
    elif(funcdict["num"]!=p[-2]):
        print ('ERROR', 'Number of arguments passed mismatch in',p[-4])
        TAC.error = True

def p_fname2(p):
    '''fname2 : VARIABLES
		 | CONSTANTS
         '''
    p[0] = p[1]

def p_call_arg(p):
    '''call_arg : primary M_16 COMMA call_arg
                | primary M_16
                | none
    '''
    if(len(p)==2):
        p[0]=0
    elif(len(p)==3):
        p[0]=1
    else:
        p[0]=p[4] +1

def p_M_16(p):
    '''M_16 : '''
    TAC.emit("param", [p[-1]["place"]])

def p_loop_stmt(p):
    ''' loop_stmt : KEYWORD_break'''
    p[0] = p[1]

def p_exit_stmt(p):
    ''' exit_stmt : KEYWORD_exit'''
    TAC.emit("exit")
    # p[0] = TODO

def p_puts_stmt(p):
    '''puts_stmt : KEYWORD_puts mrhs
				 | KEYWORD_puts expr
    '''
    if(p[2]["type"] == "stringc"):
        temp_name = ST.newtemp({"type" : "string"})
    	TAC.emit('Assignment', [temp_name, p[2]["place"]])
        TAC.emit("prints", [temp_name])
    elif(p[2]["type"] == "string"):
        TAC.emit("prints", [p[2]["place"]])
    else:
        TAC.emit("print", [p[2]["place"]])

    # p[0] = TODO

def p_func_stmts(p):
	''' func_stmts : func_stmt
				   | func_stmts terms func_stmt
				   | none
	'''

def p_func_stmt(p):
    ''' func_stmt : top_stmt
			  | KEYWORD_return func_ret_arg
              '''
    if(isinstance(p[1],dict)):
        if("loop" in p[1].keys()):
            print("ERROR: break statement out of loop")
            TAC.error = True
    i = 1
    p[0] = ['statement']
    while(i < len(p)):
    	p[0].append(p[i])
    	i = i+1


def p_func_ret_arg(p):
    '''func_ret_arg : primary
        '''
    TAC.emit("return", [p[1]["place"]])

def p_primary(p):
    '''primary  :   INT_CONSTANTS
    |   BOOLEAN_CONSTANTS
    |   CONSTANTS
    |   VARIABLES
    |	array'''
    global ST
    if (isinstance(p[1],dict)):
        temp_name = ST.newtemp({"type" : "array"})
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
        if (strType(p[1])=='int'):
            temp_name = ST.newtemp({"type" : "int"})
            p[0] = {"place": temp_name, "type": "int"}
            TAC.emit('Assignment',[temp_name, p[1]])
        elif (strType(p[1])=='float'):
            temp_name = ST.newtemp({"type" : "float"})
            p[0] = {"place": temp_name, "type": "float"}
            TAC.emit('Assignment',[temp_name, p[1]])
        else:
            # print ST.vardict
            # print globalST.vardict
            vardict =ST.varlookup(p[1])
            if (vardict == False):
                vardict = globalST.varlookup(p[1])
                if (vardict == False):
                    print ('ERROR: ',p[1],'not declared')
                    TAC.error = True
            p[0] = {"place": p[1], "type": vardict["type"]}

def p_top_stmt(p):
    '''top_stmt	: stmt
    | KEYWORD_if expr3 opt_then M_1 gen_stmts opt_terms M_2 elsif_tail opt_else_stmt KEYWORD_end M_6
    | KEYWORD_while M_7 expr3 opt_do M_8 gen_stmts2 opt_terms KEYWORD_end M_9
    | KEYWORD_for VARIABLES KEYWORD_in for_range opt_do M_10 gen_stmts2 opt_terms KEYWORD_end M_11'''
    if(len(p)==2):
        p[0] = p[1]

def p_M_1(p):
    '''M_1 : '''
    label_name = ST.newlabel()
    TAC.emit("ifgoto", ["beq", p[-2]["place"], "0", label_name])
    p[0] = {"label": label_name}

def p_M_2(p):
    '''M_2 : '''
    label_name = ST.newlabel()
    TAC.emit("goto", [label_name])
    TAC.emit("label", [p[-3]["label"]])
    p[0] = {"label": label_name}

def p_M_6(p):
    '''M_6 : '''
    TAC.emit("label",[p[-4]["label"]])
    for label in p[-3]:
        TAC.emit("label",[label])

def p_M_7(p):
    '''M_7 : '''
    label_name = ST.newlabel()
    TAC.emit("label",[label_name])
    p[0] = {"label" : label_name}

def p_M_8(p):
    '''M_8 : '''
    label_name = ST.newlabel()
    TAC.emit("ifgoto", ["beq", p[-2]["place"], "0", label_name])
    p[0] = {"label": label_name}

def p_M_9(p):
    '''M_9 : '''

    TAC.emit("goto", [p[-7]["label"]])
    TAC.emit("label", [p[-4]["label"]])
    for i in p[-3]:
        TAC.emit("label", [i])

def p_M_10(p):
    '''M_10 : '''
    temp_name = ST.newtemp({})
    TAC.emit("Assignment", [temp_name, p[-2][0]])
    label_name = ST.newlabel()
    TAC.emit("label", [label_name])
    p[0] = {"label1": label_name, "iter": temp_name}
    label_name2 = ST.newlabel()
    TAC.emit("ifgoto", ["ble", temp_name, p[-2][1], label_name2])
    ST.varinsert(p[-4], {"type":"int", "declare": True})
    TAC.emit("Assignment", [p[-4], temp_name])
    p[0]["label2"] = label_name2

def p_M_11(p):
    '''M_11 : '''
    TAC.emit("Arithmetic", ["+", p[-4]["iter"], p[-4]["iter"], "1"])
    TAC.emit("goto", [p[-4]["label1"]])
    TAC.emit("label", [p[-4]["label2"]])
    TAC.emit("Assignment", [p[-8], p[-4]["iter"]])
    if(isinstance(p[-3],list)):
        for i in p[-3]:
            TAC.emit("label", [i])

def p_gen_stmts(p):
    '''gen_stmts : top_stmt
				| gen_stmts terms top_stmt
				| none
                '''
    if(len(p)==2):
        if(isinstance(p[1],dict)):
            if ("loop" in p[1].keys()):
                print ('ERROR: break statement out of loop')
                TAC.error = True
    if(len(p)==4):
        if(isinstance(p[3],dict)):
            if ("loop" in p[3].keys()):
                print ('ERROR: break statement out of loop')
                TAC.error = True

def p_gen_stmts2(p):
    '''gen_stmts2 : top_stmt
			| gen_stmts2 terms top_stmt
			| none
            '''
    if(len(p)==2):
        if(isinstance(p[1],dict)):
            if ("loop" in p[1].keys()):
                p[0] = [p[1]["looplabel"]]
            else:
                p[0] = []
        else:
            p[0] = []

    if(len(p)==4):
        if(isinstance(p[3],dict)):
            if ("loop" in p[3].keys()):
                p[1].append(p[3]["looplabel"])
                p[0] = p[1]
            else:
                p[0] = p[1]
        else:
            p[0] = p[1]

def p_stmt(p):
    '''stmt : expr
			| expr1
			| puts_stmt
			| loop_stmt
			| exit_stmt
			| func_call_stmt'''
    if (p[1]== "break"):
        label_name = ST.newlabel()
        TAC.emit("goto", [label_name])
        p[0] = {"loop":1, "looplabel": label_name, "allowed": 0}

def p_opt_else_stmt(p):
	'''opt_else_stmt : KEYWORD_else gen_stmts opt_terms
					 | none
	'''

def p_elsif_tail(p):
    '''elsif_tail :  none
                    | KEYWORD_elsif expr3 opt_then M_3 gen_stmts opt_terms M_4 elsif_tail
    '''
    if(len(p)!=2):
        p[8].append(p[7]["label"])
        p[0]= p[8]
    else:
        p[0] = []

def p_M_3(p):
    '''M_3 : '''
    label_name = ST.newlabel()
    TAC.emit("ifgoto", ["beq", p[-2]["place"], "0", label_name])
    p[0] = {"label": label_name}

def p_M_4(p):
    '''M_4 : '''
    label_name = ST.newlabel()
    TAC.emit("goto", [label_name])
    TAC.emit("label", [p[-3]["label"]])
    p[0] = {"label": label_name}

def p_opt_then(p):
	'''opt_then : KEYWORD_then
				| newline
	'''

def p_opt_do(p):
	'''opt_do : KEYWORD_do
				| newline
	'''

def p_for_range(p):
    '''for_range : for_range_variables DOUBLEDOT for_range_variables
    '''
    p[0] = [p[1],p[3]]

def p_for_range_variables(p):
    ''' for_range_variables : INT_CONSTANTS
                            | VARIABLES
                            | CONSTANTS
    '''
    if(strType(p[1]) != "int"):
        var_dict = ST.varlookup(p[1])
        if (var_dict["declare"] == False):
            var_dict = globalST.varlookup(p[1])
            if (var_dict["declare"] == False):
                print("DECLARATION ERROR: variable", p[1], 'not declared.')
                TAC.error = True
        if (var_dict["type"] != "int"):
            print(p[1], 'not int type.')
    p[0] = p[1]

def p_expr(p):
    '''expr :   mlhs EQUAL mrhs
    '''
    if (p[3]["type"] == "string"):
        print("TYPE ERROR: variable",p[3], 'string cannot be equated to variable.')
    if(p[1]["type"] == "int" and p[3]["type"] != "int"):
        print("TYPE ERROR: variable", p[1],'and',p[3], 'not matching type.')
    vardict = ST.varlookup(p[1]["place"])
    if (vardict == False):
        if(p[1]["type"] != "int"):
            globalST.update(p[1]["place"], "type", p[3]["type"])
    else:
        if(p[1]["type"] != "int"):
            ST.update(p[1]["place"], "type", p[3]["type"])
    if(p[3]["type"] == "stringc"):
        if (vardict == False):
            globalST.update(p[1]["place"], "type", "string")
        else:
            ST.update(p[1]["place"], "type", "string")
    TAC.emit('Assignment', [p[1]["place"], p[3]["place"]])
    p[0] = p[1]

def p_mlhs(p):
    '''mlhs : VARIABLES
    		| CONSTANTS
    		| array
    '''
    if(isinstance(p[1],dict)):
        p[0] = p[1]
    else:
        var_dict = ST.varlookup(p[1])
        if(var_dict == False):
            var_dict = globalST.varlookup(p[1])
            if (var_dict == False):
                ST.varinsert(p[1], {"type":"undefined", "declare": True})
                var_dict = {"type":"undefined", "declare": True}

        p[0] = {"place":p[1], "type": var_dict["type"]}

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
		    temp_name = ST.newtemp({"type":"int"})
		    TAC.emit('Assignment', [temp_name, "scan"])
		    p[0] = {"place": temp_name, "type": "int"}
		else:
		    p[0] = p[1]
	elif (len(p) == 3):
		temp_name = ST.newtemp({"type" : "array"})
		TAC.emit('Assignment', [temp_name, "[]"])
		p[0] = {"place": temp_name, "type": "array"}

def p_str_expr(p):
	'''str_expr : STRING_CONSTANTS
	'''
	# temp_name = ST.newtemp({"type" : "string"})
	# TAC.emit('Assignment', [temp_name, p[1]])
	p[0] = {"place": p[1], "type": "stringc"}


def p_expr1(p):
	'''expr1 : expr3
	'''
	p[0] = p[1]

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
		TAC.emit('logical', ['|',temp_name, p[1]["place"], p[3]["place"]])
		TAC.emit('ifgoto',["bne",temp_name,'0',label_name])
		TAC.emit('Assignment', [temp_name, '0'])
		TAC.emit('goto', [label_name2])
		TAC.emit('label',[label_name])
		TAC.emit('Assignment', [temp_name, '1'])
		TAC.emit('label', [label_name2])
		p[0] = {"place": temp_name, "type": "bool"}

def p_expr4(p):
	'''expr4 : expr4 LOGICALAND expr5
			 | expr5
	'''
	if (len(p)==2):
		p[0] = {"place": p[1]["place"], "type": p[1]["type"]}
	else:
        # if(p[1]["type"] != "bool" and p[3]["type"] != "bool"):
        #     print("TYPE ERROR: variable", p[1],'and',p[3] 'not matching type.')
		temp_name = ST.newtemp({"type" : "bool"})
		label_name = ST.newlabel()
		label_name2 = ST.newlabel()
		TAC.emit('logical', ['&',temp_name, p[1]["place"], p[3]["place"]])
		TAC.emit('ifgoto',["bne",temp_name,'0',label_name])
		TAC.emit('Assignment', [temp_name, '0'])
		TAC.emit('goto', [label_name2])
		TAC.emit('label',[label_name])
		TAC.emit('Assignment', [temp_name, '1'])
		TAC.emit('label', [label_name2])
		p[0] = {"place": temp_name, "type": "bool"}

def p_expr5(p):
	'''expr5 : expr6 DOUBLEEQUAL expr6
			 | expr6 NOTEQUAL expr6
			 | expr6
	'''
	if (len(p)==2):
		p[0] = {"place": p[1]["place"], "type": p[1]["type"]}
	else:
		if(p[1]["type"] != p[3]["type"]):
			print("TYPE ERROR: variable", p[1],'and',p[3], 'not matching type.')
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
		if(p[1]["type"] != "int" or p[3]["type"] != "int"):
			print("TYPE ERROR: variable", p[1],'and',p[3], 'not matching type.')
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

def p_expr7(p):
	'''expr7 : expr7 BITXOR expr8
		| expr7 PIPE expr8
		| expr8
	'''
	if (len(p)==2):
		p[0] = {"place": p[1]["place"], "type": p[1]["type"]}
	else:
		if(p[1]["type"] != "int" or p[3]["type"] != "int"):
			print("TYPE ERROR: variable", p[1],'and',p[3], 'not matching type.')
		temp_name = ST.newtemp({"type" : "int"})
		TAC.emit('logical',[p[2],temp_name,p[1]["place"],p[3]["place"]])
		p[0] = {"place": temp_name, "type": p[1]["type"]}

def p_expr8(p):
	'''expr8 : expr8 BITAND expr9
		| expr9
	'''
	if (len(p)==2):
		p[0] = {"place": p[1]["place"], "type": p[1]["type"]}
	else:
		if(p[1]["type"] != "int" or p[3]["type"] != "int"):
			print("TYPE ERROR: variable", p[1],'and',p[3], 'not matching type.')
		temp_name = ST.newtemp({"type" : "int"})
		TAC.emit('logical',[p[2],temp_name,p[1]["place"],p[3]["place"]])
		p[0] = {"place": temp_name, "type": p[1]["type"]}

def p_expr9(p):
	'''expr9 : expr9 SHIFTL expr10
		| expr9 SHIFTR expr10
		| expr10
	'''
	if (len(p)==2):
		p[0] = {"place": p[1]["place"], "type": p[1]["type"]}
	else:
		if(p[1]["type"] != "int" or p[3]["type"] != "int"):
			print("TYPE ERROR: variable", p[1],'and',p[3], 'not matching type.')
		temp_name = ST.newtemp({"type" : "int"})
		TAC.emit('logical',[p[2],temp_name,p[1]["place"],p[3]["place"]])
		p[0] = {"place": temp_name, "type": p[1]["type"]}

def p_expr10(p):
	'''expr10 : expr10 PLUS expr11
		| expr10 MINUS expr11
		| expr11
	'''
	if (len(p)==2):
		p[0] = {"place": p[1]["place"], "type": p[1]["type"]}
	else:
		if(p[1]["type"] != "int" or p[3]["type"] != "int"):
			print("TYPE ERROR: variable", p[1],'and',p[3], 'not matching type.')
		temp_name = ST.newtemp({"type" : "int"})
		TAC.emit('Arithmetic',[p[2],temp_name,p[1]["place"],p[3]["place"]])
		p[0] = {"place": temp_name, "type": p[1]["type"]}

def p_expr11(p):
	'''expr11 : expr11 MULTIPLY expr13
		| expr11 DIV expr13
		| expr11 MOD expr13
		| expr13
	'''
	if (len(p)==2):
		p[0] = {"place": p[1]["place"], "type": p[1]["type"]}
	else:
		if(p[1]["type"] != "int" or p[3]["type"] != "int"):
			print("TYPE ERROR: variable", p[1],'and',p[3], 'not matching type.')
		temp_name = ST.newtemp({"type" : "int"})
		TAC.emit('Arithmetic',[p[2],temp_name,p[1]["place"],p[3]["place"]])
		p[0] = {"place": temp_name, "type": p[1]["type"]}

def p_expr13(p):
    '''expr13 : OPEN_PAREN expr1 CLOSE_PAREN
    		  | uexpr INT_CONSTANTS
    		  | CONSTANTS
    		  | VARIABLES
    		  | array
    '''
    if(len(p)==2):
        if (isinstance(p[1],dict)):   ## ARRAY
            temp_name = ST.newtemp({})
            TAC.emit('Assignment', [temp_name, p[1]["place"]])
            p[0] = {"type":p[1]["type"], "place":temp_name}
        else:              ## constants, variables
            var_dict = ST.varlookup(p[1])
            if (var_dict == False):
                var_dict = globalST.varlookup(p[1])
                if (var_dict == False):
                    print("DECLARATION ERROR: variable", p[1], 'not declared.')
                    TAC.error = True
            # if(var_dict["type"] != "int"):
            #     print("TYPE ERROR: variable", p[1], 'not matching type.')
            if(var_dict["type"] != "string"):
                temp_name = ST.newtemp({})
                TAC.emit('Assignment', [temp_name, p[1]])
                p[0] = {"place": temp_name, "type": var_dict["type"]}
                ST.update(temp_name, "type", var_dict["type"])
            else:
                p[0] = {"place":p[1], "type":"string"}
    elif (len(p)==3):
    	temp_name = ST.newtemp({})
    	TAC.emit('Assignment', [temp_name, p[1]+p[2]])
    	if (strType(p[2])=="int"):
    		ST.update(temp_name,"type","int")
    		p[0] = {"place": temp_name, "type": "int"}
    	# if (strType(p[2])=="float"):
    	# 	ST.update(temp_name,"type","float")
    	# 	p[0] = {"place": temp_name, "type": "float"}
    elif (len(p)==4):
    	p[0] = {"place": p[2]["place"], "type": p[2]["type"]}

def p_array(p):
    '''array : VARIABLES OPEN_BRACKET expr7 CLOSE_BRACKET
    '''
    var_dict = ST.varlookup(p[1])
    if(var_dict["declare"]==False):
        var_dict = globalST.varlookup(p[1])
        if (var_dict["declare"] == False):
            print("DECLARATION ERROR: variable", p[1], 'not declared.')
            TAC.error = True
        elif(var_dict["type"] != "array"):
            print(p[1], 'is not array type.')
    elif(var_dict["type"] != "array"):
        print(p[1], 'is not array type.')
    # temp_name = ST.newtemp({"type" : "none"})
    # TAC.emit('Assignment', [temp_name, p[1]+p[2]+p[3]["place"]+p[4]])
    p[0] = {"place": p[1]+'['+p[3]["place"]+']', "type": "int"}

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
		p[0]=p[1]

def p_opt_terms(p):
	'''opt_terms : none
	   | terms
	'''

def p_terms(p):
	'''terms : term
		| terms term
	'''

def p_term(p):
	'''term : DELIM
			| newline
	'''

def p_none(p):
	'''none :
	'''
	p[0] = ""

no_special_reg = 0
globalST = st.Symtable("global")

localST = st.Symtable("local")

ST = globalST

myfile = open(filename,'r')
inputArray = myfile.readlines()
myfile.close()
ldata = ""
for i in range(0,len(inputArray)):
	ldata = ldata + inputArray[i]

lexer.Lexer.input(ldata)

# while True:
# 	found = 0
# 	tok = lexer.Lexer.token()
# 	if not tok:
# 		break
# 	# print tok.value
# 	if tok.type == 'VARIABLES':
# 		if not(tok.value in ST.vardict.keys()):
# 			ST.vardict[tok.value]= {"type":"none", "declare" : False}

# print ST.vardict
yacc.yacc()
pdata = ""
myfile = open(filename,'r')
for line in myfile.readlines():
	if line!='\n':
		pdata = pdata + line

TAC = tac.TAC()

result = yacc.parse(pdata)
print "global symboltable";
print ST.vardict
print ST.funcdict
if (TAC.error == False):
    TAC.printTAC()

# printRightDeriv(result)
