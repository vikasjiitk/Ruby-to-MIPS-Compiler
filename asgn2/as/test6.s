.data
a1: .word 0
c1: .word 0
b1: .word 0
.text
main: 
L1: 
addi $s7,$0,2
sw $s7,a1
L2: 
addi $s7,$0,1
L3: 
lw $s6,a1
add $s6,$s6,$s7
sw $s7,b1
L4: 
sw $s6,a1
lw $s6,a1
addi $s7,$0,5
ble $s6,$s7,L2
sw $s6,a1
L5: 
jal foo
move $s7,$v1
sw $s7,c1
L6: 
li $v0, 10
syscall
foo: 
L8: 
li $v0, 1
lw $s7,a1
move $a0, $s7
syscall
L9: 
move $v1, $s7
jr $ra
sw $s7,a1
