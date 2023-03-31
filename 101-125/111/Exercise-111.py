with open('currencies.txt', 'r') as file:
        lines = file.read().splitlines()
    
indexes = [index for index in lines if 'USD' in index]
print(indexes)