.data
a21: .word 0
D.17471: .word 0
a01: .word 0
a61: .word 0
b.11: .word 0
D.17451: .word 0
b1: .word 0
D.17521: .word 0
D.17481: .word 0
a51: .word 0
D.17381: .word 0
D.17401: .word 0
D.17501: .word 0
a31: .word 0
a11: .word 0
D.17461: .word 0
D.17421: .word 0
b.01: .word 0
a71: .word 0
c1: .word 0
D.17491: .word 0
D.17411: .word 0
D.17391: .word 0
a41: .word 0
D.17371: .word 0
.text
main: 
L1: 
addi $s7,$0,10
L2: 
addi $s6,$0,1
sw $s6,a01
L3: 
addi $s6,$0,1
sw $s6,a11
L4: 
addi $s6,$0,1
sw $s6,a21
L5: 
addi $s6,$0,2
sw $s6,a31
L6: 
addi $s6,$0,0
sw $s6,a41
L7: 
addi $s6,$0,1
sw $s6,a51
L8: 
addi $s6,$0,0
sw $s6,a61
L9: 
addi $s6,$0,1
sw $s6,a71
L10: 
sw $s7,c1
lw $s7,c1
addi $s6,$0,0
bgt $s7,$s6,L12
sw $s7,c1
L11: 
addi $s7,$0,1
addi $s6,$0,2
ble $s7,$s6,L21
L12: 
lw $s7,a01
lw $s6,a11
add $s5,$s7,$s6
sw $s7,a01
sw $s6,a11
L13: 
lw $s6,a21
add $s7,$s5,$s6
sw $s5,D.17371
sw $s6,a21
L14: 
lw $s6,a31
add $s5,$s7,$s6
sw $s7,D.17381
sw $s6,a31
L15: 
lw $s6,a41
add $s7,$s5,$s6
sw $s5,D.17391
sw $s6,a41
L16: 
lw $s6,a51
add $s5,$s7,$s6
sw $s7,D.17401
sw $s6,a51
L17: 
lw $s6,a61
add $s7,$s5,$s6
sw $s5,D.17411
sw $s6,a61
L18: 
lw $s6,a71
add $s5,$s7,$s6
sw $s7,D.17421
sw $s6,a71
L19: 
move $s6,$s5
sw $s5,b.01
sw $s6,b1
L20: 
addi $s6,$0,1
addi $s5,$0,2
ble $s6,$s5,L29
L21: 
lw $s7,a01
lw $s6,a11
sub $s5,$s7,$s6
sw $s7,a01
sw $s6,a11
L22: 
lw $s6,a21
add $s7,$s5,$s6
sw $s5,D.17451
sw $s6,a21
L23: 
lw $s6,a31
add $s5,$s7,$s6
sw $s7,D.17461
sw $s6,a31
L24: 
lw $s6,a41
add $s7,$s5,$s6
sw $s5,D.17471
sw $s6,a41
L25: 
lw $s6,a51
add $s5,$s7,$s6
sw $s7,D.17481
sw $s6,a51
L26: 
lw $s6,a61
add $s7,$s5,$s6
sw $s5,D.17491
sw $s6,a61
L27: 
lw $s6,a71
add $s5,$s7,$s6
sw $s7,D.17501
sw $s6,a71
L28: 
move $s6,$s5
sw $s5,b.11
sw $s6,b1
L29: 
li $v0, 1
lw $s7,b1
move $a0, $s7
syscall
sw $s7,b1
L30: 
addi $s7,$0,0
L31: 
li $v0, 10
syscall
sw $s7,D.17521
