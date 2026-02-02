"""prices = [100,200,300,400,500]
discount = 10

final_price = []

for i in prices:
    # final = i - (i * discount)/100
    final_price.append(i - (i * discount)/100)

print(final_price)"""
import numpy as np 

prices = np.array([100,200,300,400,500])
discount = 10

final_price = prices - ((prices * discount )/ 100)
print(final_price)

p_2d = np.array([[100,200,300],
                 [400,500,600]])

final = p_2d (p_2d * 20 / 100)
print(final)