#!/bin/bash
echo "
<HTML>
<BODY> " > ${1:5:-3}.html
python bin/parser.py $1 > bin/rd.html
tac bin/rd.html >> ${1:5:-3}.html
echo "
</BODY>
</HTML>
" >> ${1:5:-3}.html
