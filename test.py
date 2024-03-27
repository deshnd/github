sum = 723.67
multiple = bool(True)
c=float('Original sum: $'+str(sum))
if (int(c//100) > 1):
    multiple = True
x = (int(c//100), " x $100 bills") if multiple else (int(c//100), " x $100 bill")
print(x)
c = c%100
if (int(c//50) > 1):
    multiple = True
x = (int(c//50), " x $50 bills") if multiple else (int(c//50), " x $50 bill")
print(x)
c = c%50
if (int(c//20) > 1):
    multiple = True
x = (int(c//20), " x $20 bills") if multiple else (int(c//20), " x $20 bill")
print(x)
c = c%20
if (int(c//10) > 1):
    multiple = True
x = (int(c//10), " x $10 bills") if multiple else (int(c//10), " x $10 bill")
print(x)
c = c%10
if (int(c//5) > 1):
    multiple = True
x = (int(c//5), " x $5 bills") if multiple else (int(c//5), " x $5 bill")
print(x)
c = c%5
if (int(c//2) > 1):
    multiple = True
x = (int(c//2), " x $2 bills") if multiple else (int(c//2), " x $2 bill")
print(x)
c = c%2
if (int(c//1) > 1):
    multiple = True
x = (int(c//1), " x $1 bills") if multiple else (int(c//1), " x $1 bill")
print(x)
c = c%1
if (int(c//.50) > 1):
    multiple = True
x = (int(c//.50), " x half-dollar coins") if multiple else (int(c//.50), " x half-dollar coin")
print(x)
c = c%.50
if (int(c//.25) > 1):
    multiple = True
x = (int(c//.25), "quarters") if multiple else (int(c//.25), "quarter")
print(x)
c = c%.25
if (int(c//.1) > 1):
    multiple = True
x = (int(c//.10), "dimes") if multiple else (int(c//.10), "dime")
print(x)
c = c%.10
if (int(c//.5) > 1):
    multiple = True
x = (int(c//.5), "nickles") if multiple else (int(c//.5), "nickle")
print(x)
c = c%.5
if (int(c//.1) > 1):
    multiple = True
x = (int(c//.1), "pennies") if multiple else (int(c//.1), "penny")
print(x)

#running logic in python to understand
