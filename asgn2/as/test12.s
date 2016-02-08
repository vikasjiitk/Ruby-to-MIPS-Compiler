.data
a1: .word 0
b1: .word 0
.text
main: 
L1: 
addi $s7,$0,4
L2: 
addi $s6,$0,5
add $s7,$s7,$s6
L3: 
move $s6,$s7
L4: 
mult $s7,$s6
mflo $s7
L5: 
li $v0, 1
move $a0, $s6
syscall
sw $s6,b1
L6: 
li $v0, 1
move $a0, $s7
syscall
sw $s7,a1
L7: 
li $v0, 10
syscall
