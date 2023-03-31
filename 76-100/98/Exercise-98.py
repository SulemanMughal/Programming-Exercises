list1 = [1, 2, 0]
list2 = [4, 5, 6, 1]
result = False
    
for item1 in list1:
    if item1 in list2:
        result = True
        break
    
print(result)