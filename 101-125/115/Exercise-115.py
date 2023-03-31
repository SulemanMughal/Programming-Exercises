numbers = list(range(1, 20))
even = [number for number in numbers if number % 2 == 0]
    
with open('num.txt', 'w') as file:
    for num in even:
        file.write(str(num) + '\n')