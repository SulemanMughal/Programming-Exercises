import pickle
    
    
ids = ['001', '003', '011']
    
with open('data.pickle', 'wb') as file:
    pickle.dump(ids, file)