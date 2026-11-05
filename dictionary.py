
"Dictionary Tasks"
"Task 11: Create a Student Dictionary"

student={"name":"Abisheik",
         "Age":"20",
         "course":"Python",
         "Marks":"100"}
for i,j in student.items():
    print(i,j)
print()
print()


"Task 12: Count Character Frequency"

py="programming"
code={}
for i in py:
    if i in code:
        code[i]+=1
    else:
        code[i]=1
print(code)
print()
print()


"Task 13: Count Word Frequency"

sentence="Python SQL Python Excel SQL Python"
word=sentence.split()
count={}
for i in word:
    if i in count:
        count[i]+=1
    else:
        count[i]=1
print(count)
print()
print()


"14: Find the Student with the Highest Mark"

students={"Arun": 78,
          "Priya": 92,
          "Kumar": 85,
          "Divya": 96,
          "Ravi": 88}
highest=0
name=""
for i,j in students.items():
    if j > highest:
        highest=j
        name=i
print(name,":",highest)
print()
print()

##a=[10,20,30,40,50]
##b=0
##for i in a:
##    if i > b:
##        b=i
##print(b)


##"Task 15: Merge Two Dictionaries and add their valuees"
##
##dict_a={"Python": 10, "SQL": 15, "Excel": 8}
##dict_b= {"SQL": 20, "Excel": 12, "Power BI": 10}
##dict_c=
##merged_dict={}
##for i, j in dict_b.items():
##    if i in merged_dict:
##        merged_dict[i]+=j
##    else:
##        merged_dict[i]=j
##print(i, j)

"Task 16: Group Students by Marks"
students={"Arun": 82,
          "Priya": 95,
          "Kumar": 68,
          "Divya": 42,
          "Ravi": 88}

groups={"Excellent":[],
        "Good":[],
        "Average":[],
        "Needs improvements":[]}

for i,j in students.items():
    if j>=90:
        groups["Excellent"].append(i)
    elif j>=75:
        groups["Good"].append(i)
    elif j>=50:
        groups["Average"].append(i)
    else:
        groups["Needs improvements"].append(i)
for i,j in groups.items():
   print(i,":",", ".join(j))
print()
print()

        
