def function(idx, l=[]):
    for i in range(idx):
        l.append(i ** 3)
    print(l)
    
function(3)
function(5, ['a', 'b', 'c'])
function(6)