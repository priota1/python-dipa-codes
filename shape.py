n=int(input("enter a number:"))
def main():
    
    print_triangle(n)

def print_triangle(n):
    for i in range(n):
            for j in range(n-i-1):
                 print(" ",end="")
            for j in range(i+1):
                 print("#",end=" ")
            print()            
            

main()