
# Function to evaluate a polynomial at x.  The polynomial is given
# as a list of coefficients, from the greatest to the least.
def polyval(x, coef)
    sum = 0
    coef = coef.clone		# Don't want to destroy the original
    while true
        sum += coef.shift	# Add and remove the next coef
        break if coef.empty?	# If no more, done entirely.
        sum *= x		# This happens the right number of times.
    end
    return sum
end

def readints(prompt)
    # Read a line
    print prompt
    line = readline.chomp
    raise EOFError.new if line == 'quit' # You can also use a real EOF.
            
    retval = [ ]
    for str in line.split(/\s+/)
	if str =~ /^\-?\d+$/
            retval.push(str.to_i)
	else
	    raise TypeError.new
	end
    end

    return retval
end

def term_to_str(coef, exp)
    ret = ""
    coef = coef.abs
    ret = coef.to_s     unless coef == 1 && exp > 0
    ret += "x" if exp > 0				# x if exponent not 0
    ret += "^" + exp.to_s if exp > 1			# ^exponent, if > 1.

    return ret
end

def polystr(p)
    exp = p.length
    p = (p.map { |c| exp -= 1; [ c, exp ] }).select { |p| p[0] != 0 }
    return "0" if p.empty?
    result = (if p[0][0] < 0 then "-" else "" end) + term_to_str(*p[0])
    for term in p[1...p.length]
	result += (if term[0] < 0 then " - " else " + " end) + 
		term_to_str(*term)
    end

    return result
end
        
begin
    while true
	print "\n"
        begin
            poly = readints("Enter a polynomial coefficients: ")
	rescue TypeError
            print "Try again.\n"
	    retry
	end
	break if poly.empty?

        while true
	    print "Enter x value or blank line: "
	    x = readline.chomp
	    break if x == ''
            raise EOFError.new if x == 'quit'

	    # If it looks bad, let's try again.
	    if x !~ /^\-?\d+$/
                print "That doesn't look like an integer.  Please try again.\n"
		next
	    end

	    # Convert to an integer and print the result.
	    x = x.to_i
            print "p(x) = ", polystr(poly), "\n"
            print "p(", x, ") = ", polyval(x, poly), "\n"
	end
    end
rescue EOFError
    print "\n=== EOF ===\n"
rescue Interrupt, SignalException
    print "\n=== Interrupted ===\n"
else
    print "--- Bye ---\n"
end
