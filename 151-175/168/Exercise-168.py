properties = ['number of companies', 'companies', 'cap']
indeks = ['WIG20', 'mWIG40', 'sWIG80']
    
data = {idx: {i: None for i in properties} for idx in indeks}
print(data)