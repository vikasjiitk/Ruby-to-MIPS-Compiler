.data
a1: .word 0
c1: .word 0
b1: .word 0
.text
main: 
L1: 
li $v0,5
syscall
move $t2, $v0
L2: 
li $v0,5
syscall
move $t1, $v0
sw $t1,b1
L3: 
lw $t1,c1
add $t1,$t1,$t2
sw $t2,a1
L4: 
li $v0, 1
move $a0, $t1
syscall
sw $t1,c1
L5: 
li $v0, 10
syscall
