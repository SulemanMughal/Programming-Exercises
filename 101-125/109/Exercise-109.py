users = {'001': 'Mark', '002': 'Monica', '003': 'Jacob'}
user_id = '004'
    
try:
    print(users[user_id])
except KeyError:
    print(f'The {user_id} key is not in the dictionary. Adding key ...')
    users[user_id] = None
print(users)