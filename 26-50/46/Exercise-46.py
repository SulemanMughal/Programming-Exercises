text = 'Programming in python.'
text = text.lower()
text = text.replace(' ', '')
text = text.replace('.', '')
vowels = {'a', 'e', 'i', 'o', 'u'}
letters = set(text)
consonants = letters.difference(vowels)
print(f'Number of items: {len(consonants)}')