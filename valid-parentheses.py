"""
20. Valid Parentheses
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

1. Open brackets must be closed by the same type of brackets.
2. Open brackets must be closed in the correct order.
3. Every close bracket has a corresponding open bracket of the same type.

"""

def validParentheses(string):
    map = [] # stack
    pairedBrackets = {'}': '{', ']': '[', ')': '('}

    for char in string:
        # if char is in pairedBrackets
        if char in pairedBrackets:
            # if map has length and the last itme in map is the corresponding value of char, pop it off the stack(map)
            if map and map[len(map) - 1] == pairedBrackets[char]:
                map.pop()
            # if map is empty or the last item in map is not the corresponding value of char( which means they are not same pair of bracket), return False
            else:
                return False
        # if char is not any of the key values in pairedBracket, add it to the map
        else:
            map.append(char)
    # return True if the map is empty, which means all the items in the map have been popped off 
    return True if not map else False



print(validParentheses("()[]{}"))
print(validParentheses('()'))
print(validParentheses('(]'))
