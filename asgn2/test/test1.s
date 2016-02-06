.data
a1: .word 0
.text
main: 
L1: 
addi $t2,$0,2
L2: 
li $v0, 1
move $a0, $t2
syscall
L3: 
li $v0, 10
syscall
sw $t2,a1
