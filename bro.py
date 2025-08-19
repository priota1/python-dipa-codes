def multiply(number1,number2):
     return number1*number2
     
print(multiply(6,8))
def add(*agrs):
     sum=0
     agrs=list(agrs)
     agrs[0]=3
     for i in agrs:
          sum+=i
     return sum
print(add(2,3,4,5,6,7,))
def hello(**names):
     print("hello",end=" ")
     for key, value in names.items():
          print(key,value,end=" ")
hello(tittle="mrs",first="priota",last="banik")