.data
a: .word 0
belikejanish: .word 0
.text
main: 
L1: 
addi $t2,$0,2
L2: 
addi $t1,$0,1
L3: 
add $t2,$t2,$t1
sw $t1,belikejanish
L4: 
li $v0, 1
move $a0, $t2
syscall
L5: 
li $v0, 10
syscall
sw $t2,a
