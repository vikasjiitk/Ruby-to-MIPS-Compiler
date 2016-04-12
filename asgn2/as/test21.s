.data
D.18141: .word 0
D.17611: .word 0
a01: .word 0
D.17801: .word 0
D.18061: .word 0
D.17881: .word 0
a251: .word 0
D.17961: .word 0
a311: .word 0
a151: .word 0
D.17681: .word 0
D.17621: .word 0
D.18151: .word 0
D.17811: .word 0
a71: .word 0
D.18011: .word 0
D.17951: .word 0
a241: .word 0
a81: .word 0
D.17891: .word 0
D.17751: .word 0
a121: .word 0
D.17691: .word 0
D.17861: .word 0
D.17731: .word 0
a61: .word 0
D.17631: .word 0
b1: .word 0
D.18121: .word 0
D.18001: .word 0
D.17941: .word 0
D.18091: .word 0
D.17741: .word 0
a231: .word 0
a131: .word 0
D.17871: .word 0
D.18031: .word 0
D.17721: .word 0
D.17641: .word 0
b.01: .word 0
D.18131: .word 0
D.17971: .word 0
a181: .word 0
a101: .word 0
D.18081: .word 0
a221: .word 0
D.17711: .word 0
D.18021: .word 0
D.17901: .word 0
D.18181: .word 0
D.17651: .word 0
D.17841: .word 0
b.11: .word 0
D.18101: .word 0
a191: .word 0
a111: .word 0
a291: .word 0
a51: .word 0
a211: .word 0
D.18221: .word 0
a31: .word 0
D.17851: .word 0
D.17701: .word 0
a281: .word 0
D.18051: .word 0
c1: .word 0
D.18111: .word 0
a91: .word 0
D.17991: .word 0
a161: .word 0
a41: .word 0
D.17791: .word 0
a201: .word 0
a21: .word 0
D.17771: .word 0
D.18211: .word 0
D.18041: .word 0
D.18161: .word 0
D.17821: .word 0
D.17781: .word 0
D.17981: .word 0
a141: .word 0
D.17661: .word 0
a171: .word 0
D.18191: .word 0
a271: .word 0
a11: .word 0
D.17761: .word 0
D.18201: .word 0
D.17931: .word 0
D.18071: .word 0
D.18171: .word 0
D.17831: .word 0
D.17671: .word 0
a301: .word 0
a261: .word 0
.text
main: 
L1: 
addi $s7,$0,10
L2: 
addi $s6,$0,1
sw $s6,a01
L3: 
addi $s6,$0,1
sw $s6,a11
L4: 
addi $s6,$0,1
sw $s6,a21
L5: 
addi $s6,$0,2
sw $s6,a31
L6: 
addi $s6,$0,0
sw $s6,a41
L7: 
addi $s6,$0,1
sw $s6,a51
L8: 
addi $s6,$0,0
sw $s6,a61
L9: 
addi $s6,$0,1
sw $s6,a71
L10: 
addi $s6,$0,0
sw $s6,a81
L11: 
addi $s6,$0,2
sw $s6,a91
L12: 
addi $s6,$0,1
sw $s6,a101
L13: 
addi $s6,$0,2
sw $s6,a111
L14: 
addi $s6,$0,0
sw $s6,a121
L15: 
addi $s6,$0,2
sw $s6,a131
L16: 
addi $s6,$0,0
sw $s6,a141
L17: 
addi $s6,$0,1
sw $s6,a151
L18: 
addi $s6,$0,2
sw $s6,a161
L19: 
addi $s6,$0,2
sw $s6,a171
L20: 
addi $s6,$0,0
sw $s6,a181
L21: 
addi $s6,$0,1
sw $s6,a191
L22: 
addi $s6,$0,0
sw $s6,a201
L23: 
addi $s6,$0,1
sw $s6,a211
L24: 
addi $s6,$0,0
sw $s6,a221
L25: 
addi $s6,$0,1
sw $s6,a231
L26: 
addi $s6,$0,0
sw $s6,a241
L27: 
addi $s6,$0,0
sw $s6,a251
L28: 
addi $s6,$0,0
sw $s6,a261
L29: 
addi $s6,$0,2
sw $s6,a271
L30: 
addi $s6,$0,2
sw $s6,a281
L31: 
addi $s6,$0,0
sw $s6,a291
L32: 
addi $s6,$0,0
sw $s6,a301
L33: 
addi $s6,$0,1
sw $s6,a311
L34: 
sw $s7,c1
lw $s7,c1
addi $s6,$0,0
bgt $s7,$s6,L36
sw $s7,c1
L35: 
addi $s7,$0,1
addi $s6,$0,2
ble $s7,$s6,L69
L36: 
lw $s7,a01
lw $s6,a11
add $s5,$s7,$s6
sw $s7,a01
sw $s6,a11
L37: 
lw $s6,a21
add $s7,$s5,$s6
sw $s5,D.17611
sw $s6,a21
L38: 
lw $s6,a31
add $s5,$s7,$s6
sw $s7,D.17621
sw $s6,a31
L39: 
lw $s6,a41
add $s7,$s5,$s6
sw $s5,D.17631
sw $s6,a41
L40: 
lw $s6,a51
add $s5,$s7,$s6
sw $s7,D.17641
sw $s6,a51
L41: 
lw $s6,a61
add $s7,$s5,$s6
sw $s5,D.17651
sw $s6,a61
L42: 
lw $s6,a71
add $s5,$s7,$s6
sw $s7,D.17661
sw $s6,a71
L43: 
lw $s6,a81
add $s7,$s5,$s6
sw $s5,D.17671
sw $s6,a81
L44: 
lw $s6,a91
add $s5,$s7,$s6
sw $s7,D.17681
sw $s6,a91
L45: 
lw $s6,a101
add $s7,$s5,$s6
sw $s5,D.17691
sw $s6,a101
L46: 
lw $s6,a111
add $s5,$s7,$s6
sw $s7,D.17701
sw $s6,a111
L47: 
lw $s6,a121
add $s7,$s5,$s6
sw $s5,D.17711
sw $s6,a121
L48: 
lw $s6,a131
add $s5,$s7,$s6
sw $s7,D.17721
sw $s6,a131
L49: 
lw $s6,a141
add $s7,$s5,$s6
sw $s5,D.17731
sw $s6,a141
L50: 
lw $s6,a151
add $s5,$s7,$s6
sw $s7,D.17741
sw $s6,a151
L51: 
lw $s6,a161
add $s7,$s5,$s6
sw $s5,D.17751
sw $s6,a161
L52: 
lw $s6,a171
add $s5,$s7,$s6
sw $s7,D.17761
sw $s6,a171
L53: 
lw $s6,a181
add $s7,$s5,$s6
sw $s5,D.17771
sw $s6,a181
L54: 
lw $s6,a191
add $s5,$s7,$s6
sw $s7,D.17781
sw $s6,a191
L55: 
lw $s6,a201
add $s7,$s5,$s6
sw $s5,D.17791
sw $s6,a201
L56: 
lw $s6,a211
add $s5,$s7,$s6
sw $s7,D.17801
sw $s6,a211
L57: 
lw $s6,a221
add $s7,$s5,$s6
sw $s5,D.17811
sw $s6,a221
L58: 
lw $s6,a231
add $s5,$s7,$s6
sw $s7,D.17821
sw $s6,a231
L59: 
lw $s6,a241
add $s7,$s5,$s6
sw $s5,D.17831
sw $s6,a241
L60: 
lw $s6,a251
add $s5,$s7,$s6
sw $s7,D.17841
sw $s6,a251
L61: 
lw $s6,a261
add $s7,$s5,$s6
sw $s5,D.17851
sw $s6,a261
L62: 
lw $s6,a271
add $s5,$s7,$s6
sw $s7,D.17861
sw $s6,a271
L63: 
lw $s6,a281
add $s7,$s5,$s6
sw $s5,D.17871
sw $s6,a281
L64: 
lw $s6,a291
add $s5,$s7,$s6
sw $s7,D.17881
sw $s6,a291
L65: 
lw $s6,a301
add $s7,$s5,$s6
sw $s5,D.17891
sw $s6,a301
L66: 
lw $s6,a311
add $s5,$s7,$s6
sw $s7,D.17901
sw $s6,a311
L67: 
move $s6,$s5
sw $s5,b.01
sw $s6,b1
L68: 
addi $s6,$0,1
addi $s5,$0,2
ble $s6,$s5,L101
L69: 
lw $s7,a01
lw $s6,a11
sub $s5,$s7,$s6
sw $s7,a01
sw $s6,a11
L70: 
lw $s6,a21
add $s7,$s5,$s6
sw $s5,D.17931
sw $s6,a21
L71: 
lw $s6,a31
add $s5,$s7,$s6
sw $s7,D.17941
sw $s6,a31
L72: 
lw $s6,a41
add $s7,$s5,$s6
sw $s5,D.17951
sw $s6,a41
L73: 
lw $s6,a51
add $s5,$s7,$s6
sw $s7,D.17961
sw $s6,a51
L74: 
lw $s6,a61
add $s7,$s5,$s6
sw $s5,D.17971
sw $s6,a61
L75: 
lw $s6,a71
add $s5,$s7,$s6
sw $s7,D.17981
sw $s6,a71
L76: 
lw $s6,a81
add $s7,$s5,$s6
sw $s5,D.17991
sw $s6,a81
L77: 
lw $s6,a91
add $s5,$s7,$s6
sw $s7,D.18001
sw $s6,a91
L78: 
lw $s6,a101
add $s7,$s5,$s6
sw $s5,D.18011
sw $s6,a101
L79: 
lw $s6,a111
add $s5,$s7,$s6
sw $s7,D.18021
sw $s6,a111
L80: 
lw $s6,a121
add $s7,$s5,$s6
sw $s5,D.18031
sw $s6,a121
L81: 
lw $s6,a131
add $s5,$s7,$s6
sw $s7,D.18041
sw $s6,a131
L82: 
lw $s6,a141
add $s7,$s5,$s6
sw $s5,D.18051
sw $s6,a141
L83: 
lw $s6,a151
add $s5,$s7,$s6
sw $s7,D.18061
sw $s6,a151
L84: 
lw $s6,a161
add $s7,$s5,$s6
sw $s5,D.18071
sw $s6,a161
L85: 
lw $s6,a171
add $s5,$s7,$s6
sw $s7,D.18081
sw $s6,a171
L86: 
lw $s6,a181
add $s7,$s5,$s6
sw $s5,D.18091
sw $s6,a181
L87: 
lw $s6,a191
add $s5,$s7,$s6
sw $s7,D.18101
sw $s6,a191
L88: 
lw $s6,a201
add $s7,$s5,$s6
sw $s5,D.18111
sw $s6,a201
L89: 
lw $s6,a211
add $s5,$s7,$s6
sw $s7,D.18121
sw $s6,a211
L90: 
lw $s6,a221
add $s7,$s5,$s6
sw $s5,D.18131
sw $s6,a221
L91: 
lw $s6,a231
add $s5,$s7,$s6
sw $s7,D.18141
sw $s6,a231
L92: 
lw $s6,a241
add $s7,$s5,$s6
sw $s5,D.18151
sw $s6,a241
L93: 
lw $s6,a251
add $s5,$s7,$s6
sw $s7,D.18161
sw $s6,a251
L94: 
lw $s6,a261
add $s7,$s5,$s6
sw $s5,D.18171
sw $s6,a261
L95: 
lw $s6,a271
add $s5,$s7,$s6
sw $s7,D.18181
sw $s6,a271
L96: 
lw $s6,a281
add $s7,$s5,$s6
sw $s5,D.18191
sw $s6,a281
L97: 
lw $s6,a291
add $s5,$s7,$s6
sw $s7,D.18201
sw $s6,a291
L98: 
lw $s6,a301
add $s7,$s5,$s6
sw $s5,D.18211
sw $s6,a301
L99: 
lw $s6,a311
add $s5,$s7,$s6
sw $s7,D.18221
sw $s6,a311
L100: 
move $s6,$s5
sw $s5,b.11
sw $s6,b1
L101: 
li $v0, 1
lw $s7,b1
move $a0, $s7
syscall
sw $s7,b1
L102: 
li $v0, 10
syscall
