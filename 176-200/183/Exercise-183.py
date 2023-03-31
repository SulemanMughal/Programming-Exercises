import json
    
    
stocks = {'PLW': 360.0, 'TEN': 320.0, 'CDR': 329.0}
result = json.dumps(stocks, sort_keys=True, indent=4)
print(result)