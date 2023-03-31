omega = {
    (x, y, z) 
    for x in range(1, 7) 
    for y in range(1, 7) 
    for z in range(1, 7)
}
a = {(x, y, z) for x, y, z in omega if (x + y + z) % 7 == 0}
prob = round(len(a) / len(omega), 2)
print(f'Probability: {prob}')