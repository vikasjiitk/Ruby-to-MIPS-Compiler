[0, 14]
.data
D.17321: .word 0
eval1: .word 0
D.17341: .word 0
D.17301: .word 0
D.17311: .word 0
D.17331: .word 0
a1: .word 0
b1: .word 0
c1: .word 0
d1: .word 0
.text
main: 
L1: 
addi $s7,$0,0
L2: 
addi $s6,$0,10
L3: 
addi $s5,$0,20
L4: 
addi $s4,$0,40
L5: 
div $s6,$s7
mflo $s3
sw $s6,b1
L6: 
add $s6,$s3,$s7
sw $s3,D.17301
sw $s7,a1
L7: 
addi $s7,$0,2
mult $s4,$s7
mflo $s3
L8: 
add $s7,$s6,$s3
sw $s6,D.17311
sw $s3,D.17321
L9: 
mult $s5,$s4
mflo $s3
sw $s5,c1
sw $s4,d1
L10: 
add $s7,$s3,$s7
sw $s3,D.17331
L11: 
li $v0, 1
move $a0, $s7
syscall
sw $s7,eval1
L12: 
addi $s7,$0,0
sw $s7,D.17341
L13: 
li $v0, 10
syscall
