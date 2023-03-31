omega = {
    (x, y, z) 
    for x in range(1, 7) 
    for y in range(1, 7) 
    for z in range(1, 7)
}
a = {
    (x, y, z) 
    for x, y, z in omega 
    if x % 2 != 0 and y % 2 != 0 and z % 2 != 0
}
prob = round(len(a) / len(omega), 4)
print(f'Probability: {prob}')