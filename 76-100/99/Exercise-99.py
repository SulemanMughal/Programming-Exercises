hashtags = ['holiday', 'sport', 'fit', None, 'fashion']
result = True
    
for hashtag in hashtags:
    if not isinstance(hashtag, str):
        result = False
        break
    
print(result)