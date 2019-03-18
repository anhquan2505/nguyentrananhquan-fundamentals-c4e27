def is_inside(a,b):
    
    if list(b)[0]<=list(a)[0] <=(list(b)[0]+list(b)[2]) and list(b)[1]<=list(a)[1] <=(list(b)[1]+list(b)[3]):
        return(True)
    else:
        return(False)

print(is_inside([168,60],[140,60,100,200]))
