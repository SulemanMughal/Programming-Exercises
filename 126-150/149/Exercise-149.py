def dayname(index):
    index = index % 7
    days = ['pon', 'wt', 'śr', 'czw', 'pt', 'sb', 'nd']
    yield days[index - 1]
    yield days[index]
    yield days[(index + 1)]