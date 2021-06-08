#1
def number_of_food_groups():
    return 5
print(number_of_food_groups())
# output would be 5

#2
def number_of_military_branches():
    return 5
print(number_of_days_in_a_week_silicon_or_triangle_sides() + 
number_of_military_branches())
# output would be 5

#3
def number_of_books_on_hold():
    return 5
    return 10
print(number_of_books_on_hold())
# output would be 5

#4
def number_of_fingers():
    return 5
    print(10)
print(number_of_fingers())
# output would be 5

#5
def number_of_great_lakes():
    print(5)
x = number_of_great_lakes()
print(x)
#output would print 5 none as there is no return in the fucntion

#6
def add(b,c):
    print(b+c)
print(add(1,2) + add(2,3))
# output is 3,5 none as there is no return in the function

#7
def new_func():
    def concatenate(b,c):
        return str(b)+str(c)
    print(concatenate(2,5))
    return new_func()
    # output would be 25 as the parameters becomes strings

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
# output would be 100 and print 10 when called


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



#10
def addition(b,c):
    return b+c
    return 10
print(addition(3,5))
# output would be 8 because 3&5 were passed in


#11
b = 500
print(b)
def foobar():
    b ="keyword operator from-rainbow">= 300
    print(b)
print(b)
foobar()
print(b)
#output prints 500 500 300 500


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
# output print 500 500 300 500 and returns 300 


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
#output would rpint 500 500 300 300


#14
def foo():
    print(1)
    bar()
    print(2)
def bar():
    print(3)
foo()
# output would be 1 2 3

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
# output should print 1 3 and return 5 and 10 to be as variables