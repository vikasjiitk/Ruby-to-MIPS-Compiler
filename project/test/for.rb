a = []
a[1]=9
for i in 0..10 do
a[i] = i*i
i = i+2
puts i
end
puts "Printing Squares:\n"
for i in 0..10 do
puts a[i]
puts " "
end
