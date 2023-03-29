from loader import *
from classes import Warehouse, Item

stock = Loader(model='stock')
all_wh = stock.objects
w1 = all_wh[0]
w2 = all_wh[1]
w3 = all_wh[2]
w4 = all_wh[3]

for attr, value in stock.__dict__.items():
    print(f"{attr} = {value}")


print(w1.occupancy())
print(w2.occupancy())
print(w3.occupancy())
print(w4.occupancy())

print(w1.occupancy() + w2.occupancy() + w3.occupancy() + w4.occupancy())