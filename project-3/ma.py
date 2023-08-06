op=[]
var=0
digits = [4,3,2,1]      
for i in range(len(digits)):
    op.append(digits[i])
    var+=op[-1]
    op[-1]+1
print(op)