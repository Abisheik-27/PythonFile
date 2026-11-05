
#1
"varible swapping"
a=10
b=20
a,b=b,a
print(a)
print(b)
print()

#2
"three variable rotation"
a=10
b=20
c=30
a,b,c=c,a,b
print(a)
print(b)
print(c)
print()

#3
"reverse 2 variables"
x=100
y=200
print(y)
print(x)
print()
#4
"exchange without 3rd variable"
a=15
b=25
a,b=b,a
print(a)
print(b)
print()

#5
"calculate and store"
a=10
b=5
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print()

#6
"Double and triple"
x=50
double=x*2
triple=x*3
print(x)
print(double)
print(triple)
print()

#7
"Swap three variables"
a="python"
b="SQL"
c="Excel"
a,b,c=c,a,b
print(a)
print(b)
print(c)
print()

#8
"personal introduction"
name="Abisheik"
age=24
city="Pondicherry"
profession="Data analtyics"
print("My name is",name,".","Im",age,"years old",".","Im from",city,".","My profession is",profession)
print()

#9
"Shopping bills"
print("===================================")
name="Mysore sandal"
price=80
quantity=6
shop="arun cost price"
print("product-",name,".""\n""Price of per soap-",price,".""\n""Total quantity of the product-",quantity,".""\n""Location-",shop,".")
print("Total amount-",price*quantity)
print("===================================")
print()

#10
"Student Result"
English=97
Maths=98
Science=95
print("English subject - ",English)
print("Maths subject - ",Maths)
print("Science subject - ",Science)
print("Total Mark - ",English+Maths+Science)
print()
print()
print()

"Operator Task"
#1
"Swap two numbers using arithmetic opt"
a=10
b=20
a=a+b
b=a-b
a=a-b
print(a)
print(b)
print()
print()

#2
"swap using multiply and division"
a=5
b=10
a=a*b
b=a/b
a=a/b
print(a)
print(b)
print()
print()


#3
"Rotate 3 variables"
a=10
b=20
c=30
a=a+b+c
b=a-b-c
c=a-b-c
a=a-b-c
print(a)
print(b)
print(c)
print()

#4
"find the last digit"
number=9876
print(number%10)
print()

