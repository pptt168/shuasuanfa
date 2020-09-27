from collections import deque
class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        adjacency = [[] for _ in range(numCourses)]
        flag = [0 for _ in range(numCourses)]
        for tail, head in prerequisites:
            adjacency[head].append(tail)
        def dfs(tail):
            if flag[tail]==-1:return True
            if flag[tail] == 1:return False
            flag[tail] = 1
            for head in adjacency[tail]:
                if not dfs(head): return False
            flag[tail] = -1
            return True 
        for i in range(numCourses):
            if not dfs(i): return False
        return True