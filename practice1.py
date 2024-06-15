"""7) Space Counter
You have been given the task of making the content on a social media platform more user-friendly.
Your task is to find and return an integer value representing the count of the number of spaces in a given string S.
Input: A string S
Output :
Return an integer value representing the count of the number of spaces in a given string S.
Example:
Input: Hello World Hey
Output:
2"""
string=input()
count=0
space=0
for i in string:
    if " " == i:
        count+=1
print(count)