##username=input("Enter username:")
##while username!="Abisheik":
##    username=input("Enter correct password:")
##print("success")



##"Sum of digit"
##sum=45673
##add=0
##while sum>0:
##    digit=sum%10
##    add=add+digit
##    sum=sum//10
##print(add)
##
##"Reverse"
##num=89372
##reverse=0
##while num>0:
##    digit=num%10
##    reverse=reverse*10+digit
##    num=num//10
##print(reverse)
##
##"palindrome"
##num=1234321
##original=num
##reverse=0
##while num>0:
##    digit=num%10
##    reverse=reverse*10+digit
##    num=num//10
##if original==reverse:
##    print("palindrome correct")
##else:
##    print("palindrome not correct")
##
##print()
##print()
##print()
##print()
##print()
##
##"Control Statement - Break, Continue"
##"First Divisible Number — For Loop"
##
##for i in range(1,51,1):
##    if i%3==0 and i%5==0:
##        print(i)
##        break
##print()
##print()
##
##"Skip Multiples — For Loop"
##"that are divisible by either 3 or 5."
##
##for i in range(1,31,1):
##    if i%3==0 or i%5==0:
##        continue
##    print(i)
##print()
##print()
##
##"Odd Numbers Before 30 — While Loop"
##num=1
##while num<30:
##    if num%2!=0:
##        print(num)
##    num=num+1
##print()
##print()
##
##"first number greater than 50 that is divisible by 7."
##        
##num=1
##while num<=100:
##    if num>50 and num%7==0:
##        print(num)
##        break
##    num=num+1
##print()
##print()
##
##"Do not print numbers divisible by 3. Stop the loop when the number reaches 40"
##for i in range(1,51):
##    if i %3==0:
##        continue
##    if i==40:
##        break
##    print(i)
##print()
##print()
##
##
##"Print numbers divisible by 4. Stop when you reach the first number divisible by both 4 and 6."
##num=1
##while num<=100:
##    if num %4==0 and num%6==0:
##        break
##    if num%4==0:
##        print(num)
##    num=num+1
##print()
##print()
##
##"Find the first perfect square greater than 20. Print the number and stop the loop."
##
####for i in range(1,101):
####    if 
####        print(i)
####print()
####print()
##
##"Do not print numbers divisible by 2 or 3. Stop when the number reaches 45."
##num= 1
##while num<=50:
##    if num==45:
##        break
##    if num %2==0 or num%3== 0:
##        num = num + 1
##        continue
##    print(num)
##    num=num+ 1
##print()
##print()
##
##
##secret_number=27
##for i in range(5):
##    guess_num=int(input("Enter number:"))
##    if secret_number==guess_num:
##        print("Number found")
##        break
##    elif guess_num==0:
##        print("Bye")
##        break
##else:
##    print("Not found")
##
##
##guess_num=12
##while(True):
##    secret_num=int(input("Enter guess number:"))
##    if guess_num==secret_num:
##        print("Your guess number is correct")
##        break
##    elif guess_num<secret_num:
##        print("Too high")
##    elif guess_num>secret_num:
##        print("Too low")
##else:
##    print("number not found")
##    
##
##digit_count=0
##sum_total=0
##largest=0
##small=9
##odd=0
##even=0
##multiple=1
##num=int(input("Enter a number: "))
##while num>0:
##    digit=num%10
##    digit_count=digit_count+1
##    sum_total=sum_total+digit
##    if digit>largest:
##        largest=digit
##    if digit<small:
##        small=digit
##    if digit%2==0:
##        even=even+1
##    else:
##        odd=odd+1
##    multiple=multiple*digit
##    num=num//10
##print("Digit count:", digit_count)
##print("Sum Total:", sum_total)
##print("Largest:", largest)
##print("Smallest:", small)
##print("Odd number:", odd)
##print("Even number:", even)
##print("Multiple:", multiple)
##print()
##print()

"Armstrong"

count=3
num=153
total=0
temp=num
while num>0:
    digit=num%10
    total=total+digit**count
    num=num//10
if total==temp:
    print("armstrong valid")
else:
    print("armstrong invalid")
    
