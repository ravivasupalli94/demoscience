
username='ravi'
password='ravi123'

k_name=input("Enter your username:")
k_pass=str(input("Enter your password:"))

if k_name==username and k_pass==password:
    print('''
    1. deposite
    2. withdraw
    3. mini_statement
    4. exit
    ''')
    amount=45000
    option=int(input("select your option:"))
    if option==1:
        dep=int(input("Enter the amount"))
        amount+=dep
        print("Total amount:",amount)
    elif option==2:
        withd=int(input("Enter the amount:"))
        amount-=withd
        print("Total amount",amount)
    elif option==3:
        print("=====ATM=====")
        print("username:",username)
        print("Total amount:",amount)
        print("Thanks for ravi")
        print("====================")
    elif option==4:
        exit()
else:
    print("please enter correct pin ")
