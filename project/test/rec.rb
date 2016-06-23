array = []

def foo(a)
a = a-1
if a>=0 then
x = a+1
puts x
puts '\n'
foo(a)
puts x
puts '\n'
end
end
b = gets
foo(b);
k=0
i=9
#for k in k..i do
#puts "Element number "
#puts k
#puts ": "
#puts array[k]
#puts "\n"
#end
