.data
i1: .word 0
k1: .word 0
res1: .word 0
j1: .word 0
.text
main: 
L1: 
addi $s7,$0,0
sw $s7,res1
L2: 
addi $s7,$0,0
sw $s7,i1
L3: 
addi $s7,$0,1
addi $s6,$0,2
ble $s7,$s6,L16
L4: 
addi $s7,$0,0
sw $s7,j1
L5: 
addi $s7,$0,1
addi $s6,$0,2
ble $s7,$s6,L13
L6: 
addi $s7,$0,0
sw $s7,k1
L7: 
addi $s7,$0,1
addi $s6,$0,2
ble $s7,$s6,L10
L8: 
lw $s7,res1
addi $s6,$0,1
add $s7,$s7,$s6
sw $s7,res1
L9: 
lw $s7,k1
addi $s6,$0,1
add $s7,$s7,$s6
sw $s7,k1
L10: 
lw $s7,k1
addi $s6,$0,9
ble $s7,$s6,L8
sw $s7,k1
L11: 
addi $s7,$0,1
addi $s6,$0,2
ble $s7,$s6,L12
L12: 
lw $s7,j1
addi $s6,$0,1
add $s7,$s7,$s6
sw $s7,j1
L13: 
lw $s7,j1
addi $s6,$0,9
ble $s7,$s6,L6
sw $s7,j1
L14: 
addi $s7,$0,1
addi $s6,$0,9
ble $s7,$s6,L15
L15: 
lw $s7,i1
addi $s6,$0,1
add $s7,$s7,$s6
sw $s7,i1
L16: 
lw $s7,i1
addi $s6,$0,9
ble $s7,$s6,L4
sw $s7,i1
L17: 
addi $s7,$0,1
addi $s6,$0,2
ble $s7,$s6,L18
L18: 
li $v0, 1
lw $s7,res1
move $a0, $s7
syscall
sw $s7,res1
L19: 
li $v0, 10
syscall
