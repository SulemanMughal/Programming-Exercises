import re
    
    
string = 'Python 3.8'
result = re.findall(pattern=r"\d", string=string)
print(result)