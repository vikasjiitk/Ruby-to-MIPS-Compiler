.data
a1: .word 0
.text
main: 
L1: 
jal foo
move $s7,$v1
sw $s7,a1
L2: 
li $v0, 1
lw $s7,a1
move $a0, $s7
syscall
sw $s7,a1
L3: 
li $v0, 10
syscall
foo: 
L5: 
addi $s7,$0,2
move $v1, $s7
jr $ra
