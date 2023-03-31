text = """Python is powerful... and fast
plays well with others
runs everywhere
is friendly & easy to learn
is Open
These are some of the reasons people who use 
Python would rather not use anything else"""
    
words = text.split()
words = [word.lower() for word in words]
words = [word.replace('.', '').replace(',', '') for word in words]
words = [word for word in words if len(word) > 6]
print(words)