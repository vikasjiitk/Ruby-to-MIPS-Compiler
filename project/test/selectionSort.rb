a = []
min = 0 
array_size = 10
t1 = array_size - 2
t3 = array_size - 1
def initializeArray()
  a[0] = 9
  a[1] = 5
  a[2] = 3
  a[3] = 7
  a[4] = 8
  a[5] = 1
  a[6] = 6
  a[7] = 2
  a[8] = 4
  a[9] = 0  
end

def findMinRemArray(index1,index2)  
  for j in index1..index2 do
    temp2 = a[min]  
    if (a[j] < temp2) then
      min = j
    end
  end 
end

initializeArray()

for i in 0..t1 do
  min = i
  t2  = i + 1
  findMinRemArray(t2,t3)
  temp = a[i]
  temp1 = a[min]
  a[i] = temp1
  a[min] = temp
end
puts "The sorted array is : \n"
for i in 0..t3 do 
  puts a[i]
  puts " "
end