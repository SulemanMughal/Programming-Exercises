import json
    
    
stocks = {'PLW': ['Playway', 350], 'BBT': ['Boombit', 22]}
    
with open('stocks.json', 'w') as file:
    json.dump(stocks, file, indent=4)