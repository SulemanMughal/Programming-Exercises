with open('plw.txt', 'r') as file:
    lines = file.read().splitlines()
    
lines = [line for line in lines if len(line) > 0]
lines = [line.split() for line in lines]
print(lines)