# Alex Rapp
# UWYO COSC 1010
# 10/05/2024
# Lab 08
# Lab Section:11
# Sources, people worked with, help given to:
# lecture slides, past assignments
# lab TA's
# N/a


# Write a function that will properly check strings to see if they are an int or float, and convert them if so
# If they can't be converted return false
# Other wise return the converted int or float 
# Floats should only have one decimal point in them 
left = 0
right = 0
ans = 0
def inint(num=input('what is your number?')):
        if '.' in num:
            left,right = num.split('.',1)
            if '.' in right:
                return False
            elif right.isnumeric() == False:
                return False
            elif left.lstrip('-').isnumeric() == False:
                return False
            else:
                if int(left)>=0:
                    ans = int(left) + int(right)/(10**len(right))
                else:
                    ans = int(left) - int(right)/(10**len(right))
                return ans
        elif num.lstrip('-').isnumeric() == False:
            return False
        else:
            ans = int(num)
            return ans
ans = inint()
print(ans)

print("*" * 75)

# just wondering if anyone cares point slope form is (y-y1) = m(x-x1)

# Point-slope y = mx + b
# This is used in mathematics to determine what the value y would be for any given x
# Where b is the y-intercept, where the line crosses the y-axis (x = 0)
# m is the slope of the line, the rate of change, how steep the line is
# x is the variable, and is determined by which point on the graph you wish to evaluate
# Create a function slope_intercept that takes in four parameters
    # m, the slope
    # b, the intercept
    # a lower x bound
    # an upper x bound
# Return a list for all values of y for the given x range, inclusive (whole number X's only)
# Check to make sure that the lower bound is less than or equal to the upper bound
# m, b can be floats or integers
# the bounds must be integers, if not return false

# Create a while loop to prompt users for their input for the four variables
# Exit on the word exit
# Remember all inputs are strings, but the function needs ints or floats
# Call your function and print the resulting list

left = 0
right = 0
ans = 0
def inint(num=input('what is your number?')):
        if '.' in num:
            left,right = num.split('.',1)
            if '.' in right:
                return False
            elif right.isnumeric() == False:
                return False
            elif left.lstrip('-').isnumeric() == False:
                return False
            else:
                if int(left) == 0 and int(right) == 0:
                    return 'a'
                elif int(left)>=0:
                    ans = int(left) + int(right)/(10**len(right))
                else:
                    ans = int(left) - int(right)/(10**len(right))
                return ans
        elif num.lstrip('-').isnumeric() == False:
            return False
        elif num == '0':
            return 'a'
        else:
            ans = int(num)
            return ans

def slope_intercept(m,b,xl,xu,yvals=[]):
    if inint(m) != False and inint(b) != False and inint(xl) != False and inint(xu) != False:
        m=inint(m)
        b=inint(b)
        xl=inint(xl)
        xu=inint(xu)
        if m == 'a':
            m = 0
        if b == 'a':
            b = 0
        if xl == 'a':
            xl = 0
        if xu == 'a':
            xu = 0
        if xl <= xu:
            for i in range(xl,xu+1):
                y=m*i+b
                yvals.append(y)
            return yvals
        else:
            print('invalid input')
            return False
    else:
        print('invalid input')
        return False
run = True
lists = []
x=0
b=0
xl=0
xu=0
yvals=[]
while run == True:
    que = input('what is your slope? \nwhat is your y-intercept? \nwhat is you lower x bound? \nwhat is you upper x bound?\nenter in format m,b,xlower,xupper \nenter exit to end ')
    if yvals != False:
        del yvals[:]
    if que.lower() == 'exit':
        print('thank you')
        run = False
        break
    if ',' in que:
        lists = que.split(',')
        if len(lists) == 4:
            m,b,xl,xu = que.split(',')
            if inint(m) != False and inint(b) != False and inint(xl) != False and inint(xu) != False:
                yvals = slope_intercept(m,b,xl,xu)
                if yvals != False:
                    print(yvals)
                else:
                    print('invalid input')
            else:
                print('invalid input')
        else:
            print('invalid input')
    else:
        print('invalid input')


print("*" * 75)


# Write a function to solve the quadratic formula
# https://en.wikipedia.org/wiki/Quadratic_formula
# Accept inputs for a, b, c
# Remember that this returns two values
# Create a loop like above to prompt the user for input for the three values
# Create a second function that just does the square root operation 
    # If the number you are trying to take the square root of is negative, return null

def sqrt(a='',b='',c='',disc=0,disc2=0):
    disc =  b**2
    disc2 = 4*a*c
    disc = disc -disc2
    if disc >= 0:
        return disc
    else:
        return 'null'


def quadratic(a='',b='',c=''):
    a=inint(a)
    b=inint(b)
    c=inint(c)
    if a != 0:
        if sqrt(a,b,c) != 'null':
            r1=(-b + sqrt(a,b,c))/(2*a)
            r2 =(-b - sqrt(a,b,c))/(2*a)
            return r1,r2
        else:
            return '',''
    else:
        return 'h',''



lis=[]
run = True
while run ==True:
    eq=input('what is your a, b, and c values?\ninputted a,b,c\nenter exit to exit ')
    if eq.lower() == 'exit':
        print('thank you')
        run = False
        break
    if ',' in eq:
        lis = eq.split(',')
        if len(lis) == 3:
            a,b,c = eq.split(',')
            if inint(a) != False and inint(b) != False and inint(c) != False:
                a=str(inint(a))
                b=str(inint(b))
                c=str(inint(c))
                if inint(a) == 'a':
                    a='0'
                if inint(b) == 'a':
                    b='0'
                if inint(c) == 'a':
                    c='0'
                r1, r2 = quadratic(a,b,c)
                if r1 == 'h':
                    print('the a value cannot be zero in the quadratic formula')
                elif r1 != '':
                    print(f'your roots are{r1} and {r2}')
                else:
                    print('There is no real roots')
            else:
                print('invalid input')
        else:
            print('invalid input')
    else:
        print('invalid input')
    
    





    
