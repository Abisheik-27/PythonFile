secret_number=27
for i in range(5):
    guess_num=int(input("Enter number:"))
    if secret_number==guess_num:
        print("Number found")
        break
    elif guess_num==0:
        print("Bye")
        break
else:
    print("Not found")


guess_num=12
while(True):
    secret_num=int(input("Enter guess number:"))
    if guess_num==secret_num:
        print("Your guess number is correct")
        break
    elif guess_num<secret_num:
        print("Too high")
    elif guess_num>secret_num:
        print("Too low")
else:
    print("number not found") 
