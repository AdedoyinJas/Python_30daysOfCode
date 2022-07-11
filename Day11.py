val1 = int(input("Enter value:"))
val2 = int(input('Enter value:'))
def gcd(a , b):
    while True:
        c = a%b
        a = b
        b = c
        if b == 0:
            gcd = a
            return gcd

print(gcd(42,18))




'''a = input("Enter value:")
b = input('Enter value:')
def gcd(a , b):
    while b:
         a,b = b, a%b
    return a

print(gcd(42,18))'''