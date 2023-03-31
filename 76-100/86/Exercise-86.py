result = []
for i in range(10, 100):
    if i % 11 == 0:
        result.append(str(i))
print(','.join(result))