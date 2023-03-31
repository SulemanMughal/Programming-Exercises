items = [(3, 4), (2, 5), (1, 4), (6, 1)]
items.sort(key=lambda item: item[0]**2 + item[1]**2)
print(items)