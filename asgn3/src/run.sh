#!/bin/bash
echo "
<HTML>
<BODY> " > ${1:5:-3}.html
python bin/parser.py $1 > bin/rd.txt
tac bin/rd.txt >> ${1:5:-3}.html
echo "
</BODY>
</HTML>
" >> ${1:5:-3}.html
