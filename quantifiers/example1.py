# Universal: -VxEz(x^2 >= 0) in python

def ex1():
    for x in range(-100, 100):
        if not(x**2 >= 0):
            return False
        return True

print(ex1())

