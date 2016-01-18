require("list")
require("tree")

print "=== List test ===\n"
x = List.new(10)
x.at_front(33)
x.pr(true)

s = 0
x.each { |n| s += n }
print "sum = ", s, "\n"

print "\n=== Tree test ===\n"
t = Tree.new(28)
t.insert(38)
t.insert(1)
t.pr(true)

s = 0
t.each { |n| s += n }
print "sum = ", s, "\n"

print "Max is ", t.max, "\n"
