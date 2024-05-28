#use paranthesis () to define tuple
marks = (90,94,96,90,97,97,97)

print(marks)

#for loop in tuple(it used to show every marks individually)
for result in marks:
    print(result)

#count(it use to count how many times values inserted in tuple)
print(marks.count(97))
print(marks.count(90))

#to see the index of any numbers in tuple
print(marks.index(96))
print(marks.index(97))