#5
"remove the last digit"
number=9876
print(number//10)
print()

#6
"extract last 2 digit"
number=98765
print(number%100)
print()

#7
"Find the 1st digit"
number=456
print(number//100)
print()

#8
"find the middle digit"
number=456
a=number//10
print(a%10)
print()

#9
"Reverse 2 digit number"
number=47
lastnum=(number%10)
firstnum=(number//10)
print(lastnum*10+firstnum)
print()
print()

#10
"Reverse a 3 number"
number=123
last=(number%10)
middle=(number//10)%10
first=(number//100)
print(last*100+middle*10+first)
print()
print()

#11
"sum of digit"
number=456
first=(number//100)
second=(number//10)%10
last=(number%10)
print(first+second+last)
print()
print()

#12
"product of digit"
number=234
first=(number//100)
second=(number//10)%10
third=(number%10)
print(first*second*third)
print()
print()

#13
"Seperate Quotient and remainder"
a=27
b=5
quotient=(a/b)
remainder=(a%b)
print(quotient)
print(remainder)
print()
print()

#14
"converts second into hours, minutes and seconds"
seconds=3665
hours=(seconds//3600)
minutes=(seconds//3600)
sec=(seconds%60)
print(hours)
print(minutes)
print(sec)
print()
print()

#15
"converts Days into weeks and Days"
days=45
weeks=(days//7)
days=(days%7)
print(weeks)
print(days)
print()
print()

#16
"Converts Months into years and months"
months=27
years=(months//12)
Months=(months%12)
print(years)
print(Months)
print()

#17
"Converts minutes into Hours and Minutes"
minutes=135
Hours=(minutes//60)
Minutes=(minutes%60)
print(Hours)
print(Minutes)
print()

#18
"Reverse Total amount calculation"
total_amount=1000
price=(total_amount//4)
print(price)
print()

#19
"calculate discount amnt and final price"
price=2500
discount_percentage=20
discount_amount=(price*discount_percentage/100)
final_price=(price-discount_amount)
print("The Discount amount is -",discount_amount)
print("The final amount is -",final_price)
print()

#20
"salary breakdown"
basic_salary=30000
HRA=(basic_salary*20/100)
Bonus=(basic_salary*10/100)
Total_salary=(basic_salary+HRA+Bonus)
print("The basic salary is:",basic_salary)
print("HRA:",HRA)
print("Bonus:",Bonus)
print("The total salary is:",Total_salary)
print()

#21
"Find whether a number is even"
number=24
print(number%2==0)
print()

#22
"Find whether a number is odd"
number=17
print(number%2==0)
print()

#23
"Ccreate whether a number s divisib le by 5"
number=125
print(number%5==0)
print()

#24
"whether a number is divisible by both 3 and 5"
number=30
print(number%3==0 and number%5==0)
print()

#25
"check whether a number is divisible by 10"
number=150
print(number%10==0)
print()

#26
"check whether a nuumber is between two values"
number=75
print(number>50 and number<100)
print()

#27
"check whether a number is outside a range"
number=150
print(number<10 or number>100)
print()

#28
"check largest number among this three"
a=10
b=20
c=15
is_a_largest=(a>b and a>c)
is_b_largest=(b>a and b>c)
is_c_largest=(c>b and c>a)
print(is_a_largest)
print(is_b_largest)
print(is_c_largest)
print()

#29
"Check all the numbers are equal"
a=10
b=10
c=10
final=(a==b and b==c)
print(final)
print()

#30
"check both numbers are positive"
a=10
b=-5
print(a>0 and b>0)
print()

#31
"check Whether At Least One Number Is Positive"
a = -10
b = 5
print(a>0 or b>0)
print()

#32
"Check Whether Exactly One Condition Is True"
a = 10
b = 20
print((a>15) != (b>15))
print()

#33
"Student Pass Condition"
english = 45
maths = 55
print(english >= 40 and maths >= 40)
print()
print()

#34
"Exam Eligibility"
attendance = 80
internal_marks = 45
eligible = attendance >= 75 and internal_marks >= 40
print(eligible)
print()
print()


#35
"Admission Eligibility"
marks = 75
age = 20
maths_pass = True
computer_science_pass = False
eligible = marks >= 60 and age >= 17 and age <= 25 and (maths_pass or computer_science_pass)
print(eligible)
print()
print()

"Assignment, Membership and Identity opt"
#1
"Create a variable"
num=10
add=(15+10)
multiply=(add*2)
subtract=(multiply-10)
print(add)
print(multiply)
print(subtract)
print()
print()

num=10
num+=15
print(num)
num*=2
print(num)
num-=10
print(num)
print()
print()

#2
"Create a variable"
x=20
x+=10
print(x)
x/=2
print(x)
x*=5
print(x)
x-=15
print(x)
print()
print()

#3
"Create a variable"
a=50
a+=25
print(a)
a%=7
print(a)
a*=10
print(a)
print()
print()


"IF, Elif, Else tasks"
#1
"Get a number from the user."
num=int(input("Enter a number:"))
if num%3==0 and num%5==0:
    print("Fizzbuzz")
elif num%3==0:
    print("Fizz")
elif num%5==0:
    print("buzz")
else:
    print("Normal")
print()
print()

#2

number = int(input("Enter a number: "))
if number % 3 == 0 and number % 5 == 0 and number % 2 == 0:
    print("Even FizzBuzz")
elif number % 3 == 0 and number % 5 == 0 and number % 2 != 0:
    print("Odd FizzBuzz")
elif number % 3 == 0 and number % 2 == 0:
    print("Even Fizz")
elif number % 3 == 0 and number % 2 != 0:
    print("Odd Fizz")
elif number % 5 == 0:
    print("Buzz")
else:
    print("Normal")
print()
print()

#3
"NUMBER PRIORITY"
number = int(input("Enter a number: "))
if number % 2 == 0 and number % 3 == 0 and number % 5 == 0:
    print("Super Number")
elif number % 2 == 0 and number % 3 == 0:
    print("Even Multiple")
elif number % 3 == 0:
    print("Fizz")
elif number % 5 == 0:
    print("Buzz")
elif number % 2 == 0:
    print("Even")
else:
    print("Odd")

#4
"MARKS WITH SPECIAL CASE"
marks = int(input("Enter your marks: "))
if marks < 0 or marks > 100:
    print("Invalid Marks")
elif marks == 100:
    print("Perfect Score")
elif marks >= 90:
    print("Distinction")
elif marks >= 75:
    print("First Class")
elif marks >= 60:
    print("Second Class")
elif marks >= 40:
    print("Pass")
else:
    print("Fail")
print()
print()

#5
"LEAP YEAR"
year = int(input("Enter a year: "))
if year % 400 == 0:
    print("Leap Year")
elif year % 100 == 0:
    print("Not a Leap Year")
elif year % 4 == 0:
    print("Leap Year")
else:
    print("Not a Leap Year")
print()
print()


#6
"AGE with spl case"
age = int(input("Enter your age: "))
if age < 0:
    print("Invalid Age")
elif age == 0:
    print("New Born")
elif age <= 12:
    print("Child")
elif age <= 17:
    print("Teenager")
elif age == 18:
    print("Exactly Adult")
elif age <= 59:
    print("Adult")
else:
    print("Senior Citizen")
print()
print()

#7
"NUMBER SIGN + PARITY"
number = int(input("Enter a number: "))
if number == 0:
    print("Zero")
elif number > 0 and number % 2 == 0:
    print("Positive Even")
elif number > 0 and number % 2 != 0:
    print("Positive Odd")
elif number < 0 and number % 2 == 0:
    print("Negative Even")
else:
    print("Negative Odd")
print()
print()


#8
"ATM WITHDRAWAL"
balance = int(input("Enter account balance: "))
withdrawal = int(input("Enter withdrawal amount: "))
if withdrawal <= 0:
    print("Invalid Amount")
elif withdrawal % 100 != 0:
    print("Invalid Amount")
elif withdrawal > balance:
    print("Insufficient Balance")
elif balance - withdrawal < 1000:
    print("Minimum Balance Required")
else:
    balance = balance - withdrawal
    print("Withdrawal Successful")
    print("Remaining Balance:", balance)
print()
print()

#9
"TRIANGLE CLASSIFICATION"
a = int(input("Enter side 1: "))
b = int(input("Enter side 2: "))
c = int(input("Enter side 3: "))
if a <= 0 or b <= 0 or c <= 0:
    print("Invalid Triangle")
elif a + b <= c or a + c <= b or b + c <= a:
    print("Invalid Triangle")
elif a == b and b == c:
    print("Equilateral")
elif a == b or b == c or a == c:
    print("Isosceles")
else:
    print("Scalene")
print()
print()

#10
"LARGEST NUMBER WITH TIE"
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))
if a == b and b == c:
    print("All Equal")
elif a == b and a > c:
    print("First and Second are Largest")
elif a == c and a > b:
    print("First and Third are Largest")
elif b == c and b > a:
    print("Second and Third are Largest")
elif a > b and a > c:
    print("First number is Largest")
elif b > a and b > c:
    print("Second number is Largest")
else:
    print("Third number is Largest")
