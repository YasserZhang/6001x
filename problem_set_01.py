"""
Assume s is a string of lower case characters.

Write a program that counts up the number of vowels contained in the string s.
Valid vowels are: 'a', 'e', 'i', 'o', and 'u'. For example, 
if s = 'azcbobobegghakl', your program should print:

Number of vowels: 5
For problems such as these, do not include raw_input statements or define the
variable s in any way. Our automated testing will provide a value of s for
you - so the code you submit in the following box should assume s is already
defined. If you are confused by this instruction, please review L4 Problems 10
and 11 before you begin this problem set.
"""

 # Paste your code into this box 
count = 0
x = s.lower()
for char in x:
    if char in ("a", "e", "i", "o", "u"):
        count += 1
print "Number of vowels: " + str(count)



"""
Assume s is a string of lower case characters.

Write a program that prints the number of times the string 'bob' occurs in s.
For example, if s = 'azcbobobegghakl', then your program should print

Number of times bob occurs is: 2
For problems such as these, do not include raw_input statements or define the
variable s in any way. Our automated testing will provide a value of s for you
- so the code you submit in the following box should assume s is already
defined. If you are confused by this instruction, please review L4 Problems 10
and 11 before you begin this problem set.
"""

count = 0
for i in range(len(s)):
    if s[i:i+3] == 'bob':
        count += 1
print "Number of times bob occurs is: " + str(count)

"""
Assume s is a string of lower case characters.

Write a program that prints the longest substring of s in which the letters
occur in alphabetical order. For example, if s = 'azcbobobegghakl',
then your program should print

Longest substring in alphabetical order is: beggh
In the case of ties, print the first substring. For example, if s = 'abcbcd',
then your program should print

Longest substring in alphabetical order is: abc
For problems such as these, do not include raw_input statements or define
the variable s in any way. Our automated testing will provide a value of s
for you - so the code you submit in the following box should assume s is already
defined. If you are confused by this instruction, please review L4 Problems 10
and 11 before you begin this problem set.

Note: This problem is fairly challenging. We encourage you to work smart.
If you've spent more than a few hours on this problem, we suggest that you
move on to a different part of the course. If you have time, come back to
this problem after you've had a break and cleared your head.
"""

 # Paste your code into this box 
result = ' '
for i in range(len(s)-1):
    if ord(s[i]) - ord(s[i+1]) <= 0:
        if result[len(result)-1] == ' ':
            result += s[i]
            result += s[i+1]
        else:
            result += s[i+1]
    else:
        if result[len(result)-1] != ' ':
            result += ' '
        else:
            result = result + s[i] + ' '

l = result.split(" ")
idx = 0
for i in range(1,len(l)):
    if len(l[idx])< len(l[i]):
        idx = i
print "Longest substring in alphabetical order is: " + l[idx]