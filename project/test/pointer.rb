a = []
for i in 1..5 do
a[i]=i
end
b=a
for i in 6..10 do
b[i]=a[i]+i
end
for i in 1..10 do
puts b[i]
end
