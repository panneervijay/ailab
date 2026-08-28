def unity(x,y,subset={});
    if x==y:
        return subset
    elif isintance(x,str)and x.islower():
        return(x:y)
    elif isintance(y,str)and y.islower():
        return(y:x)
    else:
        return Node
    
     
