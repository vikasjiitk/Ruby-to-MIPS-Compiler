.data
a1: .word 0
b1: .word 0
.text
main: 
L1: 
addi $t2,$0,2
sw $t2,a1
L2: 
addi $t2,$0,1
L3: 
lw $t1,a1
add $t1,$t1,$t2
sw $t2,b1
L4: 
sw $t1,a1
lw $t1,a1
addi $t2,$0,4
ble $t1,$t2,L2
sw $t1,a1
L5: 
li $v0, 1
lw $t2,a1
move $a0, $t2
syscall
L6: 
li $v0, 10
syscall
sw $t2,a1
