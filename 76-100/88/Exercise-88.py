items = [1, 3, 4, 5, 6, 9, 10, 17, 23, 24]
result = []
for item in items:
    if not item % 2 != 0:
        result.append(item)
print(result)