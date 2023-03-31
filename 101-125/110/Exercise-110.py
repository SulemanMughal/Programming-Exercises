with open('playway.txt', 'r') as file:
        lines = file.read().splitlines()
    
close = []
for idx, line in enumerate(lines):
    if idx > 0:
        close.append(int(line.split(',')[-2]))
    
close_avg = sum(close) / len(close)
print(f'3-day average closing price: {close_avg:.2f}')