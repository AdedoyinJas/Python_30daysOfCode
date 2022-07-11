code1 = input("Enter the USSD code:")
def USSD(code):
    if code == "123":
        num = input("Enter 1 to check account balance.\n Enter 2 to check send money.\n Enter 3 to check purchase airtime.\n Enter number:")
        balance = 60000
        if num == "1":
            password = input('Enter password:')
            if password == "ade":
                print('Your balance is:' + str(balance))
        elif num == "2":
            bank = input('Select 1 for GTB \n Select 2 for UBA \n Select 3 for FCMB \n Select option:')
            account = input("enter account number:")
            amount = int(input('Amount:'))
            password = input('Enter password:')
            if password == "ade":
                print("Your money has been sent and available balance is " + str(balance - amount))
        elif num == "3":
            bank = input('Select 1 for GTB \n Select 2 for UBA \n Select 3 for FCMB \n Select option:')
            phone = input("enter phone number:")
            amount = int(input('Amount of airtime:'))
            password = input('Enter password:')
            if password == "ade":
                print("The airtime has been sent and available balance is " + str(balance - amount))  
        else:
            print('Wrong input') 
    else:
        print('Password is wrong')  

print(USSD(code1))




