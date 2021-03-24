# -*- coding: utf-8 -*-
"""
Created on Wed Mar 24 22:12:45 2021

@author: Abeg
"""
#toggle each char in a str
"""string=input("")
string1=str()
for i in string:
  if i.isupper():
    i=i.lower()
    string1+=i
  else:
    i=i.upper()
    string1+=i
print(string1)"""
#pallindrome or not

"""string=input()
if(string==string[::-1]):
  print("pallindrome")
else:
  print("not")"""
#reverse order
"""string=input()
print(string[::-1])"""
#remove all char except alphabet
"""string=input()
string1=str()
for i in string:
  if i.isalpha()==True:
    string1+=i
print(string1)"""
#remove space from the str
"""string=map(str,input().split())
string1=""
print(string1.join(string))"""
#romove brackets from algebric expression
"""string=input()
string1=""
for i in string:
  if(i=="(" or i==")" or i=="[" or i=="]" or i=="{" or i=="}"):
    pass
  else:
    string1=string1+i
print(string1)"""
#sum of no in astring
"""string=input()
sum=0
for i in string:
  if(ord(i)>=48 and ord(i)<=57):
    sum=sum+int(i)
print(str(sum))"""
#capitalize first and last char of each word
"""str1=input()
str1 = result = str1.title()
result =  ""
for word in str1.split():
  result += word[:-1] + word[-1].upper() + " "
print(result[:-1])  """
#frequency of character in a SyntaxWarning
"""string=input()
char=input()
print(string.count(char))"""
#non-repeating char isinstance
"""string=input()
for i in string:
  count=0
  for j in string:
    if(i==j):
      count+=1
    if(count>1):
      break
  if count==1:
    print(i,end="")"""
#check two string are anagram or not
"""string1=input()
string2=input()
if len(string1)!=len(string2):
  print("not anagram")
else:
  string1=sorted(string1)
  string2=sorted(string2)
  if(string1==string2):
    print("anagram")
  else:
    print("not")"""
#replace a substring in a String
"""string=input("enter string")
old_string=input("enter string to be replaced")
new_string=input("enter the new string")
print(string.replace(old_string,new_string))"""
#count the common subsequence and print
"""string1=input()
string2=input()
n1=len(string1)
n2=len(string2)
dp=[[0 for i in range(n2+1)]for i in range(n1+1)]
for i in range(1,n1+1):
  for j in range(1,n2+1):
    if(string1[i-1]==string2[j-1]):
      dp[i][j]=(1+dp[i][j-1]+dp[i-1][j])
    else:
      dp[i][j]=(dp[i][j-1]+dp[i-1][j]-dp[i-1][j-1])
print(dp[n1][n2])"""
#check two string if one string contain wild card character
"""def match(first, second): 
    if len(first) == 0 and len(second) == 0: 
        return True
    if len(first) > 1 and first[0] == '*' and  len(second) == 0: 
        return False
    if (len(first) > 1 and first[0] == '?') or (len(first) != 0
        and len(second) !=0 and first[0] == second[0]): 
        return match(first[1:],second[1:]);  
    if len(first) !=0 and first[0] == '*': 
        return match(first[1:],second) or match(first,second[1:]) 
  
    return False
first=input()
second=input()
def test(first, second): 
    if match(first, second): 
        print("yes")
    else: 
        print("no")
print(test(first,second))"""
#find one extra char
"""string1=input("1st")---doubt
string2=input("2nd")
string=""
if(string1==string2):
  print("no data loss")
else:
  for i in range(len(string1)):
    for j in range(len(string2)):
      if(string1[i]==string2[j]):
        pass
      else:
        string=string+string1[i]
        break
  print(string)"""
#minimum no of appends
"""def isPalindrome(Str): 
  
    Len = len(Str) 
  
   
    if (Len == 1): 
        return True
  
    # pointing to first character 
    ptr1 = 0
  
    # pointing to last character 
    ptr2 = Len - 1
  
    while (ptr2 > ptr1): 
  
        if (Str[ptr1] != Str[ptr2]): 
            return False
        ptr1 += 1
        ptr2 -= 1
  
    return True
  
# Recursive function to count number of appends 
def noOfAppends(s): 
  
    if (isPalindrome(s)): 
        return 0
  
    # Removing first character of String by 
    # incrementing base address pointer. 
    del s[0] 
  
    return 1 + noOfAppends(s) 
  
# Driver Code 
se = input()
s = [i for i in se] 
print(noOfAppends(s))"""
  

