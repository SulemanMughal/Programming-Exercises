n = 1
pv = 1000
r = 0.04
fv = pv * (1 + r)
    
while fv <= 2000:
    fv = fv * (1 + r)
    n += 1
print(f'Future value: {fv:.2f} USD. Number of periods: {n} years')