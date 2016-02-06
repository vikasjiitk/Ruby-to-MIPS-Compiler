.data
a: .word 0
.text
main: 
L1: 
jal foo
move $t2,$v1
sw $t2,a
foo: 
L3: 
li $v0, 10
syscall
L4: 
li $v0, 1
lw $t2,a
move $a0, $t2
syscall
L5: 
jr $ra
sw $t2,a
