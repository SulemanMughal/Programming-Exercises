

desc = "Playway: Playway is a producer of computer games."
word_list = desc.lower().replace(':', '').replace('.', '').split()
word_unique = {word for word in word_list}
print(len(word_unique))