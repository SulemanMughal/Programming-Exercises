project_ids = {
    '01': 'open', 
    '02': 'new',
    '03': 'in progress',
    '04': 'completed'
}
    
if project_ids['02'] == 'new':
    project_ids['02'] = 'open'
    
print(project_ids)