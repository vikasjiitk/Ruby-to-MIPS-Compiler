.data
i1: .word 0
D.17321: .word 0
j1: .word 0
sum1: .word 0
D.17361: .word 0
.text
main: 
L1: 
addi $s7,$0,1
sw $s7,j1
L2: 
addi $s7,$0,1
sw $s7,sum1
L3: 
addi $s7,$0,0
sw $s7,i1
L4: 
addi $s7,$0,1
sw $s7,j1
L5: 
addi $s7,$0,1
addi $s6,$0,2
ble $s7,$s6,L14
L6: 
lw $s7,j1
addi $s6,$0,10
div $s7,$s6
mfhi $s5
sw $s7,j1
L7: 
sw $s5,D.17321
lw $s5,D.17321
addi $s7,$0,0
beq $s5,$s7,L9
sw $s5,D.17321
L8: 
addi $s7,$0,1
addi $s6,$0,2
ble $s7,$s6,L11
L9: 
li $v0, 1
lw $s7,j1
move $a0, $s7
syscall
sw $s7,j1
L10: 
addi $s7,$0,1
addi $s6,$0,2
ble $s7,$s6,L12
L11: 
lw $s7,sum1
lw $s6,i1
add $s7,$s7,$s6
sw $s7,sum1
sw $s6,i1
L12: 
lw $s7,i1
addi $s6,$0,1
add $s7,$s7,$s6
L13: 
addi $s6,$0,2
mult $s7,$s6
mflo $s5
sw $s7,i1
sw $s5,j1
L14: 
lw $s7,i1
addi $s6,$0,99
ble $s7,$s6,L6
sw $s7,i1
L15: 
addi $s7,$0,1
addi $s6,$0,2
ble $s7,$s6,L16
L16: 
li $v0, 1
lw $s7,sum1
move $a0, $s7
syscall
sw $s7,sum1
L17: 
addi $s7,$0,0
L18: 
li $v0, 10
syscall
sw $s7,D.17361
