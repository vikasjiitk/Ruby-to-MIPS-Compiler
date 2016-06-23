a = []
stack = []
sp = 0
size = 0
def initializeArray()
  puts "Enter size of array (<100): "
  size = gets
  temp = size-1
  for i in 0..temp do
    puts "Enter number"
    temporary = i + 1
    puts temporary
    puts " : "
    a[i] = gets
  end
end

initializeArray()

def merge(min,mid,max)
  j = min
  m = mid + 1
  i = min
  tmp = []
  while( j<=mid && m<=max) do
    if a[j] <=a[m]
      tmp[i]=a[j]
      j = j+1
    else
      tmp[i] = a[m]
      m = m + 1    
    end
    i=i+1
  end
  if(j>mid) then
    for k in m..max do
      tmp[i] = a[k]
      i = i + 1
    end
  else
    for k in j..mid do
      tmp[i] = a[k]
      i = i+1
    end
  end
  for k in min..max do
    a[k] = tmp[k]
  end
end

def part(min,max)
  if (min < max) then
    mid = (min + max )/2;
    t2 = mid +  1
    stack[sp] = min
    stack[sp+1] = max  
    stack[sp+2] = mid
    stack[sp+3] = t2
    sp = sp+4
    part(min,mid)
    min = stack[sp-4]
    max = stack[sp-3]
    mid = stack[sp-2]
    t2 = stack[sp-1]    
    part(t2,max)
    min = stack[sp-4]
    max = stack[sp-3]
    mid = stack[sp-2]
    t2 = stack[sp-1] 
    merge(min,mid,max)
    sp = sp - 4
  end
end


t1 = size - 1 
part(0,t1)
for i in 0..t1 do
  puts a[i]
  puts " "
end
