#1
def number_of_food_groups():
    return 5
print(number_of_food_groups())
# pred outpur -> 5

#2
def number_of_military_branches():
    return 5
print(number_of_days_in_a_week_silicon_or_triangle_sides() + number_of_military_branches())
# pred output -> error becuase number of days... is not defined

#3
def number_of_books_on_hold():
    return 5
    return 10
print(number_of_books_on_hold())
# pred output -> 5 because after the first return the function stops


#4
def number_of_fingers():
    return 5
    print(10)
print(number_of_fingers())
#pred output -> 5 beacuse after the return the function stops


#5
def number_of_great_lakes():
    print(5)
x = number_of_great_lakes()
print(x)
# pre output -> 5 becuase we print the function at number 5 and we store the value inside the variable x , then we print x that is 5


#6
def add(b,c):
    print(b+c)
print(add(1,2) + add(2,3))
#pred output -> 3,5,error because in the print outside the function we call it two times, so we print the sum of 1and2, and the sum of 2and3; 
# then, since the values weren't returned, we got an error since we're adding to empty boxes basically


#7
def concatenate(b,c):
    return str(b)+str(c)
print(concatenate(2,5))
#pred output -> 25 because since we make the number a string and concatenating the two strings, 2+5 is 25 an not 7


#8
def number_of_oceans_or_fingers_or_continents():
    b = 100
    print(b)
    if b < 10:
        return 5
    else:
        return 10
    return 7
print(number_of_oceans_or_fingers_or_continents())
# pred output -> 100,10 beacuse when we call the function in the mprint statement, we print b. Then, since b is greater than 10, we print the first return statement and the function stops. the second return statement is not calculated 


#9
def number_of_days_in_a_week_silicon_or_triangle_sides(b,c):
    if b<c:
        return 7
    else:
        return 14
    return 3
print(number_of_days_in_a_week_silicon_or_triangle_sides(2,3))
print(number_of_days_in_a_week_silicon_or_triangle_sides(5,3))
print(number_of_days_in_a_week_silicon_or_triangle_sides(2,3) + number_of_days_in_a_week_silicon_or_triangle_sides(5,3))
# pred output -> 7,14,21 beacuse in the first print, b<c so we print the if return; in the second print, we print the else return since b>c; in the third print, we sum the first two print


#10
def addition(b,c):
    return b+c
    return 10
print(addition(3,5))
# pred output -> 8  beacuse we stop at the first return


#11
b = 500
print(b)
def foobar():
    b = 300
    print(b)
print(b)
foobar()
print(b)
# pred output -> 500,500,300,500 becuase we print the first b, then the second print with the original b, then we call the function and we print the new b;
# last we print the third original b


#12
b = 500
print(b)
def foobar():
    b = 300
    print(b)
    return b
print(b)
foobar()
print(b) 
# pred output -> 500,500,300,500 beacuse we print the first b, then the second original b, then we call the function and we print the new b;
# last we print the last line with the original value since the return wasn't stored in the old b


#13
b = 500
print(b)
def foobar():
    b = 300
    print(b)
    return b
print(b)
b=foobar()
print(b)
# pre output -> 500,500,300,300 beacuse we print the first b, then the print outside the function with the original b, 
# then we call the function and we print the new value of b and since we stored the new value inside the variable b, we print the new value again


#14
def foo():
    print(1)
    bar()
    print(2)
def bar():
    print(3)
foo()
# pred output -> 1,3,2 beacuse we call the foo function, we print 1, then we call the bar functiona dn we print 3, for last we continue the foo function and print 2


#15
def foo():
    print(1)
    x = bar()
    print(x)
    return 10
def bar():
    print(3)
    return 5
y = foo()
print(y)
# pred output -> 1,3,5,10 , beacuse we call the foo function so we print 1, than we call the bar function so we print 3, 
# then x = to the return value of bar (5), so we print 5; for last we print the return value of foo (10)