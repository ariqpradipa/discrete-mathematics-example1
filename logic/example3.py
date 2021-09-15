# The implication statement p -> q can either be looked 
# at as equivalent to -p v q or encoded as a function

def implies(p, q):
    if p:
        return q
    else:
        return True 

x = 1
y = 2
print(implies(x >= 0 and y >= 0, x*y >= 0))