.data
a: .word 0
c: .word 0
belikejanish: .word 0
.text
main: 
L1: 
addi $t2,$0,2
sw $t2,a
L2: 
addi $t2,$0,1
sw $t2,belikejanish
L3: 
jal foo
move $t2,$v1
sw $t2,c
L4: 
li $v0, 1
lw $t2,c
move $a0, $t2
syscall
L5: 
li $v0, 10
syscall
sw $t2,c
foo: 
L7: 
lw $t2,a
lw $t1,belikejanish
add $t2,$t2,$t1
sw $t1,belikejanish
L8: 
move $v1, $t2
jr $ra
sw $t2,a
