def even(list):
    evens = []
    for i in list:
        if i%2==0:
            evens.append(i)
    return evens
print(even([1,2,3,4,5,6,7,8,9]))
