from collections import Counter
    
    
counter = Counter()
items = ['YES', 'NO', 'NO', 'YES', 'EMPTY', 'YES', 'NO']
for item in items:
    counter[item] += 1
print(counter)