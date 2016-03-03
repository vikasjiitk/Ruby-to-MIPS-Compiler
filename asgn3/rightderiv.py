import types
body = ""
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
tree = ['program', ['top_compstmt', ['top_stmts', ['top_stmts', ['top_stmts', ['top_stmt', ['stmt', ['expr', ['mlhs', 'a'], '=', ['mrhs', ['expr1', ['expr2', ['expr3', ['expr4', ['expr5', ['expr6', ['expr7', ['expr8', ['expr9', ['expr10', ['expr11', ['expr12', ['expr13', ['uexpr', ['none']], '2']]]]]]]]]]]]]]]]]], ['terms', ['term', 'NEWLINE']], ['top_stmt', 'if', ['expr3', ['expr4', ['expr5', ['expr6', ['expr7', ['expr8', ['expr9', ['expr10', ['expr11', ['expr12', ['expr13', 'a']]]]]]]], '==', ['expr6', ['expr7', ['expr8', ['expr9', ['expr10', ['expr11', ['expr12', ['expr13', ['uexpr', ['none']], '2']]]]]]]]]]], ['opt_then', 'then'], ['top_compstmt', ['top_stmts', ['top_stmt', ['stmt', ['expr', ['mlhs', 'a'], '=', ['mrhs', ['expr1', ['expr2', ['expr3', ['expr4', ['expr5', ['expr6', ['expr7', ['expr8', ['expr9', ['expr10', ['expr11', ['expr12', ['expr13', ['uexpr', ['none']], '3']]]]]]]]]]]]]]]]]], ['opt_terms', ['terms', ['term', ';']]]], ['elsif_tail', ['none']], ['opt_else_stmt', ['none']], 'end']], ['terms', ['term', 'NEWLINE']], ['top_stmt', 'while', ['expr3', ['expr4', ['expr5', ['expr6', ['expr7', ['expr8', ['expr9', ['expr10', ['expr11', ['expr12', ['expr13', 'a']]]]]]], '>', ['expr7', ['expr8', ['expr9', ['expr10', ['expr11', ['expr12', ['expr13', ['uexpr', ['none']], '1']]]]]]]]]]], ['opt_do', 'do'], ['top_compstmt', ['top_stmts', ['top_stmt', ['stmt', ['expr', ['mlhs', 'a'], '=', ['mrhs', ['expr1', ['expr2', ['expr3', ['expr4', ['expr5', ['expr6', ['expr7', ['expr8', ['expr9', ['expr10', ['expr10', ['expr11', ['expr12', ['expr13', 'a']]]], '-', ['expr11', ['expr12', ['expr13', ['uexpr', ['none']], '1']]]]]]]]]]]]]]]]]], ['opt_terms', ['terms', ['term', ';']]]], 'end']], ['opt_terms', ['none']]]]

printRightDeriv(tree)
