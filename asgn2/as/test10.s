.data
f1: .word 0
i1: .word 0
h1: .word 0
t1: .word 0
a1: .word 0
k1: .word 0
b1: .word 0
c1: .word 0
e1: .word 0
d1: .word 0
.text
main: 
L1: 
addi $s7,$0,2
L2: 
addi $s6,$0,3
L3: 
addi $s5,$0,3
L4: 
addi $s4,$0,4
L5: 
move $s3,$s7
L6: 
mult $s3,$s6
mflo $s3
sw $s3,e1
L7: 
add $s3,$s7,$s6
sw $s3,e1
L8: 
add $s3,$s7,$s4
sw $s3,f1
L9: 
add $s3,$s7,$s5
sw $s3,h1
L10: 
add $s3,$s6,$s4
sw $s3,i1
L11: 
mult $s7,$s5
mflo $s3
sw $s7,a1
sw $s5,c1
sw $s3,t1
L12: 
div $s6,$s4
mflo $s3
sw $s6,b1
sw $s4,d1
sw $s3,k1
L13: 
li $v0, 10
syscall
