#!/bin/bash
str = $1
echo "
<HTML>
<BODY> " > output.html
python parser.py 
python rightderiv.py > output.txt
tac output.txt >> output.html
echo "
</BODY>
</HTML>
" >> output.html
