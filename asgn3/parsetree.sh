echo "
<HTML>
<BODY> " > output.html
python rightderiv.py > output.txt
tac output.txt >> output.html
echo "
</BODY>
</HTML>
" >> output.html
