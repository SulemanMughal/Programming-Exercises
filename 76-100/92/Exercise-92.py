probabilities = [0.21, 0.91, 0.34, 0.55, 0.76, 0.02]
result = []
    
for prob in probabilities:
    if prob > 0.5:
        result.append(1)
    else:
        result.append(0)
    
print(result)