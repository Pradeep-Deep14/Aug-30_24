A=[1,2,3,4,5]
B=[]
#solution 1
def reversed_list(lst):
    for i in A:
        B.insert(0,i)
    return B
print(reversed_list(A))
#solution 2

def reversed_listt(lst):
    B=A[::-1]
    return B

print(reversed_listt(B))