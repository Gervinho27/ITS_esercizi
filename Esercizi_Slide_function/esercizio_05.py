def add_one(numeri):
        add = numeri + 1
        return add

def add_one_to_list(mylist):
    new_list = []
    for popa in mylist:
          new_list.append(add_one(popa))
    print(new_list)


pier = [1, 2, 3]
add_one_to_list(pier)