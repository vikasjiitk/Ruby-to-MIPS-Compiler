.data
a1: .word 0
.text
main: 
L1: 
jal foo
move $t2,$v1
sw $t2,a1
L2: 
li $v0, 1
lw $t2,a1
move $a0, $t2
syscall
sw $t2,a1
L3: 
li $v0, 10
syscall
foo: 
L5: 
addi $t2,$0,2
move $v1, $t2
jr $ra
