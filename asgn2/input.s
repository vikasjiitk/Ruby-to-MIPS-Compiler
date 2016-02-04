.data
a: .word 0
c: .word 0
d: .word 0
.text
main: 
L0: 
lw $s7,a
addi $s7,$0,2
sw $s7,a
L1: 
lw $s7,d
addi $s7,$0,7
L2: 
lw $s6,a
add $s6,$s6,$s7
sw $s7,d
L3: 
sw $s6,a
addi $s7,$0,50
ble $s6,$s7,L1
sw $s6,a
L4: 
lw $s7,c
addi $s7,$0,2
sw $s7,c
L5: 
jal foo
L6: 
jr $ra
foo: 
L8: 
li $v0, 1
lw $s7,a
move $a0, $s7
syscall
L9: 
jr $ra
sw $s7,a

