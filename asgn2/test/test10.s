.data
a: .word 0
c: .word 0
e: .word 0
d: .word 0
f: .word 0
i: .word 0
h: .word 0
k: .word 0
j: .word 0
belikejanish: .word 0
.text
main: 
L1: 
addi $t2,$0,2
L2: 
addi $t1,$0,3
L3: 
addi $t0,$0,3
L4: 
sw $t0,c
addi $t0,$0,4
L5: 
sw $t0,d
move $t0,$t2
L6: 
mult $t0,$t1
mflo $t0
sw $t0,e
L7: 
add $t0,$t2,$t1
sw $t0,e
L8: 
lw $t0,d
sw $t1,belikejanish
add $t1,$t2,$t0
sw $t1,f
L9: 
lw $t1,c
sw $t0,d
add $t0,$t2,$t1
sw $t0,h
L10: 
lw $t0,belikejanish
sw $t2,a
lw $t2,d
sw $t1,c
add $t1,$t0,$t2
sw $t1,i
L11: 
lw $t1,a
sw $t2,d
lw $t2,c
sw $t0,belikejanish
mult $t1,$t2
mflo $t0
sw $t1,a
sw $t2,c
sw $t0,j
L12: 
lw $t0,belikejanish
lw $t2,d
div $t0,$t2
mflo $t1
sw $t0,belikejanish
sw $t2,d
sw $t1,k
L13: 
li $v0, 10
syscall
