def get_even_list(a):
    for i in list(a):
        if i % 2 != 0:
            a.remove(i)
    return(a)

even_list = get_even_list([1, 2, 5, 9, -10, 6])

if set(even_list) == set([2, -10, 6]):
    print("Your function is correct")
else:
    print("Ooops, bugs detected")
    