#!/usr/bin/python
import ply.lex as lex
import sys
keywords = [
'KEYWORD_alias','KEYWORD_and','KEYWORD_BEGIN','KEYWORD_begin','KEYWORD_break','KEYWORD_case','KEYWORD_class','KEYWORD_def','KEYWORD_definedQ','KEYWORD_do',
'KEYWORD_else','KEYWORD_elsif','KEYWORD_END','KEYWORD_end','KEYWORD_ensure','KEYWORD_false','KEYWORD_for','KEYWORD_if','KEYWORD_in','KEYWORD_module','KEYWORD_next',
'KEYWORD_nil','KEYWORD_not','KEYWORD_or','KEYWORD_redo','KEYWORD_rescue','KEYWORD_retry','KEYWORD_return','KEYWORD_self','KEYWORD_super','KEYWORD_then',
'KEYWORD_true','KEYWORD_undef','KEYWORD_unless','KEYWORD_until','KEYWORD_when','KEYWORD_while','KEYWORD_yield','KEYWORD___ENCODING__','KEYWORD___END__',
'KEYWORD___FILE__','KEYWORD___LINE__','KEYWORD_puts', 'KEYWORD_gets', 'KEYWORD_exit', 'KEYWORD_new'
]

operators = [
	# +,-,*,/,%,&,|,^ ,!,~,=,**,<<,>>,==,===, !=, <=>, >=, >, <,<=,%=,/=,-=, +=,*=,**=,.,..,...,not,and,or,?:, &&, ||,&=,|=,^=,<<=,>>=,&&=,||=
    'PLUS', 'MINUS', 'MULTIPLY', 'DIV', 'MOD',
    'BITAND', 'PIPE', 'BITXOR', 'BITNOT', 'BITCOMP', 'EQUAL',
    'DOUBLESTAR' , 'SHIFTL', 'SHIFTR', 'DOUBLEEQUAL', 'TRIPLEEQUAL',
    'NOTEQUAL', 'IFF', 'GREATEREQUAL', 'GREATER', 'LESS',
    'LESSEQUAL', 'MODEQUAL', 'DIVEQUAL', 'MINUSEQUAL','PLUSEQUAL',
    'MULTIPLYEQUAL','DOUBLESTAREQUAL', 'DOT', 'DOUBLEDOT','TRIPLEDOT',
    'NOT','AND','OR','QUESTIONCOLON','LOGICALAND','LOGICALOR',
    'BITANDEQUAL', 'PIPEEQUAL', 'BITXOREQUAL', 'SHIFTLEQUAL', 'SHIFTREQUAL', 'LOGICALANDEQUAL', 'LOGICALOREQUAL'
]

delimiters=[
    # [,],{,},(,), , ,;,',",\n
    'OPEN_BRACKET','CLOSE_BRACKET','BLOCK_BEGIN','BLOCK_END',
    'OPEN_PAREN', 'CLOSE_PAREN','COMMA','DELIM','SQUOTES','DQUOTES','newline'
]

identifiers = [
    'CONSTANTS','VARIABLES','SIGIL_AT','SIGIL_DOUBLE_AT','SIGIL_DOLLAR'
]

constants = [
	'INT_CONSTANTS','FLOAT_CONSTANTS', 'STRING_CONSTANTS', 'CHAR_CONSTANTS', 'BOOLEAN_CONSTANTS'
]
symbols = [ # ?, \, $ , :, ::
	'QUESTION_MARK','BACK_SLASH','DOLLAR','COLON', 'DOUBLE_COLON'
]
tokens = keywords + operators + delimiters + identifiers + constants +symbols

