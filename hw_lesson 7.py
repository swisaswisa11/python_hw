def crazt_func (number): 

    mylist = []
    for i in range(number):
        if i % 2 == 0 and i % 3 == 0:  
            mylist.append(i)
    return mylist 

print(crazt_func(12))