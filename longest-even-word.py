"""
Consider a string, sentence, of words seperated by spaces where each word is a substring consisting of English
alphabetic letters only.
Find the first word in the sentence that has a length which is both an even number and greater than or equal to the length of any other word
of each length in the sentece. If there are multiple words meeting the criteria, return the one which occurs first in the sentence.
"""

def longestEvenWord(sentence):
    sentence = sentence.split(' ')
    maxLength = sentence[0]

    for i in range(len(sentence)):
        if len(sentence[i]) % 2 == 0 and len(sentence[i]) > len(maxLength):
            maxLength = sentence[i]
            # print(maxLength)
        
    return maxLength
    

print(longestEvenWord('Time to write great code'))
print(longestEvenWord('Time to have a greatt party'))
print(longestEvenWord('Time to have a great party at the castle'))
print(longestEvenWord('It is a pleasant day today'))
