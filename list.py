"create a list with duplicate values"

students=['Abisheik', 'Akshay', 'Dass', 'Abisheik', 'swathi', 'swathi']
num=[]
for i in students:
    if i not in num:
        num.append(i)
print(num)
print()
print()

"oddd even"
number = [1,2,3,4,5,6,7,8,9,10]
odd=[]
even=[]
for num in number:
    if num%2==0:
        even.append(num)
    else:
        odd.append(num)
print(even)
print(odd)
print()
print()

"pos and neg"
number = [1,2,3,-4,-5,-6,7,-8,9,10]
positive=[]
negative=[]
for num in number:
    if num>0:
        positive.append(num)
    else:
        negative.append(num)
print(positive)
print(negative)
print()
print()


"list compensation"
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
new=[]
for x in fruits:
    if 'a' in x:
        new.append(x)
print(new)
print()
print()

"sorting- asending order"
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)
print()
print()

"descending order"
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse=True)
print(thislist)
print()
print()

"case sensitive- Capital letter comes 1st"
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort()
print(thislist)
print()

"case-insensitive- lower letter comes 1st"
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key=str.lower)
print(thislist)
print()











"List Task:"
"1. Find the Second Largest Number"
num=[10, 25, 8, 40, 25, 30]
num=list(set(num))
num.sort()
print(num[-2])
print()
print()


"2. remove dulicate element"
num= [10, 20, 10, 30, 20, 40]
num=list(set(num))
print(num)
print()
print()


"3.Count Even and Odd Numbers"
num = [10, 15, 20, 25, 30, 35]
odd=0
even=0
for i in num:
    if i%2==0:
        even+=1
    else:
        odd+=1
print(even)
print(odd)
print()
print()



"5. Find Common Elements Between Two Lists"
a=[10, 20, 30, 40, 50]
b=[30, 40, 60, 70]
common=[]
for i in a:
    if i in b:
        common.append(i)
print(common)
print()
print()

"6. Move All Zeros to the End"
num=[0, 10, 0, 20, 30, 0, 40]
a=[]
for i in num:
    if i!=0:
        a.append(i)
for i in num:
    if i==0:
        a.append(i)
print(a)
print()
print()

"7.Find the Frequency of Each Element"
num = [10, 20, 10, 30, 20, 10, 40]
for i in num:
    if num.count(i)>0:
        print(i, "appears",  num.count(i), "Times")
print()
print()


"8. Find the Missing Number"
"A list contains numbers from 1 to 10"

num = [1, 2, 3, 5, 6, 7, 8, 9, 10]
for i in range(1,11):
    if i not in num:
        print(i)
print()
print()

"9. Reverse a List Without Using reverse()"
num = [10, 20, 30, 40, 50]
a=[]
for i in num:
    a.insert(0,i)
print(a)


