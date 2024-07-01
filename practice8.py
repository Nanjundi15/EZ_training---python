list=[4,-1,-3,6,-2,-1,3,2,-8,-2]
sum=0
maxi=0
for i in range(len(list)):
    # for j in range(i,len(list)):
        sum+=list[i]
        if sum>maxi:
            maxi=sum
print(maxi)
print(sum)
          
        
    
