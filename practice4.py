'''
3) Chocolate jar
You are given an integer array of size N, representing jars of chocolates. Three students A, B, and C respectively,
will pick chocolates one by one from each chocolate jar, till the jar is empty, and then repeat the same with the rest of the jars. 
Your task is to fine and return an integer value representing the total number of chocolates that student A will have, 
after all the chocolates have been picked from all the jars.
Note: Once a jar is done A will start taking the chocolates from the new jar.
Input Format :
input1: An integer array representing the quantity of chocolates in each jar. input2: An integer value N representing the number of jars.
Output Format:
Return an integer value representing the total number of chocolates that student A will have, after all the chocolates are picked.
Example:
Input:
10 20 30 
Output:
21'''
jar=[10,20,30]
n=3
a=0
# b=0
# c=0
for i in jar:
    if i%3==0:
        a+=i//3
        # b+=i//3
        # c+=i//3    for a and b displaying how many distributed
        
    if i%3>0:
        a+=i//3+1
        # b+=i//3
        # c+=i//3
# print(a,b,c)
print(a)