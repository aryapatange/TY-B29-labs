# Truth Table & Resolution Example (Propositional Logic)

from itertools import product

# implication helper
def implies(p, q): return (not p) or q

# KB: R → W, R
def kb(R, W): return implies(R, W) and R

vars = ['R', 'W']
assignments = product([True, False], repeat=len(vars))

print("Truth Table:")
valid = True

for R, W in assignments:
    kb_val = kb(R, W)
    print(f"R={R}, W={W} | KB={kb_val}, Query={W}")
    if kb_val and not W:     # KB true but query false → fails entailment
        valid = False
        break

print("\nResult:", "KB entails Query" if valid else "Does NOT entail Query")

# simple resolution demonstration
print("\nResolution:")
print("(¬R ∨ W), R ⊢ W")
print("1) (~R ∨ W) and ~W → ~R")
print("2) R and ~R → contradiction")
print("Therefore: KB entails W")
