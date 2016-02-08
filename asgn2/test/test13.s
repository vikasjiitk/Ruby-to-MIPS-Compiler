.data
a1: .word 0
c1: .word 0
b1: .word 0
d1: .word 0
.text
main: 
L1: 
addi $t2,$0,4
L2: 
addi $t1,$0,5
L3: 
or $t0,$t2,$t1
L4: 
sw $t0,c1
and $t0,$t2,$t1
sw $t2,a1
sw $t1,b1
L5: 
li $v0, 1
lw $t1,c1
move $a0, $t1
syscall
sw $t1,c1
L6: 
li $v0, 1
move $a0, $t0
syscall
sw $t0,d1
L7: 
li $v0, 10
syscall
