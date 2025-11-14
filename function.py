def add(a,b):
    return a+b

result = add(3,8)
print(result)

def calculate_expression(a,b,c):
   return a + b * 2 ** 2 - (6 / c)

sum = calculate_expression(3,4,3)
print(sum)

def calculate_expression_2(a,b,c):
    return a+b*c
print(calculate_expression_2(2,5,3))


def calculate_expression_3(a,b,c):
    return (a+b)*c
print(calculate_expression_3(2,5,3))

#Function for Exponentiation
def exponentiation(base,power):
    return base ** power 
print(exponentiation(2,6))

#Function for Roots
def roots(number, n ):
    return number ** (1/n)
print(roots(27,3))