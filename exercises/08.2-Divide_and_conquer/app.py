list_of_numbers = [4,	80,	85,	59,	37,25,	5,	64,	66,	81,20,	64,	41,	22,	76,76,	55,	96,	2,	68]


#Your code here:
def merge_two_list(num_list):

    odd = []
    even = []

    for num in list_of_numbers:
        if (num % 2) == 0:
             #            print("{0} is Even".format(num))
             even.append(num)
             #print(even)
        else:
            #print("{0} is Odd".format(num))
            odd.append(num)
            #print(odd)

    for num in even:
        odd.append(num)
    return odd

print(merge_two_list(list_of_numbers))

