def  count(num):
    newList = []
    for x in range(num, -1, -1):
        newList.append(x)
    return newList
print(count(20))


def print_return(list):
    print(list[0])
    return list[1]
print (print_return([10,50]))


def first_plus_length(list):
    print(list[0])
    return len(list)
print(first_plus_length([45,46,2]))



def values_greater_than_second(list):
    if len(list)<2:
        return False
    newList = []
    for val in list:
        if val>list[1]:
            newList.append(val)
    print(len(newList))    
    return newList
print(values_greater_than_second([40,5,3,6,90,78,20,1]))
print(values_greater_than_second([40,1,3,6,90,78,20,1]))
print(values_greater_than_second([1]))
print(values_greater_than_second([]))


def length_and_value(size,value):
    newList = []
    for x in range(size):
        newList.append(value)
    return newList
print(length_and_value(5,11))