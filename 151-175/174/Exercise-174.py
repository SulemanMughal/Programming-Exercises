import re
    
    
string = '!@#$%^&45wc'
result = re.findall(pattern=r"\w", string=string)
print(result)