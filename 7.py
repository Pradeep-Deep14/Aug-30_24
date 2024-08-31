input_list = ['apple,orange', 'banana,grape', 'watermelon']

for item in input_list:
    for fruit in item.split(','):
        print(fruit)