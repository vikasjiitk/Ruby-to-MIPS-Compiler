all:
	cp src/lexer.py bin/lexer.py
	cp src/parser.py bin/parser.py
	cp src/TAC.py bin/TAC.py
	cp src/symtable.py bin/symtable.py
	mv bin/parser.py bin/irgen
	chmod +x bin/irgen

clean:
	rm -rf bin/*
