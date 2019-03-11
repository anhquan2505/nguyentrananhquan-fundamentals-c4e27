def get_even_list(a):
    for i in list(a):
        if i%2 != 0:
            a.remove(i)
    return(a)
a=[1,3,3,4,9,10,21]
print(get_even_list(a))
           