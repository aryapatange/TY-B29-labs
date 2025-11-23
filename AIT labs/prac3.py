# A* Pathfinding with Manhattan and Euclidean Heuristics

import math
from heapq import heappush, heappop

# distance heuristics
def manhattan(a, b): return abs(a[0]-b[0]) + abs(a[1]-b[1])
def euclidean(a, b): return math.hypot(a[0]-b[0], a[1]-b[1])

def astar(start, goal, grid, heuristic=manhattan):
    open_list = [(0, start, [start])]  # (f, node, path)
    visited = set()

    while open_list:
        f, node, path = heappop(open_list)
        if node == goal: return path
        if node in visited: continue

        visited.add(node)
        x, y = node
        
        # explore neighbors
        for dx, dy in [(1,0),(-1,0),(0,1),(0,-1)]:
            nx, ny = x+dx, y+dy
            if 0<=nx<len(grid) and 0<=ny<len(grid[0]) and grid[nx][ny]==0:
                g = len(path)
                h = heuristic((nx, ny), goal)
                heappush(open_list, (g+h, (nx, ny), path + [(nx, ny)]))

    return None

# 0 = free, 1 = blocked
grid = [
    [0,0,0,0,1],
    [1,1,0,1,0],
    [0,0,0,0,0],
    [0,1,1,1,0],
    [0,0,0,0,0]
]

start, goal = (0,0), (4,4)

print("Manhattan Path:", astar(start, goal, grid, manhattan))
print("Euclidean Path:", astar(start, goal, grid, euclidean))
