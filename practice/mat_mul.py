def mat_prod(A,B):
    C=[]
    for i in range(len(A)):
        C.append([])
        for j in range(len(A)):
            C[i].append(0)
            sum=0
            for k in range(len(A)):
                sum+=A[i][k]*B[k][j]
            C[i][j]=sum
    return C
    
    
def five_product(A,B,C,D,E):
    res=mat_prod(A,B)
    res2=mat_prod(res,C)
    res3=mat_prod(res2,D)
    res4=mat_prod(res3,E)
    return res4
    
A=[[1,2],[3,4]]
B=[[5,6],[7,8]]
C=[[9,10],[11,12]]
D=[[13,14],[15,16]]
E=[[17,18],[19,20]]

print(five_product(A,B,C,D,E))    
    
