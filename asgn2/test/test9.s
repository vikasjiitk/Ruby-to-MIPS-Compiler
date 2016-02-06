.data
f1: .word 0
g1: .word 0
i1: .word 0
h1: .word 0
j1: .word 0
a1: .word 0
b1: .word 0
c1: .word 0
e1: .word 0
d1: .word 0
.text
main: 
L1: 
addi $t2,$0,2
L2: 
addi $t1,$0,1
L3: 
addi $t0,$0,1
L4: 
sw $t0,c1
addi $t0,$0,1
sw $t0,d1
L5: 
addi $t0,$0,1
L6: 
sw $t0,e1
addi $t0,$0,1
L7: 
sw $t0,f1
addi $t0,$0,1
L8: 
sw $t0,g1
addi $t0,$0,1
L9: 
add $t1,$t1,$t2
sw $t1,b1
L10: 
lw $t1,c1
add $t1,$t1,$t2
L11: 
sw $t2,a1
lw $t2,e1
add $t2,$t2,$t1
sw $t2,e1
sw $t1,c1
L12: 
lw $t1,g1
lw $t2,f1
add $t1,$t1,$t2
L13: 
add $t0,$t0,$t1
sw $t1,g1
L14: 
lw $t1,a1
mult $t1,$t1
mflo $t1
L15: 
sub $t1,$t1,$t1
L16: 
add $t0,$t0,$t2
sw $t0,h1
sw $t2,f1
L17: 
add $t1,$t1,$t1
sw $t1,a1
L18: 
jal foo
move $t1,$v1
sw $t1,i1
L19: 
jal foo1
move $t2,$v1
sw $t2,j1
L20: 
li $v0, 10
syscall
foo: 
L22: 
li $v0, 1
lw $t2,a1
move $a0, $t2
syscall
sw $t2,a1
L23: 
addi $t2,$0,1
move $v1, $t2
jr $ra
foo1: 
L25: 
li $v0, 1
lw $t2,b1
move $a0, $t2
syscall
sw $t2,b1
L26: 
addi $t2,$0,1
move $v1, $t2
jr $ra
