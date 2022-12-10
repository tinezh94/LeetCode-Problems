"""
There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 
1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return the ordering of courses you should take to finish all courses. If there are many valid answers, return any of them. 
If it is impossible to finish all courses, return an empty array.
"""

def findOrder(numCourses, prerequisites):
    # build adjacency list of prereqs
    preMap = { i: [] for i in range(numCourses)}
    for crs, pre in prerequisites:
        preMap[crs].append(pre)
        
    visitedSet = set()
    cycleSet = set()
    output = []
    # a course has 3 possible states
        # 1. visited- crossed out, crs has been added to the output
        # 2. visiting- crs has not been added to the output, but added to the cycle
        # 3. not visited- crs has not been added to the output or the cycle
    
    def dfs(crs):
        if crs in cycleSet:
            return False
        if crs in visitedSet:
            return True
        
        cycleSet.add(crs)
        for pre in preMap[crs]:
            if dfs(pre) == False:
                return False
        cycleSet.remove(crs)
        visitedSet.add(crs)
        output.append(crs)
        return True
    
    for crs in range(numCourses):
        if not dfs(crs):
            return []
        
    return output