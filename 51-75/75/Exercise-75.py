project_ids = {
    '01': 'open', 
    '03': 'in progress',
    '05': 'in progress',
    '04': 'completed'
}
    
result = list(set(project_ids.values()))
result.sort()
print(result)