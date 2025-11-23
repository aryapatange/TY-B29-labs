#8 puzzle using bfs and dfs
from collections import deque

moves = {'U':-3, 'D':3, 'L':-1, 'R':1}

def valid(pos, m):
    return not ((m=='L' and pos%3==0) or
                (m=='R' and pos%3==2) or
                (m=='U' and pos<3) or
                (m=='D' and pos>5))

def neighbors(state):
    res = []
    i = state.index('0')
    for m, step in moves.items():
        if valid(i, m):
            s = list(state)
            j = i + step
            s[i], s[j] = s[j], s[i]
            res.append(''.join(s))
    return res

def bfs(start, goal):
    q = deque([start])
    vis = {start}
    while q:
        s = q.popleft()
        print(s)
        if s == goal:
            print("Goal reached!")
            return
        for n in neighbors(s):
            if n not in vis:
                vis.add(n)
                q.append(n)

def dfs(start, goal):
    stack = [start]
    vis = {start}
    while stack:
        s = stack.pop()
        print(s)
        if s == goal:
            print("Goal reached!")
            return
        for n in neighbors(s):
            if n not in vis:
                vis.add(n)
                stack.append(n)

# Run
bfs("123405678", "123456780")
print("\n--- DFS ---\n")
dfs("123405678", "123456780")

#maze navigation
from collections import deque

maze = [
    [0,1,0,0,0],
    [0,1,0,1,0],
    [0,0,0,1,0],
    [1,1,0,1,0],
    [0,0,0,0,0]
]

start, goal = (0,0), (4,4)

def bfs(maze, start, goal):
    q = deque([[start]])      # store path
    visited = set([start])
    
    while q:
        path = q.popleft()
        x, y = path[-1]

        if (x, y) == goal:    # goal reached
            return path

        for dx, dy in [(1,0),(-1,0),(0,1),(0,-1)]:  # 4 directions
            nx, ny = x+dx, y+dy
            if 0<=nx<len(maze) and 0<=ny<len(maze[0]) and maze[nx][ny]==0:
                if (nx, ny) not in visited:
                    visited.add((nx, ny))
                    q.append(path + [(nx, ny)])

    return None

print("Path:", bfs(maze, start, goal))
