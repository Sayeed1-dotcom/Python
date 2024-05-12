#arithmatic operators (+,-,*,/,%,**)
a=4
b=3
c=5
d=10

#Addition
Sum=a+b+c
print(Sum)

#Subtraction
diff=c-b
print(diff)

#Multiplication
M=b*c
print(M)

#Division
D=d/c
print(D)

#remainder
R=a % b
print(R)

#power like a^2=4^2=16
P=a ** b
print(P)

#relational operators (==,!=,>,>=,<,<=)

a=10
b=20

print(a == b) #Answer will be False
print(a != b) #Answer will be True
print(a > b) #Answer will be False
print(a >= b) #Answer will be False
print(a < b) #Answer will be True
print(a <= b) #Answer will be True

#Assignment operators(+=,-=,*=,/=,%=,**=)

i = 10
i += 5 #output 10+5=15
print("i =", i)

j=12
j -= 5 #output 12-5=7
print("j =", j)

k=3
k *= 5 #output 3*5=15
print("k =", k)

l=10
l /= 5 #output 10/5=2
print("l =", l)

p=10
p %= 5 #output 10%5=0
print("p =", p)

q=2
q **= 3 #output 2**3=8
print("q =", q)


#Logical operators (not,and,or)

                      #not

print(not True)
a=20
b=10
print(not (a>b)) #answer will be: False

                     #and
A = True
B = True
print("1.AND operator :", A and B) #Answer will be: True

A = True
B = False
print("2.AND operator :", A and B) #Answer will be: False

A = False
B = True
print("3.AND operator :", A and B) #Answer will be: False

A = False
B = False
print("4.AND operator :", A and B) #Answer will be: False

                     #or
C = True
D = True 
print ("1.OR operator :", C or D) #Answer will be: True

C = True
D = False
print ("2.OR operator :", C or D) #Answer will be: True

C = False
D = True 
print ("3.OR operator :", C or D) #Answer will be: True

C = False
D = False 
print ("4.OR operator :", C or D) #Answer will be: False 


#Multiple operators (relational & logical)

a = 10
b = 5
c = 5

print("1.Combined answer is :", (a>b) and (b==c) ) #Answer will be: True
print("2.Combined answer is :", (a<b) and (b==c) ) #Answer will be: False
print("3.Combined answer is :", (a>b) and (a>c) ) #Answer will be: True
print("4.Combined answer is :", (a>b) and not(c>a) ) #Answer will be: True
print("5.Combined answer is :", (a>b) or (a>c) ) #Answer will be: True
print("6.Combined answer is :", (a>b) or (b>c) ) #Answer will be: True
print("7.Combined answer is :", (a<b) or (a<c) ) #Answer will be: False


#Type casting

a = str("4")
b = float(5)
c = 2.526
print(type (a))
print("b value is :", b)
print("b+c value is :", b+c)