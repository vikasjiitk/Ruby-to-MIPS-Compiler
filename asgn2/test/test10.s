.data
f1: .word 0
i1: .word 0
h1: .word 0
t1: .word 0
a1: .word 0
k1: .word 0
b1: .word 0
c1: .word 0
e1: .word 0
d1: .word 0
.text
main: 
L1: 
addi $t2,$0,2
L2: 
addi $t1,$0,3
L3: 
addi $t0,$0,3
L4: 
sw $t0,c1
addi $t0,$0,4
L5: 
sw $t0,d1
move $t0,$t2
L6: 
mult $t0,$t1
mflo $t0
sw $t0,e1
L7: 
add $t0,$t2,$t1
sw $t0,e1
L8: 
lw $t0,d1
sw $t1,b1
add $t1,$t2,$t0
sw $t1,f1
L9: 
lw $t1,c1
sw $t0,d1
add $t0,$t2,$t1
sw $t0,h1
L10: 
lw $t0,b1
sw $t2,a1
lw $t2,d1
sw $t1,c1
add $t1,$t0,$t2
sw $t1,i1
L11: 
lw $t1,a1
sw $t0,b1
lw $t0,c1
sw $t2,d1
mult $t1,$t0
mflo $t2
sw $t1,a1
sw $t0,c1
sw $t2,t1
L12: 
lw $t2,b1
lw $t0,d1
div $t2,$t0
mflo $t1
sw $t2,b1
sw $t0,d1
sw $t1,k1
L13: 
li $v0, 10
syscall
