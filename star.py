def main():
    number=getnumber()
    call(number)

def getnumber():
    while True :

     n=int(input("whats n?"))
     if n<0:
        break 
     return n 
def call(n):
    for i in range(n):
        print("hi")

main()