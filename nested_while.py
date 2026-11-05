for i in range(1,6):
    for j in range(i):
        print("*",end="")
    print()



for i in range(1,6,1):
    for j in range(i):
        print(i,end="")
    print()
print()

for i in range(5):
    for j in range(i,i+1):
        print("*"*5)
print()



for i in range(5):
    for j in range(5):
        print(((i),(j)),end="")
    print()
print()


for i in range(5):
    for j in range(5):
        if i==j:
            print("*",end="")
        else:
            print(" ",end="")
    print()
print()



for i in range(5):
    for j in range(5):
        if i==0 or j==4:
            print("*",end="")
        elif i==4 or j==0:
            print("*",end="")
        else:
            print(" ",end="")
    print()
print()




for i in range(8):
    for j in range(8):
        if (i+j)%2==0:
            print("B",end=" ")
        else:
            print("W",end=" ")
    print()
print()
print()



for i in range(5):
    for j in range(1,i+1):
        print(i,end="")
    print()
print()
print()


w1="earth"
w2="heart"
if sorted(w1)==sorted(w2):
    print("anagram")
else:
    print("not anagrams")
print()
print()


"find the non repeatable word"

word="school"
for i in word:
    if word.count(i)==1:
        print(i)
        break
