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
sw $t0,c1
L4: 
addi $t0,$0,4
sw $t0,d1
L5: 
move $t0,$t2
L6: 
mult $t0,$t0
mflo $t0
L7: 
add $t0,$t0,$t2
sw $t0,e1
L8: 
lw $t0,f1
add $t0,$t0,$t2
sw $t0,f1
L9: 
lw $t0,h1
add $t0,$t0,$t2
sw $t0,h1
L10: 
lw $t0,i1
add $t0,$t0,$t1
sw $t0,i1
L11: 
lw $t0,t1
mult $t0,$t2
mflo $t0
sw $t0,t1
sw $t2,a1
L12: 
lw $t2,k1
div $t2,$t1
mflo $t2
sw $t2,k1
sw $t1,b1
L13: 
li $v0, 10
syscall
