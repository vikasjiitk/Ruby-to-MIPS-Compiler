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
addi $s7,$0,1
sw $s7,d
L2: 
lw $s7,a
lw $s6,d
add $s7,$s7,$s6
sw $s6,d
L3: 
sw $s7,a
lw $s7,a
addi $s6,$0,5
ble $s7,$s6,L2
sw $s7,a
L4: 
jal foo
lw $s7,c
move $s7,$v1
sw $s7,c
foo: 
L6: 
li $v0, 1
lw $s7,a
move $a0, $s7
syscall
L7: 
move $v1, $s7
jr $ra
sw $s7,a
