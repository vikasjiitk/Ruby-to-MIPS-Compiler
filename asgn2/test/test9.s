.data
a: .word 0
c: .word 0
e: .word 0
d: .word 0
g: .word 0
f: .word 0
i: .word 0
h: .word 0
j: .word 0
belikejanish: .word 0
.text
main: 
L1: 
addi $t2,$0,2
L2: 
addi $t1,$0,1
L3: 
addi $t0,$0,1
L4: 
sw $t0,c
addi $t0,$0,1
L5: 
sw $t0,d
addi $t0,$0,1
sw $t0,e
L6: 
addi $t0,$0,1
L7: 
sw $t0,f
addi $t0,$0,1
sw $t0,g
L8: 
addi $t0,$0,1
sw $t0,h
L9: 
add $t1,$t2,$t1
L10: 
lw $t0,c
add $t0,$t2,$t0
L11: 
sw $t1,belikejanish
lw $t1,d
sw $t2,a
add $t2,$t0,$t1
sw $t0,c
sw $t1,d
L12: 
lw $t1,f
add $t0,$t1,$t2
sw $t2,e
L13: 
lw $t2,a
sw $t1,f
add $t1,$t0,$t2
sw $t1,h
L14: 
mult $t2,$t2
mflo $t2
L15: 
lw $t1,belikejanish
sub $t2,$t2,$t1
L16: 
sw $t2,a
lw $t2,f
sw $t1,belikejanish
add $t1,$t2,$t0
sw $t2,f
sw $t0,g
sw $t1,h
L17: 
lw $t1,a
lw $t0,belikejanish
add $t1,$t1,$t0
sw $t1,a
sw $t0,belikejanish
L18: 
jal foo
move $t0,$v1
sw $t0,i
L19: 
jal foo1
move $t2,$v1
sw $t2,j
foo: 
L21: 
li $v0, 1
lw $t2,a
move $a0, $t2
syscall
L22: 
li $v0, 10
syscall
sw $t2,a
foo1: 
L24: 
li $v0, 1
lw $t2,belikejanish
move $a0, $t2
syscall
L25: 
jr $ra
L26: 
jr $ra
sw $t2,belikejanish
