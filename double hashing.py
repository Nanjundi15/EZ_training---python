h=list(map(int,input().split()))
k=[False for i in range(len(h))]
for i in h:
    h_k1=i%11
    h_k2=(8-(i%8))
    
    if k[h_k1]==False:
        k[h_k1]=i
    else:
        for j in range(len(h)):
            hk=(h_k1+(j*h_k2))%11
            if k[hk]==False:
                k[hk]=i
                break
print(k)

"20 34 45 70 56 81 104 37 46 39"