.data
temp11: .word 0
str0 : .asciiz "abcd23"
.text
main:
la $s7,str0
li $v0, 4
move $a0, $s7
syscall
sw $s7,temp11
li $v0,10
syscall
