.data
a1: .word 0
.text
main: 
L1: 
addi $s7,$0,-2
L2: 
li $v0, 1
move $a0, $s7
syscall
sw $s7,a1
L3: 
li $v0, 10
syscall
