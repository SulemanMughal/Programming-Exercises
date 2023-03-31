# Solution 1

names = ['Jack', 'Leon', 'Alice', None, 'Bob']
    
for name in names:
    if name is None:
        continue
    print(name)


# Solution 2

names = ['Jack', 'Leon', 'Alice', None, 'Bob']
for name in names:
    if not isinstance(name, str):
        continue
    print(name)