# ============================
# N-QUEENS WITH FORWARD CHECKING
# ============================

def safe(board, r, c):
    for i in range(r):
        if board[i] == c or abs(board[i]-c) == abs(i-r):
            return False
    return True

def fc(board, r, c, n, dom):
    nd = [d.copy() for d in dom]            # copy domains
    for i in range(r+1, n):
        for x in (c, c+(i-r), c-(i-r)):     # same col + diagonals
            if x in nd[i]: nd[i].remove(x)
    return nd

def solve(board, r, n, dom):
    if r == n: return [board[:]]
    res = []
    for c in dom[r]:
        if safe(board, r, c):
            board[r] = c
            nd = fc(board, r, c, n, dom)
            if all(nd[i] for i in range(r+1, n)):
                res += solve(board, r+1, n, nd)
    return res

n = 8
domains = [list(range(n)) for _ in range(n)]
ans = solve([-1]*n, 0, n, domains)
print("\nN-Queens Solutions:", len(ans))
print("Example:", ans[0])


# ============================
# SUDOKU SOLVER (BACKTRACKING)
# ============================

def find_cell(b):
    for i in range(9):
        for j in range(9):
            if b[i][j] == 0: return i, j
    return None, None

def valid(b, r, c, num):
    if num in b[r]: return False
    if num in [b[x][c] for x in range(9)]: return False
    rs, cs = 3*(r//3), 3*(c//3)
    for i in range(rs, rs+3):
        for j in range(cs, cs+3):
            if b[i][j] == num: return False
    return True

def solve_sudoku(b):
    r, c = find_cell(b)
    if r is None: return True
    for n in range(1,10):
        if valid(b, r, c, n):
            b[r][c] = n
            if solve_sudoku(b): return True
            b[r][c] = 0
    return False

sudoku = [
 [5,3,0,0,7,0,0,0,0],
 [6,0,0,1,9,5,0,0,0],
 [0,9,8,0,0,0,0,6,0],
 [8,0,0,0,6,0,0,0,3],
 [4,0,0,8,0,3,0,0,1],
 [7,0,0,0,2,0,0,0,6],
 [0,6,0,0,0,0,2,8,0],
 [0,0,0,4,1,9,0,0,5],
 [0,0,0,0,8,0,0,7,9]
]

solve_sudoku(sudoku)
print("\nSolved Sudoku:")
for row in sudoku: print(row)


# ============================
# MAP COLORING WITH FORWARD CHECKING
# ============================

def safe_color(r, col, assign, neigh):
    return all(assign.get(n) != col for n in neigh[r])

def fc_color(assign, dom, r, col, neigh):
    nd = {x:set(dom[x]) for x in dom}
    for n in neigh[r]:
        nd[n].discard(col)
    return nd

def backtrack(assign, dom, neigh, colors):
    if len(assign) == len(dom): return assign
    r = next(x for x in dom if x not in assign)
    for col in dom[r]:
        if safe_color(r, col, assign, neigh):
            assign[r] = col
            res = backtrack(assign, fc_color(assign, dom, r, col, neigh), neigh, colors)
            if res: return res
            del assign[r]
    return None

neighbors = {
 'WA':['NT','SA'], 'NT':['WA','SA','Q'], 'SA':['WA','NT','Q','NSW','V'],
 'Q':['NT','SA','NSW'], 'NSW':['Q','SA','V'], 'V':['SA','NSW'], 'T':[]
}

colors = ['Red','Green','Blue']
domains = {r:set(colors) for r in neighbors}

sol = backtrack({}, domains, neighbors, colors)
print("\nMap Coloring Solution:", sol)
