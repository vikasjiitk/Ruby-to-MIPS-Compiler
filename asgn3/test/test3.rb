s = "Hi there.  How are you?"
print s.length, " [" + s + "]\n"

print s[4], "\n"
printf("%c\n", s[4])

print "[" + s[4,4] + "] [" + s[6..15] + "]\n"

print "Wow " * 3, "\n"

print s.index("there"), " ", s.index("How"), " ", s.index("bogus"), "\n"