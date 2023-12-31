# 1.Countdown - Create a function that accepts a number as an input. Return a new list that counts down by one, from the number (as the 0th element) down to 0 (as the last element).
#   Example: countdown(5) should return [5,4,3,2,1,0]

list = []
def count_list(top):
    for number in range(top,0,-1):
        list.append(number)
    return list    
print(count_list(8))

# 2.Print and Return - Create a function that will receive a list with two numbers. Print the first value and return the second.
#   Example: print_and_return([1,2]) should print 1 and return 2

def split_action(list):
    print(list[0])
    return list[1]
print(split_action([6,8]))

# 3.First Plus Length - Create a function that accepts a list and returns the sum of the first value in the list plus the list's length.
#   Example: first_plus_length([1,2,3,4,5]) should return 6 (first value: 1 + length: 5)

def fpl(list):
    for ind in range(0,len(list)-1,1):
        sum_first_length= list[0]+ len(list)
    return sum_first_length
print(fpl([6,5,1,4,2,8,11,3]))    

# 4.Values Greater than Second - Write a function that accepts a list and creates a new list containing only the values from the original list that are greater than its 2nd value. Print how many values this is and then return the new list. If the list has less than 2 elements, have the function return False
#   Example: values_greater_than_second([5,2,3,2,1,4]) should print 3 and return [5,3,4]
#   Example: values_greater_than_second([3]) should return False
list3 = []
def greater_than_second(list):
    for index in range(0,len(list),1):
        if len(list) < 2:
            return False
        if list[index]> list[1]:
            list3.append(list[index])
    return list3
print(greater_than_second([4,2,1,5,2,7,1]))
print(greater_than_second([9]))

# 5.This Length, That Value - Write a function that accepts two integers as parameters: size and value. The function should create and return a list whose length is equal to the given size, and whose values are all the given value.
#   Example: length_and_value(4,7) should return [7,7,7,7]
#   Example: length_and_value(6,2) should return [2,2,2,2,2,2]


def len_val(a,b):
    arr_num = []
    for bers in range(0,a):
        arr_num.append(b)
    return arr_num
print(len_val(5,9))
print(len_val(12,2))
