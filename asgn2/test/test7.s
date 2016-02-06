.data
a: .word 0
c: .word 0
d: .word 0
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
sw $t2,belikejanish
L4: 
sw $t1,a
lw $t1,a
addi $t2,$0,5
ble $t1,$t2,L2
sw $t1,a
L5: 
lw $t2,a
lw $t1,belikejanish
sub $t2,$t2,$t1
sw $t1,belikejanish
L6: 
sw $t2,a
lw $t2,a
addi $t1,$0,1
bge $t2,$t1,L5
sw $t2,a
L7: 
jal foo
move $t2,$v1
sw $t2,c
L8: 
jal foo1
move $t2,$v1
sw $t2,d
L9: 
li $v0, 10
syscall
foo: 
L11: 
li $v0, 1
lw $t2,a
move $a0, $t2
syscall
L12: 
jr $ra
sw $t2,a
foo1: 
L14: 
li $v0, 1
lw $t2,belikejanish
move $a0, $t2
syscall
L15: 
jr $ra
sw $t2,belikejanish
