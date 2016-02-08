.data
a1: .word 0
c1: .word 0
b1: .word 0
.text
main: 
L1: 
li $v0,5
syscall
move $s7, $v0
L2: 
li $v0,5
syscall
move $s6, $v0
L3: 
add $s5,$s7,$s6
sw $s7,a1
sw $s6,b1
L4: 
li $v0, 1
move $a0, $s5
syscall
sw $s5,c1
L5: 
li $v0, 10
syscall
