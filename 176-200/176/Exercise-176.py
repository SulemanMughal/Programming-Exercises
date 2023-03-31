import re
    
    
text = 'Programming in Python - from A to Z'
result = re.split(pattern=r"\s+", string=text)
print(result)