number = 13
    
if number > 1:
    for i in range(2, number):
        if number % i == 0:
            print(f'{number} - not a prime number')
            break
    else:
        print(f'{number} - prime number')
else:
    print(f'{number} - not a prime number')