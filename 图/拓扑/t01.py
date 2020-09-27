# https: // leetcode-cn.com/problems/course-schedule/，课程表
from collections import deque
class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        adjacency = [[] for _ in range(numCourses)]
        indegrees = [0 for _ in range(numCourses)]
        for tail,head in prerequisites:
            indegrees[head] += 1
            adjacency[tail].append(head)
        quequ=deque()
        for i,d in enumerate(range(indegrees)):
            if d==0:quequ.append(i)
        while quequ:
            tail=quequ.popleft()
            numCourses-=1
            for head in adjacency[tail]:
                indegrees[head]-=1
                if(indegrees[head]==0):
                    quequ.append(head)
        return numCourses==0
        
