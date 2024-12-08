'''
Problem statement
You're given a string 'S' consisting of "{", "}", "(", ")", "[" and "]" .



Return true if the given string 'S' is balanced, else return false.



For example:
'S' = "{}()".

There is always an opening brace before a closing brace i.e. '{' before '}', '(' before ').
So the 'S' is Balanced.
Detailed explanation ( Input/output format, Notes, Images )
Sample Input 1 :
[()]{}{[()()]()}
Sample Output 1 :
Balanced
Explanation Of the Sample Input 1 :
There is always an opening brace before a closing brace i.e. '{' before '}', '(' before '), '[' before ']'.
So the 'S' is Balanced.
Sample Input 2 :
[[}[
Sample Output 2 :
Not Balanced
Constraints:
1 <= 'N' <= 10^5

Where 'N' is the length of the input string 'S'.
Time Limit: 1 sec
'''

def isValidParenthesis(s: str) -> bool:
    a=[]
    t=-1
    for i in s:
        if t!=-1 and ((a[-1]=='(' and i==')') or (a[-1]=='[' and i==']') or (a[-1]=='{' and i=='}')):
            a=a[:len(a)-1]
            t-=1
        else:
            a.append(i)
            t+=1
        #print(t,a)
    return t==-1