res = 1
def fact(n)
if (n==1) then
return 0
end
res = res*n
t3=n-1
fact(t3)
return 0
end

puts "Enter value of n to compute n! : "
i = gets
fact(i)
puts res

