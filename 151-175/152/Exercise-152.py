omega = {(x, y) for x in range(1, 7) for y in range(1, 7)}
a = {(x, y) for x, y in omega if x**2 + y**2 >= 45}
prob = round(len(a) / len(omega), 2)
print(f'Probability: {prob}')