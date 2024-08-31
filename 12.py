#Reverse  a string and remove duplicate

input_string="pradeep"

def reverse_remove_duplicates(input_string):
    reversed_string=""
    seen_characters=set()
    for i in range((len(input_string)-1),-1,-1):
        if input_string[i] not in reversed_string:
            reversed_string+=input_string[i]
            seen_characters.add(input_string[i])
    return reversed_string

print(reverse_remove_duplicates(input_string))