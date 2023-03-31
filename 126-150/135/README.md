# Exercise No. 135

The following function is defined:


    def function(idx, l=[]):
        for i in range(idx):
            l.append(i ** 3)
        print(l)


Call the function three times as follows:


    function(3)
    function(5, ['a', 'b', 'c'])
    function(6)


Analyze the results!


**Expected result:**


    [0, 1, 8]
    ['a', 'b', 'c', 0, 1, 8, 27, 64]
    [0, 1, 8, 0, 1, 8, 27, 64, 125]


