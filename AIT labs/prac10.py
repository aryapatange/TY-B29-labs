# Fuzzy Logic Fan Speed Controller (Temp + Humidity)

def tri(x, a, b, c):
    if x <= a or x >= c: return 0
    return (x-a)/(b-a) if x <= b else (c-x)/(c-b)

def fuzz_temp(t):
    return {
        'cold': tri(t, 0, 5, 15),
        'warm': tri(t, 10, 17.5, 25),
        'hot':  tri(t, 20, 27.5, 35)
    }

def fuzz_hum(h):
    return {
        'low': tri(h, 0, 20, 40),
        'med': tri(h, 30, 50, 70),
        'high':tri(h, 60, 80, 100)
    }

def rules(temp, hum):
    return [
        ('off',   min(temp['cold'], hum['low'])),
        ('low',   min(temp['warm'], hum['low'])),
        ('med',   min(temp['warm'], hum['med'])),
        ('low',   min(temp['hot'],  hum['low'])),
        ('med',   min(temp['hot'],  hum['med'])),
        ('high',  min(temp['hot'],  hum['high']))
    ]

def defuzz(rules_fired):
    centers = {'off':0, 'low':30, 'med':60, 'high':90}
    num = sum(centers[l]*v for l,v in rules_fired)
    den = sum(v for _,v in rules_fired)
    return num/den if den else 0

def control(temp, hum):
    ft = fuzz_temp(temp)
    fh = fuzz_hum(hum)
    rf = rules(ft, fh)
    return defuzz(rf)

# Test values
tests = [(10,30),(18,45),(28,75),(5,20),(32,90)]
for t,h in tests:
    print(f"T={t}C  H={h}% → Fan={control(t,h):.2f}%")
