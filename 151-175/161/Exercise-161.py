with open('plw.txt', 'r') as file:
    lines = file.read()
    
lines = lines.lower()
lines = lines.replace(',', '').replace('.', '')
tokens = lines.split()
tokens = [token for token in tokens if len(token) > 7]
tokens.sort()
print(tokens)