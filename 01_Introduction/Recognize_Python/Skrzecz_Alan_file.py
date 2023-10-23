num1 = 42  # variable declaration , Number , Integer
num2 = 2.3 # variable declaration , Number, Float
boolean = True # variable declaration , Boolean
string = 'Hello World' # variable declaration , String
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives'] # variable declaration , List initialize
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False} # variable declaration , Dictionary initialize
fruit = ('blueberry', 'strawberry', 'banana') # variable declaration , Tuple initialize
print(type(fruit)) # log statement ,  type check
print(pizza_toppings[1]) # log statement, access value of the List
pizza_toppings.append('Mushrooms') # add value on the List
print(person['name']) # log statement, access value of the Dictionary
person['name'] = 'George' # change value of the Dictionary
person['eye_color'] = 'blue' # add value to the Dictionary
print(fruit[2]) # log statement , access value of the Tuple

if num1 > 45: # conditional, if
    print("It's greater") # log statement , since num1 is less than 45 is gonna move to the else
else: # conditional, else
    print("It's lower") #log statement , num1 is less thatn 45 so It' lower is the result

if len(string) < 5: # conditional, if length of string is less than 5
    print("It's a short word!") #log statement, move to the elif cause length is 11
elif len(string) > 15: # coditional, elif the length is more than 15
    print("It's a long word!") # log statement, move to the else cuase the length is 11
else: # conditional, else , run when either if and elif are true
    print("Just right!") # log statement, prints "Just right!" cause the length is 11

for x in range(5): # for loop, starts at 0(inclusive) , finishes at 4 (5 exclusive)
    print(x) # log statement , prints 0,1,2,3,4
for x in range(2,5): # for loop, starts at 2(inclusive), ends at 4 (5 exclusive)
    print(x) # log statement , prints 2,3,4
for x in range(2,10,3): # for loop, starts at 2(inclusive), have increment of 3 and ends at 10
    print(x) # log statement, prints 2,5,8
x = 0 # variable declaration
while(x < 5): # while loop , starts at 0 and ends at 4
    print(x) # log statement , prints 0,1,2,3,4
    x += 1 # increment by 1

pizza_toppings.pop() # remove last value of the List = Mushroom
pizza_toppings.pop(1) # remove value at index 1 of the List = Sausage

print(person) # log statement, prints the Dictionary
person.pop('eye_color') # delete value of the Dictionary
print(person) # log statement, prints the Dictionary without the pooped element

for topping in pizza_toppings:  #for loop, checks every value of the List
    if topping == 'Pepperoni': # if statement, check if the topping is equal to Pepperoni
        continue # if the value is equal to Pepperoni,continue and go back to the if statement but for the next index
    print('After 1st if statement') # second value is Jalapenos and third value is Cheese, so it print two times 'After 1st statement' 
    if topping == 'Olives': # since the last value is equal to Olives we go to the next line
        break # we break the function, we have the statement printed two times

def print_hello_ten_times(): # function is defined
    for num in range(10): # for loop , starts at 0 , ends at 9
        print('Hello') # log statement , prints Hello

print_hello_ten_times() # the functtion is called , the Hello is printed 10 times

def print_hello_x_times(x): # function is defined
    for num in range(x): # range is from 0 to x(exclusive)
        print('Hello') #log statement, prints Hello

print_hello_x_times(4) # functiuon is called , it prints Hello 4 times

def print_hello_x_or_ten_times(x = 10): # function in defined 
    for num in range(x): # for loop , starts at 0(inclusive) at ends at 9 (10,the given value, exclusive)
        print('Hello') #log statement, prints Hello

print_hello_x_or_ten_times() # function is called, the value of x remains 10 , prints Hello 10 times
print_hello_x_or_ten_times(4) # function is called, the new value for x is 4, prints Hello 4 times


"""
Bonus section
"""

# print(num3)                    - NameError: name <variable name> is not defined 
# num3 = 72                      # the variable should be declared before the line print(num3)
# fruit[0] = 'cranberry'         - TypeError: 'tuple' object does not support item assignment
# print(person['favorite_team']) - KeyError: 'favorite_team'
# print(pizza_toppings[7])       - IndexError: list index out of range
#   print(boolean)               - IndentationError: unexpected indent
# fruit.append('raspberry')      - AttributeError: 'tuple' object has no attribute 'append'
# fruit.pop(1)                   - AttributeError: 'tuple' object has no attribute 'pop'
