items = [1, 5, 3, 2, 2, 4, 2, 4]
result = []
    
for item in items:
    if not item in result:
        result.append(item)
        
print(result)