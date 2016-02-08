.data
a1: .word 0
c1: .word 0
b1: .word 0
.text
main: 
L1: 
addi $s7,$0,2
sw $s7,a1
L2: 
addi $s7,$0,1
sw $s7,b1
L3: 
jal foo
move $s7,$v1
sw $s7,c1
L4: 
li $v0, 1
lw $s7,c1
move $a0, $s7
syscall
sw $s7,c1
L5: 
li $v0, 10
syscall
foo: 
L7: 
lw $s7,a1
lw $s6,b1
add $s7,$s7,$s6
sw $s6,b1
L8: 
move $v1, $s7
jr $ra
sw $s7,a1
