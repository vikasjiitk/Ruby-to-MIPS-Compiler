puts "Enter a number to check if it is prime: "
num = gets


def prime(number)
	if number == 1 then
		puts "The number is not prime"
	elsif number == 2 then
		puts "The number is prime"
	else 
		temp = number/2
		flag = 1
		i=2
		while( i>=2 && i<=temp && flag == 1) do 
			if (number % i == 0)
				flag = 0
			end 
		  i = i+ 1
		end
		if flag == 0 
			puts "The number is not prime"
		else
			puts "The number is prime"
		end
	end
end

prime(num)