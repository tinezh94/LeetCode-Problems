"""
Given an integer array ‘arr[]’ of size N, find the sum of all sub-arrays of the given array.
"""

def sumOfSubarrays(arr):
    sum = 0
    temp = 0
    for i in range(len(arr)):
        temp = 0
        for j in range(i, len(arr)):
            temp += arr[j]
            print('temp', temp)
            sum += temp
            print('sum',sum)
    return sum
    

print(sumOfSubarrays([1, 2, 3]))