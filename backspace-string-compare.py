"""
844. Backspace String and Compare

Given two strings s and t, return true if they are equal when both are typed into empty text editors. '#' means a backspace character.

Note that after backspacing an empty text, the text will continue empty.

"""

def backspaceCompare(s, t):
    stack1 = []
    stack2 = []
    
    for c in s:
        if c != '#':
            stack1.append(c)
        else:
            if stack1: stack1.pop()
    
    for c in t:
        if c != '#':
            stack2.append(c)
        else:
            if stack2: stack2.pop()
    
    return stack1 == stack2
        

print(backspaceCompare("ab#c", "ad#c"))
print(backspaceCompare("ab##", "c#d#"))
print(backspaceCompare("a#c", "b"))