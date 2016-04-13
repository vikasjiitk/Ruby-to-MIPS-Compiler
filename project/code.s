.data
temp41: .word 0
temp21: .word 0
temp71: .word 0
temp61: .word 0
temp31: .word 0
temp101: .word 0
temp91: .word 0
res1: .word 0
temp81: .word 0
temp51: .word 0
t1: .word 0
temp11: .word 0
t11: .word 0
t21: .word 0
n1: .word 0
temp111: .word 0
t31: .word 0
.text
main:
addi $s7,$0,1
move $s6,$s7
sw $s7,temp11
sw $s6,res1
j l_label1
fact: 
addi $sp,$sp,-4
sw $ra,0($sp)
lw $s7,n1
move $s7,$a0
move $s6,$s7
sw $s7,n1
addi $s7,$0,1
sw $s6,temp11
sw $s7,temp21
lw $s7,temp11
lw $s6,temp21
beq $s7,$s6,l_label2
sw $s7,temp11
sw $s6,temp21
addi $s7,$0,0
sw $s7,temp31
j l_label3
l_label2: 
addi $s7,$0,1
sw $s7,temp31
l_label3: 
lw $s7,temp31
addi $s6,$0,0
beq $s7,$s6,l_label4
sw $s7,temp31
addi $s7,$0,0
move $v1, $s7
lw $ra,0($sp)
addi $sp,$sp,4
jr $ra
sw $s7,temp41
j l_label5
l_label4: 
l_label5: 
lw $s7,res1
move $s6,$s7
sw $s7,res1
lw $s7,n1
move $s5,$s7
mult $s6,$s5
mflo $s4
sw $s6,temp51
sw $s5,temp61
move $s5,$s4
sw $s4,temp71
sw $s5,res1
move $s5,$s7
sw $s7,n1
addi $s7,$0,1
sub $s4,$s5,$s7
sw $s5,temp81
sw $s7,temp91
move $s7,$s4
sw $s4,temp101
move $a0,$s7
sw $s7,t31
jal fact
addi $s7,$0,0
move $v1, $s7
lw $ra,0($sp)
addi $sp,$sp,4
jr $ra
sw $s7,temp111
addi $s7,$0,0
move $v1, $s7
lw $ra,0($sp)
addi $sp,$sp,4
jr $ra
l_label1: 
j l_label6
ret: 
addi $sp,$sp,-4
sw $ra,0($sp)
lw $s7,n1
move $s7,$a0
move $s6,$s7
sw $s7,n1
addi $s7,$0,1
sw $s6,temp11
sw $s7,temp21
lw $s7,temp11
lw $s6,temp21
beq $s7,$s6,l_label7
sw $s7,temp11
sw $s6,temp21
addi $s7,$0,0
sw $s7,temp31
j l_label8
l_label7: 
addi $s7,$0,1
sw $s7,temp31
l_label8: 
lw $s7,temp31
addi $s6,$0,0
beq $s7,$s6,l_label9
sw $s7,temp31
addi $s7,$0,1
move $v1, $s7
lw $ra,0($sp)
addi $sp,$sp,4
jr $ra
sw $s7,temp41
j l_label10
l_label9: 
l_label10: 
lw $s7,n1
move $s6,$s7
sw $s7,n1
addi $s7,$0,1
sub $s5,$s6,$s7
sw $s6,temp51
sw $s7,temp61
move $s7,$s5
sw $s5,temp71
move $a0,$s7
sw $s7,t11
jal ret
move $s7,$v1
sw $s7,t1
lw $s7,t1
move $s6,$s7
sw $s7,t1
li $v0, 1
move $a0, $s6
syscall
sw $s6,temp81
lw $s6,t11
move $s7,$s6
sw $s6,t11
addi $s6,$0,1
add $s5,$s7,$s6
sw $s7,temp91
sw $s6,temp101
move $s6,$s5
sw $s5,temp111
move $v1, $s6
lw $ra,0($sp)
addi $sp,$sp,4
jr $ra
sw $s6,t21
addi $s6,$0,0
move $v1, $s6
lw $ra,0($sp)
addi $sp,$sp,4
jr $ra
l_label6: 
addi $s7,$0,10
move $a0,$s7
sw $s7,temp21
jal ret
move $s7,$v1
sw $s7,res1
li $v0,10
syscall
