.data
a1: .word 0
b1: .word 0
.text
main: 
L1: 
addi $s7,$0,2
L2: 
addi $s6,$0,1
L3: 
add $s7,$s7,$s6
sw $s6,b1
L4: 
li $v0, 1
move $a0, $s7
syscall
sw $s7,a1
L5: 
li $v0, 10
syscall
