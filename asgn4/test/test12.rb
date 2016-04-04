a= 4
n = 5
c = 121
def shuffle(arr)
    for n in 0..4
	if (c == 1000) 
		c = 1001
	else 
		c = 0
	end
    end
end
end
def pairs(a, b)
    a << b
    shuffle(b)
end

shuffle(a)
pairs(1,2)

