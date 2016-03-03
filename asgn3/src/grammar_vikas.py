def p_program(p):
    'PROGRAM    :   COMPSTMT'

def p_t(p):
    'T : DELIM | "\n"'

def p_compstmt(p):
    'COMPSTMT : STMT {T EXPR} [T]'

def p_stmt(p):
    '''STMT		: CALL KEYWORD_do [PIPE [BLOCK_VAR] PIPE] COMPSTMT end
                | KEYWORD_undef FNAME
                | KEYWORD_alias FNAME FNAME
                | STMT KEYWORD_if EXPR
                | STMT KEYWORD_while EXPR
                | STMT KEYWORD_unless EXPR
                | STMT KEYWORD_until EXPR
                | KEYWORD_BEGIN BLOCK_BEGIN COMPSTMT BLOCK_END
                | KEYWORD_END BLOCK_BEGIN COMPSTMT BLOCK_END
                | LHS EQUAL COMMAND [KEYWORD_do [PIPE [BLOCK_VAR] PIPE] COMPSTMT KEYWORD_end]
                | EXPR'''

def p_expr(p):
    '''EXPR		: MLHS EQUAL MRHS
        		| KEYWORD_return CALL_ARGS
        		| KEYWORD_yield CALL_ARGS
        		| EXPR KEYWORD_and EXPR
        		| EXPR KEYWORD_or EXPR
        		| KEYWORD_not EXPR
        		| COMMAND
        		| BITNOT COMMAND
        		| ARG'''

def p_call(p):
    '''CALL		: FUNCTION
                | COMMAND'''

def p_command(p):
    '''COMMAND		: OPERATION CALL_ARGS
            		| PRIMARY DOT OPERATION CALL_ARGS
            		| PRIMARY DOUBLE_COLON OPERATION CALL_ARGS
            		| KEYWORD_super CALL_ARGS'''

def p_function(p):
    '''FUNCTION     : OPERATION [OPEN_PARAN [CALL_ARGS] CLOSE_PARAN]
                    | PRIMARY DOT OPERATION OPEN_PARAN [CALL_ARGS] CLOSE_PARAN
                    | PRIMARY DOUBLE_COLON OPERATION OPEN_PARAN [CALL_ARGS] CLOSE_PARAN
                    | PRIMARY DOT OPERATION
                    | PRIMARY DOUBLE_COLON OPERATION
                    | KEYWORD_super OPEN_PARAN [CALL_ARGS] CLOSE_PARAN
                    | KEYWORD_super'''
