.data
a1: .word 0
c1: .word 0
b1: .word 0
d1: .word 0
.text
main: 
L1: 
addi $s7,$0,4
L2: 
addi $s6,$0,5
L3: 
or $s5,$s7,$s6
L4: 
and $s4,$s7,$s6
sw $s7,a1
sw $s6,b1
L5: 
li $v0, 1
move $a0, $s5
syscall
sw $s5,c1
L6: 
li $v0, 1
move $a0, $s4
syscall
sw $s4,d1
L7: 
li $v0, 10
syscall
