def function(*args, **kwargs):
    print(args, kwargs)
 
function(3, 4)
function(x=3, y=4)
function(1, 2, x=3, y=4)