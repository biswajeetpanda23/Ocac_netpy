import time

with open ( 'mainbal.txt' , 'r' ) as fptr :
        mainbal = int ( fptr . read () )
        fptr . close ()


with open ( 'password.txt' , 'r' ) as fptr :
        password = int ( fptr . read () )
        fptr . close ()

print("please insert your card")

time.sleep(3)



pin=int(input("enter your pin : "))


if pin == password:
    while True:
         
     print("""
           
           1==mainbal.txt
           2==withdraw balance
           3==deposit balance
           4==exit
          """
         )
     try:
        option=int(input("please enter your choice :  "))
     except:
        print("please enter valid option")

     if option==1:
        print(f"your current balance is {mainbal}")
     if option==2:
         withdraw_amount=int(input("please enter withdrwal_amount :  "))

         mainbal=mainbal-withdraw_amount

         print(f"{withdraw_amount}is debited from your account :  ")

         print(f"your current balance is {mainbal}")

     if option==3:
         diposit_amount=int(input("please enter your diposit amount:  "))
         mainbal=mainbal+diposit_amount
         print(f"{diposit_amount}is credited your bank account :  ")

         print(f"your current balance is {mainbal}")

     if option==4:
         break



else:
    print("Wrong pin Please try again")


with open ( 'mainbal.txt' , 'w' ) as fptr :
        fptr . write ( str ( mainbal ) )
        fptr . close ()
