.data
a: .word 0
leq: .word 0
c: .word 0
belikejanish: .word 0
.text
main: 
L1: 
addi $t2,$0,2
sw $t2,a
L2: 
addi $t2,$0,1
L3: 
lw $t1,a
add $t1,$t1,$t2
sw $t1,a
sw $t2,belikejanish
L4: 
lw $t2,leq
bgtz $t2,L4
sw $t2,leq
L5: 
jal foo
move $t2,$v1
sw $t2,c
foo: 
L7: 
li $v0, 1
lw $t2,a
move $a0, $t2
syscall
L8: 
li $v0, 10
syscall
L9: 
jr $ra
sw $t2,a
