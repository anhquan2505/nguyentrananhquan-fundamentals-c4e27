def is_inside(a,b):
    
    if list(b)[0]<list(a)[0]<list(a)[0]+list(b)[2] and list(b)[1]<list(a)[1]<list(a)[1]+list(b)[3] :
        return(True)
    else:
        return(False)

print(is_inside([5,6],[7,8,9,10]))
