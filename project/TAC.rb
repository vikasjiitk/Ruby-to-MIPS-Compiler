=,temp1,3
=,i,temp1
goto,l_label1
flabel,foo
funcarg,a,0
=,temp1,a
=,temp2,1
-,temp3,temp1,temp2
=,a,temp3
=,temp4,i
=,temp5,0
ifgoto,bge,temp4,temp5,l_label2
=,temp6,0
goto,l_label3
label,l_label2
=,temp6,1
label,l_label3
ifgoto,beq,temp6,0,l_label4
=,temp7,i
=,temp8,1
-,temp9,temp7,temp8
=,i,temp9
=,temp10,a
print,temp10
param,a
call,foo
goto,l_label5
label,l_label4
label,l_label5
=,temp11,a
print,temp11
return,0
label,l_label1
=,temp2,1
=,a,temp2
param,a
call,foo
# goto,l_label1
# flabel,foo
# =,temp1,"hi"
# prints,temp1
# call,foo
# return,0
# label,l_label1
# call,foo
# goto,l_label1
# flabel,bar
# funcarg,j,0
# =,temp1,j
# =,temp2,j
# *,temp3,temp1,temp2
# =,s,temp3
# =,string,"bi"
# prints,string
# return,s
# return,0
# label,l_label1
# goto,l_label2
# flabel,foo
# funcarg,i,0
# funcarg,a,1
# param,i
# call,bar,sq
# =,string,"hi"
# prints,string
# =,temp1,sq
# =,temp2,a
# +,temp3,temp1,temp2
# =,t,temp3
# return,t
# return,0
# label,l_label2
# =,temp1,6
# =,f,temp1
# =,temp2,3
# param,temp2
# param,f
# call,foo,i
# =,temp3,i
# print,temp3
# =,temp1,[]
# =,a,temp1
# =,temp2,1
# =,temp3,a[temp2]
# =,temp4,2
# =,temp3,temp4
# =,temp5,1
# =,temp6,a[temp5]
# =,temp7,temp6
# print,temp6
# =,temp1,[]
# =,a,temp1
# =,temp2,2
# =,c,temp2
# =,temp3,1
# =,temp4,a[temp3]
# =,temp5,c
# =,temp4,temp5
# =,temp6,1
# =,temp7,a[temp6]
# =,temp8,temp7
# =,temp9,1
# +,temp10,temp7,temp9
# =,e,temp10
# =,temp11,1
# =,temp12,a[temp11]
# =,temp13,temp12
# print,temp12
# =,temp14,e
# print,temp14
# # =,temp1,[]
# =,a,temp1
# =,temp2,2
# =,c,temp2
# =,temp3,1
# =,temp4,a[temp3]
# =,temp5,c
# =,temp4,temp5
# =,temp6,1
# =,temp7,a[temp6]
# =,temp8,temp7
# print,temp7
# =,temp,[]
# =,a,temp
# =,temp1,5
# =,a[1],temp1
# =,b,a[1]
# print,b
# =,a[1],2
# =,i,4
# =,d,6
# =,a[i],d

# prints,temp1
# =,i,temp1
# =,temp2,i
# ifgoto,beq,temp2,0,label1
# =,temp3,i
# =,temp4,2
# +,temp5,temp3,temp4
# =,i,temp5
# goto,label2
# label,label1
# label,label2
# =,temp1,[]
# =,a,temp1
# =,temp2,2
# =,c,temp2
# =,temp3,3
# =,d,temp3
# =,temp4,1
# =,temp5,a[temp4]
# =,temp6,c
# =,temp7,d
# +,temp8,temp6,temp7
# =,temp5,temp8
# =,temp9,1
# =,temp10,a[temp9]
# =,temp11,temp10
# =,temp12,1
# +,temp13,temp10,temp12
# =,e,temp13
# =,temp14,1
# =,temp15,a[temp14]
# =,temp16,temp15
# print,t
# =,temp17,e
# print,t
