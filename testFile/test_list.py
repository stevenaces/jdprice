import copy
l_list = [
    [4699.0, 4799.0, 4688.0],
    [4699.0, 4699.0, 4699.0],
    [5799.0, 5499.0, 5799.0]
]
ll_list = []
l_price = []
item = []
i = 0
j = 0
for l in l_list:
    l_price.clear()
    for price in l:
        l_price.append(price)

    ll_list.append(copy.deepcopy(l_price))

    # j = j + 1

print(ll_list)

