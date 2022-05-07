def count_down(c):
    res = []
    for x in range(c +  1): 
        res.append(x)
    res.sort(reverse = True)
    return res
print(count_down(5))
 

def print_and_return(x):
    fb = x 
    print(fb[0])
    return fb[1]
b=print_and_return([1, 2])
print(b)



def first_plus_length(list):
    firstvalue = list[0]
    lastvalue = len(list)
    result = firstvalue + lastvalue
    return result
print (first_plus_length([1,2,3,4,5]))


def values_greater_than_second(list):
    if len(list) < 2:
        return False
    x = [] 
    for y in list:
        if y > list[1]:
            x.append(y)
    print(len(x))
    return x 

print(values_greater_than_second([5,2,3,2,1,4]))
print(values_greater_than_second([3]))

def length_and_value(size, value):
    result = []
    for x in range(size):
        result.append(value)
    return result

print(length_and_value(4, 7))
print(length_and_value(6, 2))
