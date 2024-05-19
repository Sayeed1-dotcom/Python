        #break & continue
#break
student = ['Ahnat','Afrin','Absar','Tanha','Tanu']

for name in student:
    if name == 'Tanha':
        break;
    print(name)
print(len(student))

#continue
for name in student:
    if name == 'Absar':
        continue;
    print(name)
