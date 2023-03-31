import re
    
    
raw_text = "Send an email to info@template.com or sales-info@template.it"
result = re.findall(r"[\w\.-]+@[\w\.-]+", raw_text)
print(result)