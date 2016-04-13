i=3
def foo(a)
a = a-1
if i>=0 then
i = i-1
puts a
foo(a)
end
puts a
end
a = 1
foo(a);
