"""

383. Ransom Note

Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.

Each letter in magazine can only be used once in ransomNote.

"""

def ransomNote(ransomNote, magazine):
    hashA = {}
    hashB = {}
    
    for char in ransomNote:
        hashA[char] = hashA.get(char, 0) + 1
    for char in magazine:
        hashB[char] = hashB.get(char, 0) + 1
    
    for key in hashA:
        if hashA[key] > hashB.get(key, 0):
            return False
        
    return True
    

print(ransomNote('a', 'b '))
print(ransomNote('aa', 'ab'))
print(ransomNote('aa', 'aab'))
print(ransomNote('aajjfoieax', 'jsjfieoajiojfseas'))