import ply.yacc as yacc

from test_lexer import tokens

def p_S(p):
    '''S    :   A B
    '''
    i = 1
    p[0] = ['S']
    while(i < len(p)):
        p[0].append(p[i])
        i = i+1

def p_A(p):
    '''A :  a A
    | B
    '''
    i = 1
    p[0] = ['A']
    while(i < len(p)):
        p[0].append(p[i])
        i = i+1
def p_B(p):
    '''     B : b B
            B :  A
            B : b
    '''
    i = 1
    p[0] = ['B']
    while(i < len(p)):
        p[0].append(p[i])
        i = i+1

yacc.yacc()

while True:
   try:
       s = raw_input('test > ')
   except EOFError:
       break
   if not s: continue
   result = yacc.parse(s)
   print(result)
