text = 'Python is a very popular programming language'
    
words = text.split(' ')
result = []
for idx, word in enumerate(words):
    if idx < 4:
        result.append(word.lower())
print(result)