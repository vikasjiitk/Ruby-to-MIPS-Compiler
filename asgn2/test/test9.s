.data
f1: .word 0
g1: .word 0
i1: .word 0
h1: .word 0
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
L5: 
sw $t0,d1
addi $t0,$0,1
sw $t0,e1
L6: 
addi $t0,$0,1
L7: 
sw $t0,f1
addi $t0,$0,1
sw $t0,g1
L8: 
addi $t0,$0,1
sw $t0,h1
L9: 
add $t1,$t2,$t1
L10: 
lw $t0,c1
add $t0,$t2,$t0
L11: 
sw $t1,b1
lw $t1,d1
sw $t2,a1
add $t2,$t0,$t1
sw $t0,c1
sw $t1,d1
L12: 
lw $t1,f1
add $t0,$t1,$t2
sw $t2,e1
L13: 
lw $t2,a1
sw $t1,f1
add $t1,$t0,$t2
sw $t1,h1
L14: 
mult $t2,$t2
mflo $t2
L15: 
lw $t1,b1
sub $t2,$t2,$t1
L16: 
sw $t2,a1
lw $t2,f1
sw $t1,b1
add $t1,$t2,$t0
sw $t2,f1
sw $t0,g1
sw $t1,h1
L17: 
lw $t1,a1
lw $t0,b1
add $t1,$t1,$t0
sw $t1,a1
sw $t0,b1
L18: 
jal foo
move $t0,$v1
sw $t0,i1
L19: 
jal foo1
addi $t2,$0,1
move $t2,$v1
L20: 
li $v0, 10
syscall
foo: 
L22: 
li $v0, 1
lw $t2,a1
move $a0, $t2
syscall
L23: 
addi $t1,$0,1
move $v1, $t1
jr $ra
sw $t2,a1
foo1: 
L25: 
li $v0, 1
lw $t2,b1
move $a0, $t2
syscall
L26: 
addi $t1,$0,1
move $v1, $t1
jr $ra
sw $t2,b1
