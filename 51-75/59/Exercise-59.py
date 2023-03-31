text = 'Python programming'
text = text.lower()
characters = list(set(text))
characters.remove(' ')
characters.sort()
print(characters)