L=[1,2,2,[3,3,4,5],6,6,7,[7,8,9]]

#Nested List to Flattened List

def flattened_list(L):
    Flattened=[]
    for i in L:
        if i not in Flattened:
            if isinstance(i,list):
                Flattened.extend(flattened_list(i))
            else:
                Flattened.append(i)
    return len(list(set(Flattened)))

Flattened=flattened_list(L)

print("The Flattened List:", Flattened)