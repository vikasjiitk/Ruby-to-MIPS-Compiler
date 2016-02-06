.data
a1: .word 0
b1: .word 0
.text
main: 
L1: 
addi $t2,$0,4
L2: 
addi $t1,$0,5
add $t2,$t2,$t1
L3: 
move $t1,$t2
L4: 
mult $t2,$t1
mflo $t2
L5: 
li $v0, 1
move $a0, $t1
syscall
sw $t1,b1
L6: 
li $v0, 1
move $a0, $t2
syscall
sw $t2,a1
L7: 
li $v0, 10
syscall
