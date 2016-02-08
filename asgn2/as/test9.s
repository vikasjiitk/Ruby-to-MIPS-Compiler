.data
f1: .word 0
g1: .word 0
i1: .word 0
h1: .word 0
j1: .word 0
a1: .word 0
b1: .word 0
c1: .word 0
e1: .word 0
d1: .word 0
.text
main: 
L1: 
addi $s7,$0,2
L2: 
addi $s6,$0,1
L3: 
addi $s5,$0,1
L4: 
addi $s4,$0,1
L5: 
addi $s3,$0,1
sw $s3,e1
L6: 
addi $s3,$0,1
L7: 
addi $s2,$0,1
sw $s2,g1
L8: 
addi $s2,$0,1
sw $s2,h1
L9: 
add $s6,$s7,$s6
L10: 
add $s5,$s7,$s5
L11: 
add $s2,$s5,$s4
sw $s5,c1
sw $s4,d1
L12: 
add $s4,$s3,$s2
sw $s2,e1
L13: 
add $s2,$s4,$s7
sw $s2,h1
L14: 
mult $s7,$s7
mflo $s7
L15: 
sub $s7,$s7,$s6
L16: 
add $s2,$s3,$s4
sw $s3,f1
sw $s4,g1
sw $s2,h1
L17: 
add $s7,$s7,$s6
sw $s7,a1
sw $s6,b1
L18: 
jal foo
move $s6,$v1
sw $s6,i1
L19: 
jal foo1
move $s7,$v1
sw $s7,j1
L20: 
li $v0, 10
syscall
foo: 
L22: 
li $v0, 1
lw $s7,a1
move $a0, $s7
syscall
sw $s7,a1
L23: 
addi $s7,$0,1
move $v1, $s7
jr $ra
foo1: 
L25: 
li $v0, 1
lw $s7,b1
move $a0, $s7
syscall
sw $s7,b1
L26: 
addi $s7,$0,1
move $v1, $s7
jr $ra
