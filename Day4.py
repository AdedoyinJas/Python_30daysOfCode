a = {  0 : '0'  , 1: '1', 2 : '2' , 3: '3' ,4 : '4' , 5 : '5' ,6 : '6' , 7 : '7' ,8 : '8' ,
 9 : '9' , 10 : 'A', 11 : 'B' , 12 : 'C' , 13 : 'D', 14 : 'E' , 15 : 'F' }


val = input("enter number:")
remainder = val % 16
real = val//16
def decitohexa(val):
    try:
        if val > 0:
            return str(real) + str(a[remainder])
    
    except:
        return "You entered a string"


print(decitohexa(val))