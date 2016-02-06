.data
a: .word 0
.text
mail: 
L1: 
jal foo
move $t2,$v1
sw $t2,a
foo: 
L3: 
addi $t2,$0,2
move $v1, $t2
jr $ra
L4: 
li $v0, 1
lw $t2,a
move $a0, $t2
syscall
L5: 
jr $ra
sw $t2,a
