marks = [95,96,97,98,"math"]

print(marks)
print(marks[0]) #it will print 0th index position number: 95
print(marks[1]) #it will print 2nd position number: 96
print(marks[0:2]) #it will print 1st two number: 95,96
print(marks[2:4]) #it will print 3rd and 4th number: 97,98

 # if we want to print number from back
print(marks[-1]) # it will print 'math'
print(marks[-2]) # it will print '98'

#Checking length of list
print(len(marks))

#Append(means adding in list)
marks.append(85)
print(marks)

#insert (means adding in specific position on the list)
marks.insert(0, 70)
marks.insert(1, 80)

print(marks)

#number existing check on the list
print(95 in marks) #True
print(90 in marks) #False

#for loop in list
name = ["Ahnat","Afrin","Tanha"]
for student in name:
    print(student)
print(len(name))

#while loop in list
fruits = ["apple","mango","orange"]

i = 0
while i < len(fruits):
    print(fruits[i])
    i+=1

#to clean list
fruits.clear()
print(fruits)