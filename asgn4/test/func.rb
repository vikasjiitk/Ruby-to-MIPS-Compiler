def bar(j)
s = j*j
return s
end
def foo(i,a)
sq = bar(i)
t = sq + a
return t;
end
f = 6
i = foo(3,f);
puts i;
