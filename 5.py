L=[1,2,2,3,3,4,5,6,6,7]

#Remove duplicates and unique elements separately from this list

def split_unique_duplicate_elements(lst):
    seen=set()
    unique_list=[]
    duplicate_list=[]
    for i in L:
        if i not in seen:
            unique_list.append(i)
            seen.add(i)
        else:
            duplicate_list.append(i)
    return unique_list,duplicate_list

unique_list,duplicate_list=split_unique_duplicate_elements(list)

print(f"The Unique List is :",unique_list)
print(f"The Duplicate List is :",duplicate_list)