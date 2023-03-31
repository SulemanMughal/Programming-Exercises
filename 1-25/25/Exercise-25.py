string = '1 0 0 1 0 1'
binary = string[::2]
number = int(binary, 2)
print(f'Number found: {number}')