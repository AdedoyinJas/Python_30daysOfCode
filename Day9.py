def is_prime(number):
    number = int(input("Your number:"))
    if number > 1:
        for i in range(2,number):
            if (number % i) == 0:
                print(number , "is not a prime number")
        else:
             print(number , "is a prime number")
    
    else:
        print(number , "is a not prime number")

print(is_prime(9))














#for i in range(2,5):
    #print (i)