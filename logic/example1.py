# A nested loop can be constructed to generate the truth 
# table for standard logic operators such as the and

for p in (True, False):
    for q in (True, False):
        print("%10s %10s %10s" % (p, q, p and q))
