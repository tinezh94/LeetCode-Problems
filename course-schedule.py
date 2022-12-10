"""
There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. 
You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return true if you can finish all courses. Otherwise, return false.
"""

def canFinish(numCourses, prerequisites):
    prevMap = { i: [] for i in range(numCourses)}
    
    for crs, pre in prerequisites:
        prevMap[crs].append(pre)
        
    visitedSet = set()
    def dfs(crs):
        if crs in visitedSet:
            return False
        if prevMap[crs] == []:
            return True
        
        visitedSet.add(crs)
        for pre in prevMap[crs]:
            if not dfs(pre): return False
        visitedSet.remove(crs)
        prevMap[crs] = []
        return True
    
    for crs in range(numCourses):
        if not dfs(crs): return False
    
    return True
