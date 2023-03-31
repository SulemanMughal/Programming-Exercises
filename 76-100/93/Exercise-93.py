items = ['x', 'y', 'z', 'y', 'x', 'y', 'y', 'z', 'x']
    
freq = {}
for item in items:
    if item not in freq.keys():
        freq[item] = 1
    else:
        freq[item] += 1
    
print(freq)