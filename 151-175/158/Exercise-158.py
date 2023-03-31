pv = 1000
n = 10
rate = [0.01, 0.02, 0.03, 0.04, 0.05, 0.06, 0.07]
fvs = [round(pv * (1 + r)**n, 2) for r in rate]
print(fvs)