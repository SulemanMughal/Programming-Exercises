tax = 0.23
net_price = [5.5, 4.0, 9.0, 10.0]
gross_price = [round(price * (1 + tax), 2) for price in net_price]
print(gross_price)