.data
a: .word 0
c: .word 0
d: .word 0
.text
main: 
main: 
L1: 
lw $s7,a
addi $s7,$0,2
sw $s7,a
L2: 
lw $s7,d
addi $s7,$0,1
L3: 
lw $s6,a
add $s6,$s6,$s7
sw $s7,d
L4: 
sw $s6,a
lw $s6,a
addi $s7,$0,5
ble $s6,$s7,L2
sw $s6,a
L5: 
jal foo
lw $s7,c
move $s7,$v1
sw $s7,c
foo: 
L7: 
li $v0, 1
lw $s7,a
move $a0, $s7
syscall
L8: 
li $v0, 10
syscall
sw $s7,a
