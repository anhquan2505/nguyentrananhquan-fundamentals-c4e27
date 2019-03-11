def giatri(k,n):
    if k==0 or k==n: 
        return 1
    elif(k==1): 
        return n
    return giatri(k-1,n-1) + giatri(k,n-1)

m=int(input("nhap n: "))
for i in range(m):
    for j in range(i+1):
        print(giatri(j,i),end=' ')
    print()