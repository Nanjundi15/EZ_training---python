list=[13,21,45,68,97,65,54,89,46,66,41]
print(list)
n=int(input())
k=[False for i in range(len(list))]
for i in list:
    
    h_k=i%n
    if k[h_k]==False:
        k[h_k]=i
    else:
        for j in range(len(list)):
            h1_k=(h_k+j)%n
            if not k[h1_k]:
                k[h1_k]=i
                break
print(k)
    
            