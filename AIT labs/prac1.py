#water jug
m, n = 4, 3      # capacities
jug1, jug2 = 0, 0
goal = 2

print(f"Start: ({jug1}, {jug2})")

while jug1 != goal and jug2 != goal:
    if jug1 == 0:
        jug1 = m
        print(f"Fill Jug1: ({jug1}, {jug2})")
    elif jug2 == n:
        jug2 = 0
        print(f"Empty Jug2: ({jug1}, {jug2})")
    else:
        transfer = min(jug1, n - jug2)
        jug1 -= transfer
        jug2 += transfer
        print(f"Pour Jug1 → Jug2: ({jug1}, {jug2})")

print(f"Goal reached: ({jug1}, {jug2})")
