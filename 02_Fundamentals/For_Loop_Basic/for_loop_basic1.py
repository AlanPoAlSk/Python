# 1. Basic - Print all integers from 0 to 150.

# for num in range(0,151):
#     print(num)

num = 0
while num <=150 :
    print(num)
    num+= 1

# 2. Multiples of Five - Print all the multiples of 5 from 5 to 1,000

for num in range(5,151):
    if (num % 5 ==0):
        print(num)

# num = 5
# while num <= 150:
#     if (num % 5 == 0):
#         print(num)
#     num+= 1


# 3. Counting, the Dojo Way - Print integers 1 to 100. If divisible by 5, print "Coding" instead. If divisible by 10, print "Coding Dojo".

for int in range(1,101):
    if(int % 10 == 0):
        print('Coding Dojo')
    elif(int % 5 == 0):
        print('Coding')
    else :
        print(int)

# 4. Whoa. That Sucker's Huge - Add odd integers from 0 to 500,000, and print the final sum.
sum = 0
for odd in range(0,500000):
    if(odd % 2 != 0):
        sum += odd
print(sum)

# 5. Countdown by Fours - Print positive numbers starting at 2018, counting down by fours.

for pos in range(2018,0,-4):
    print(pos)

# 6. Flexible Counter - Set three variables: lowNum, highNum, mult. Starting at lowNum and going through highNum, print only the integers that are a multiple of mult. For example, if lowNum=2, highNum=9, and mult=3, the loop should print 3, 6, 9 (on successive lines)

lowNum = 2
highNum = 55
mult = 7

for multiple in range(lowNum,highNum):
    if (multiple % mult ==0):
        print(multiple)
