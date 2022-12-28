"""
Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane and an integer k, return the k closest points to the origin (0, 0).

The distance between two points on the X-Y plane is the Euclidean distance (i.e., √(x1 - x2)2 + (y1 - y2)2).

You may return the answer in any order. The answer is guaranteed to be unique (except for the order that it is in).
"""

import math
import heapq

def kClosest(points, k):
    minHeap = []
    # init = math.sqrt((points[0][0] - 0)**2 + (points[0][1] - 0)** 2)
    for i in range(len(points)):
        distance = math.sqrt((points[i][0] - 0)**2 + (points[i][1] - 0)** 2)
        # print(distance)
        minHeap.append([distance, points[i][0], points[i][1]])
    
    heapq.heapify(minHeap)
    # print(minHeap)
    res = []
    while len(res) < k:
        distance, x, y = heapq.heappop(minHeap)
        res.append([x, y])
    return res
    
    
        


print(kClosest([[3,3],[5,-1],[-2,4]], 2))

    