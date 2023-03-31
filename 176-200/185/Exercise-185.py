def mae(y_true, y_pred):
    numerator = sum([abs(i[1] - i[0]) for i in zip(y_true, y_pred)])
    result = numerator / len(y_true)
    return round(result, 3)