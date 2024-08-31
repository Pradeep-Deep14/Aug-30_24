L=[1,2,3,4,3,5,4,5]
L1=[]
def duplicate_elements(L):
    for i in L:
        if i not in L1:
            if L.count(i)==1:
                L1.append(i)
    return L1

print(duplicate_elements(L))