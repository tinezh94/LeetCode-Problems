from curses.ascii import isalnum


def countFrequency(string):
    # string = string.replace(" ", "")
    string = ''.join(char for char in string if char.isalnum())
    # print(string)
    subMap = {}
    sub = []
    for i in range(len(string)):
        for j in range(i+1, len(string)+1):
                sub.append(string[i:j])
    
    for i in sub:
        subMap[i] = string.count(i)
        
    sortedList = sorted(subMap.items(), key = lambda x:x[1], reverse=True)
    
    # for k, v in sorted(sortedList):
    #     # print(k, v)
    #     print('{}: {}'.format(k, v))
    
    # print(sortedList)
    
    res = []
    for k, v in sortedList:
        formatted = '{} : {}'.format(k, v)
        res.append(formatted)
    return res
    

print(countFrequency(' ab ab,   aba '))
# print(countFrequency('abajsjfe, feas.'))