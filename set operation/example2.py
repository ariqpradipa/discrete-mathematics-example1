#
# check the input prime number or not
def func():

    n = int(input("Input a number you want to check whether it is prime or not: "))
    
    for i in range(2, int(n/2)+1):
        if (n%i) == 0:
            return False
        else:
            return True

print(func())
