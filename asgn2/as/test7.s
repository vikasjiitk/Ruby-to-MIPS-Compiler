.data
a1: .word 0
c1: .word 0
b1: .word 0
d1: .word 0
.text
main: 
L1: 
addi $t2,$0,2
sw $t2,a1
L2: 
addi $t2,$0,1
sw $t2,b1
L3: 
lw $t2,a1
add $t2,$t2,$t2
L4: 
sw $t2,a1
lw $t2,a1
addi $t1,$0,5
ble $t2,$t1,L2
sw $t2,a1
L5: 
lw $t2,a1
sub $t2,$t2,$t2
L6: 
sw $t2,a1
lw $t2,a1
addi $t1,$0,1
bge $t2,$t1,L5
sw $t2,a1
L7: 
jal foo
move $t2,$v1
sw $t2,c1
L8: 
jal foo1
move $t2,$v1
sw $t2,d1
L9: 
li $v0, 10
syscall
foo: 
L11: 
li $v0, 1
lw $t2,a1
move $a0, $t2
syscall
sw $t2,a1
L12: 
addi $t2,$0,1
move $v1, $t2
jr $ra
foo1: 
L14: 
li $v0, 1
lw $t2,b1
move $a0, $t2
syscall
sw $t2,b1
L15: 
addi $t2,$0,1
move $v1, $t2
jr $ra
