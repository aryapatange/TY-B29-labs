# Certainty Factor (CF) Combination

def combine(cf1, cf2):
    # Standard CF rules
    if cf1 > 0 and cf2 > 0: return cf1 + cf2 - cf1*cf2
    if cf1 < 0 and cf2 < 0: return cf1 + cf2 + cf1*cf2
    return (cf1 + cf2) / (1 - min(abs(cf1), abs(cf2)))

def combine_all(cfs):
    result = cfs[0]
    for cf in cfs[1:]:
        result = combine(result, cf)
    return result

# Example 1: Medical Diagnosis
cfs1 = [0.7, 0.6, 0.5]
final1 = combine_all(cfs1)
print("Flu CF:", final1, "| Confidence:", final1*100, "%")

# Example 2: Mixed Evidence
cfs2 = [0.8, -0.3, 0.5]
final2 = combine_all(cfs2)
print("Mixed CF:", final2, "| Confidence:", final2*100, "%")
