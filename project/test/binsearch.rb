a = []
b = 1
left = 0 
right = 9
for i in 0..9 do 
	a[i] = i + b
	b = b + i
end
for i in 0..9 do 
	puts a[i]
	puts " "
end
puts "Enter a number to search : "
number = gets
def binSearch(number)	
	flag = 1
	while ((left <= right) && flag ==1) do
		mid = (left + right)/2
		if (a[mid]==number)
			flag = 0
		elsif (a[mid] < number)
			left = mid + 1
		else
			right = mid - 1 
		end
	end
	if (a[mid]==number)
		puts "Number found"
	else
		puts "Number not found"
	end
end
binSearch(number)
