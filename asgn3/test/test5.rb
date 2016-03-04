def sqr(x)
    return x*x
end

(rand(4) + 2).times {
    a = rand(300)
    print a,"^2 = ", sqr(a), "\n"
}
print "\n"

def boom
    print "Boom!\n"
end
boom
boom

print "\n"
def line(cnt, ender = "+", fill = "-")
    print ender, fill * cnt, ender, "\n"
end
line(8)
line(5,'*')
line(11,'+','=')

def incr(n)
    n = n + 1
end
a = 5
incr(a)
print a,"\n"
