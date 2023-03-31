gaming = {
    '11B': [362.5, 'PLN'],
    'CDR': [74.25, 'USD'],
    'CIG': [0.85, 'PLN'],
    'PLW': [79.5, 'USD'],
    'TEN': [300.0, 'PLN']
}
    
for ticker, info in gaming.items():
    if info[1] == 'PLN':
        continue
    info[0] = info[0] * 4.0
    info[1] = 'PLN'
print(gaming)