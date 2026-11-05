"Find the largest letters"

word=("Python is a amazing programming language")
largest=""
for i in word.split():
    if len(i)>len(largest):
        largest=i
print(largest)
print()
print()


"Remove the repeating leetters"

word=("hello word hii")
remaining=""
for i in word:
    if i not in remaining:
        remaining=remaining+i
print(remaining)