# Operators
t_PLUS=r'\+'
t_MINUS=r'-'
t_MULTIPLY=r'\*'
t_DIV=r'/'
t_MOD=r'%'
t_BITAND=r'&'
t_PIPE=r'\|'
t_BITXOR=r'\^'
t_BITNOT=r'!'
t_BITCOMP=r'~'
t_EQUAL=r'='
t_DOUBLESTAR=r'\*\*'
t_SHIFTL=r'<<'
t_SHIFTR=r'>>'
t_DOUBLEEQUAL=r'=='
t_TRIPLEEQUAL=r'==='
t_NOTEQUAL=r'!='
t_IFF=r'<=>'
t_GREATEREQUAL=r'>='
t_GREATER=r'>'
t_LESS=r'<'
t_LESSEQUAL=r'<='
t_MODEQUAL=r'%='
t_DIVEQUAL=r'/='
t_MINUSEQUAL=r'-='
t_PLUSEQUAL=r'\+='
t_MULTIPLYEQUAL=r'\*='
t_DOUBLESTAREQUAL=r'\*\*='
t_DOT=r'\.'
t_DOUBLEDOT=r'\.\.'
t_TRIPLEDOT=r'\.\.\.'
t_NOT=r'not'
t_AND=r'and'
t_OR=r'or'
t_QUESTIONCOLON=r'\?:'
t_LOGICALAND=r'&&'
t_LOGICALOR=r'\|\|'
t_BITANDEQUAL=r'&='
t_PIPEEQUAL=r'\|='
t_BITXOREQUAL=r'\^='
t_SHIFTLEQUAL=r'<<='
t_SHIFTREQUAL=r'>>='
t_LOGICALANDEQUAL=r'&&='
t_LOGICALOREQUAL=r'\|\|='
#symbols
t_QUESTION_MARK=r'\?'
t_DOLLAR=r'\$'
t_BACK_SLASH=r'\\'
t_COLON=r':'
t_DOUBLE_COLON = r'::'
t_newline = r'[\n]+'
    
#keywords
    
reserved_map = { }
for r in keywords:
    reserved_map[ r[8:] ] = r

#identifiers

def t_CONSTANTS(t):
    r'[A-Z][\w_]*'
    t.type = reserved_map.get(t.value,"CONSTANTS")
    return t

def t_VARIABLES(t):
    r'[A-Za-z_][\w_]*'
    t.type = reserved_map.get(t.value,"VARIABLES")
    return t

def t_SIGIL_AT(t):
    r'@[A-Za-z_][\w_]*'
    t.type = reserved_map.get(t.value,"SIGIL_AT")
    return t

def t_SIGIL_DOUBLE_AT(t):
    r'@@[A-Za-z_][\w_]*'
    t.type = reserved_map.get(t.value,"SIGIL_DOUBLE_AT")
    return t

def t_SIGIL_DOLLAR(t):
    r'$[A-Za-z_][\w_]*'
    t.type = reserved_map.get(t.value,"SIGIL_DOLLAR")
    return t

#constants

t_INT_CONSTANTS = r'[0-9]+'
t_FLOAT_CONSTANTS = r'[0-9]+\.[0-9]+'
t_STRING_CONSTANTS = r'"([^\\\"]+|\\.)*"| \'([^\\\']+|\\.)*\''
t_CHAR_CONSTANTS = r"'.'"
t_BOOLEAN_CONSTANTS = r'TRUE|FALSE'

#delimeters
t_OPEN_BRACKET         = r'\['
t_CLOSE_BRACKET         = r'\]'
t_BLOCK_BEGIN           = r'\{'
t_BLOCK_END           = r'\}'
t_OPEN_PAREN           = r'\('
t_CLOSE_PAREN           = r'\)'
t_COMMA            = r','
t_DELIM             = r';'

#newline
# def t_newline(t):
#     r'\n+'
#     t.lexer.lineno += len(t.value)

# A string containing ignored characters (spaces and tabs)
t_ignore  = ' \t'

#comments

t_ignore_COMMENT = r'\#.* | =begin(.|\n)*=end'

# Error handling rule
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

# Build the lexer
lexer = lex.lex()

# # Test it out
# filename = sys.argv[1]
# f = open(filename,'r')
# inputArray = f.readlines()
# f.close()
# data = ""
# for i in range(0,len(inputArray)):
# 	data = data + inputArray[i]
# # Give the lexer some input
# lexer.input(data)
# # Tokenize
# output = []
# i = -1
# while True:
#     found = 0
#     tok = lexer.token()
#     if not tok:
#         break      # No more input
#     for i in range(0,len(output)):
# 	if output[i][0] == tok.type:
# 		output[i][1] = output[i][1] + 1
# 		output[i].append(tok.value)
# 		found = 1
# 		break
#     if i==len(output)-1 and not(found):
# 	output.append([tok.type,1,tok.value])
#     #print(tok)
# print "Token".ljust(25)+"Occurrences".ljust(15)+"Lexemes\n"
# for i in range(0,len(output)):
# 	print output[i][0].ljust(25) + str(output[i][1]).ljust(15) + output[i][2]
# 	if output[i][0] in (identifiers + constants):
# 		for j in range(3,len(output[i])):
# 			print "\t\t\t\t\t"+output[i][j]
