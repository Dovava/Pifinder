import math
pi = ""
match = "11102020"
pifactor = 2
def ArctanDenom(d):
    tolerance = 1.0e-20
    total = term = 1.0/ d
    n = 0
    while abs(term) > tolerance:
        n += 1
        term /= -d*d
        total += term / (2*n + 1)
    return total
while True:
    pi = str(4*ArctanDenom(pifactor))
    if (pifactor % 1000) == 0:
        print(pifactor)
    result = pi.find(match)
    if (pi.find(match) != -1):
        print(f"Found on index {pifactor+result}")
        break
    else:
        pifactor += 1
