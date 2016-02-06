.data
a: .word 0
.text
main: 
L1: 
jal foo
move $t2,$v1
sw $t2,a
L2: 
li $v0, 1
lw $t2,a
move $a0, $t2
syscall
L3: 
li $v0, 10
syscall
sw $t2,a
foo: 
L5: 
addi $t2,$0,2
move $v1, $t2
jr $ra
