L=[1,2,5,6,8,10,12]

def missing_elements(L):
    L1=[]
    for i in range(1,16):
        if i not in L:
            L1.append(i)
    return L1
count=len(missing_elements(L))
print(count)