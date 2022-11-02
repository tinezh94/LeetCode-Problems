"""

70. Climbing Stairs

You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

"""

def climbingStairs(n):
    one, two = 1, 1
    for i in range(n - 1):
        temp = one
        # the sum of the previous two numbers equals the next number 
        one = one + two
        two = temp 
    return one
    

print(climbingStairs(2))
print(climbingStairs(3))
print(climbingStairs(5))