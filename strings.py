name = "Ahnat Afrin"

print(name)

print(name.upper()) #the whole line will be converted to capital letter(AHNAT AFRIN)
print(name.lower()) #the whole line will be converted to small letter (ahnat afrin)

print(name.find('Afrin')) #it will find Afrin in index 6

print(name.replace('A','S')) # 'A' in name variable will change to 'S'
print(name.replace('Ahnat','Tanha')) # Ahnat will change to Tanha
print(name.replace('Ahnat Afrin','Sayeed')) # 'Ahnat Afrin' will change to 'Sayeed'

#keywords (in)
print('h' in name) #output will be True
print('Afrin' in name) #output will be True
print('Tanha' in name) #output will be False