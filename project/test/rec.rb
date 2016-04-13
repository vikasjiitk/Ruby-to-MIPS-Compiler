array = []

def foo(a)
a = a-1
if a>=0 then
array[a] = a*a
foo(a)
end
end

a = 10
foo(a);
k=0
i=9
for k in k..i do
puts "Element number "
puts k
puts ": "
puts array[k]
puts "\n"
end
