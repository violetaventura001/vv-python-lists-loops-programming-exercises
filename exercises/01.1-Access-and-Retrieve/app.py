
my_list = ['sunday','monday','tuesday','wednesday','thursday','friday','saturday']

# 1. print the item here
print(my_list[2])
# 2. change the position were 'thursday' is to None
my_list[4] = ('None')
print(my_list[4])
# 3. print that position now here
index = my_list.index('None')
print('The index of none:', index)