def square(j)
s = j*j
return s
end

def add2square(i,a)
sq = square(i)
t = sq+a
return t;
end
puts "Adding and Squaring\n"
puts "Enter no. to be squared: "
i = gets
puts "Enter no. to be added "
a = gets
t = add2square(i,a);
puts t;
