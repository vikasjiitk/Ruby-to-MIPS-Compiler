program		: top_compstmt
		;

top_compstmt	: top_stmts opt_terms
		;

top_stmts	: none
		| top_stmt
		| top_stmts terms top_stmt
		;

top_stmt	: stmt
		| KEYWORD_BEGIN
		  '{' top_compstmt '}'
		;

opt_terms	: none
		| terms
		;

terms		: term
		| terms ';'
		;

term		: ';'

none		:
		;

op		: '|'
		| '^'
		| '&'
		| tCMP
		| tEQ
		| tEQQ
		| tMATCH
		| tNMATCH
		| '>'
		| tGEQ
		| '<'
		| tLEQ
		| tNEQ
		| tLSHFT
		| tRSHFT
		| '+'
		| '-'
		| '*'
		| tSTAR
		| '/'
		| '%'
		| tPOW
		| tDSTAR
		| '!'
		| '~'
		| tUPLUS
		| tUMINUS
		| tAREF
		| tASET
		| '`'
		;
op		: PIPE
		| BITXOR
		| BITAND
		| tCMP		!
		| EQUAL
		| DOUBLEEQUAL
		| tMATCH	!
		| tNMATCH	!
		| GREATER
		| GREATEREQUAL
		| LESS
		| LESSEQUAL
		| NOTEQUAL
		| SHIFTL
		| SHIFTR
		| PLUS
		| MINUS
		| MULTIPLY
		| tSTAR	    !
		| DIV
		| MOD
		| tPOW		!
		| DOUBLESTAR
		| BITNOT
		| BITCOMP
		| tUPLUS	!
		| tUMINUS	!
		| tAREF		!
		| tASET		!
		| '`'		!
		;

reswords	: KEYWORD__LINE__ | KEYWORD__FILE__ | KEYWORD__ENCODING__
		| KEYWORD_BEGIN | KEYWORD_END
		| KEYWORD_alias | KEYWORD_and | KEYWORD_begin
		| KEYWORD_break | KEYWORD_case | KEYWORD_class | KEYWORD_def
		| KEYWORD_definedQ | KEYWORD_do | KEYWORD_else | KEYWORD_elsif
		| KEYWORD_end | KEYWORD_ensure | KEYWORD_false
		| KEYWORD_for | KEYWORD_in | KEYWORD_module | KEYWORD_next
		| KEYWORD_nil | KEYWORD_not | KEYWORD_or | KEYWORD_redo
		| KEYWORD_rescue | KEYWORD_retry | KEYWORD_return | KEYWORD_self
		| KEYWORD_super | KEYWORD_then | KEYWORD_true | KEYWORD_undef
		| KEYWORD_when | KEYWORD_yield | KEYWORD_if | KEYWORD_unless
		| KEYWORD_while | KEYWORD_until
		;
		
stmt	: expr

EXPR		: MLHS EQUAL MRHS
			| KEYWORD_return CALL_ARGS
			| KEYWORD_yield CALL_ARGS
			| EXPR KEYWORD_and EXPR
			| EXPR KEYWORD_or EXPR
			| KEYWORD_not EXPR
			| COMMAND
			| BITNOT COMMAND
			| ARG
