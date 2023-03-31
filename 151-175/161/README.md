# Exercise No. 161

The contents of the file plw.txt were loaded as follows:


    with open('plw.txt', 'r') as file:
        lines = file.read()


lines variable:


    "PLAYWAY\n\nPlayWay is a producer and publisher of computer and mobile games. The company is characterized by a very large number of development teams and a large number of games produced simultaneously.\nPlayWay sells, among others via the STEAM portal, AppStore and GooglePlay. The US and German markets are the two largest markets for the Group's sales.\nIn addition, the company has PlayWay Campus - a campus for cooperating development teams."


**Tasks to perform:**

    1. Change uppercase letters to lowercase

    2. Remove commas and periods

    3. Split the text into tokens

    4. Extract words with minimum 8 characters length

    5. Sort the words alphabetically


Print the result to the console.


**Expected result:**


    ['addition', 'appstore', 'characterized', 'computer', 'cooperating', 'development', 'development', 'googleplay', 'produced', 'producer', 'publisher', 'simultaneously']


