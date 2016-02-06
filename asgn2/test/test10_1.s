.data
a: .word 0
c: .word 0
e: .word 0
d: .word 0
f: .word 0
i: .word 0
h: .word 0
k: .word 0
j: .word 0
belikejanish: .word 0
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
sw $s3,e
L7: 
add $s3,$s7,$s6
sw $s3,e
L8: 
add $s3,$s7,$s4
sw $s3,f
L9: 
add $s3,$s7,$s5
sw $s3,h
L10: 
add $s3,$s6,$s4
sw $s3,i
L11: 
mult $s7,$s5
mflo $s3
sw $s7,a
sw $s5,c
sw $s3,j
L12: 
div $s6,$s4
mflo $s3
sw $s6,belikejanish
sw $s4,d
sw $s3,k
L13: 
li $v0, 10
syscall
