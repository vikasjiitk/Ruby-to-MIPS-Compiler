.data
a: .word 0
c: .word 0
d: .word 0
.text
main: 
lw $s7,a
L0: addi $s7,$0,2
sw $s7,a
lw $s7,d
L1: addi $s7,$0,7
lw $s6,a
L2: add $s6,$s6,$s7
sw $s7,d
addi $s7,$0,50
L3: ble $s6,$s7,L2
sw $s6,a
lw $s7,c
L4: addi $s7,$0,2
sw $s7,c
L5: jal foo
li $v0,10
syscall
L6: jr $ra

foo: 
L8: li $v0, 1
lw $s7,a
move $a0, $s7
syscall
L9: jr $ra
sw $s7,a

