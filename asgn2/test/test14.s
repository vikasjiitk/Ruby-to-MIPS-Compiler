.data
f1: .word 0
a1: .word 0
b1: .word 0
c1: .word 0
e1: .word 0
d1: .word 0
.text
main: 
L1: 
addi $t2,$0,4
L2: 
addi $t1,$0,5
L3: 
xor $t0,$t2,$t1
L4: 
sw $t0,c1
addi $t0,$0,1
sw $t2,a1
addi $t2,$0,1
sw $t1,b1
addi $t1,$0,1
nor $t1,$t0,$t2
L5: 
lw $t1,a1
lw $t2,b1
sslv $t0,$t1,$t2
L6: 
sw $t0,e1
srav $t0,$t1,$t2
sw $t1,a1
sw $t2,b1
L7: 
li $v0, 1
lw $t2,c1
move $a0, $t2
syscall
sw $t2,c1
L8: 
li $v0, 1
lw $t2,d1
move $a0, $t2
syscall
sw $t2,d1
L9: 
li $v0, 1
lw $t2,e1
move $a0, $t2
syscall
sw $t2,e1
L10: 
li $v0, 1
move $a0, $t0
syscall
sw $t0,f1
L11: 
li $v0, 10
syscall
