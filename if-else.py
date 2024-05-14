age = int(input("Enter your age :"))

if age >= 18:
    print("You are an adult")
    print("You can vote")
elif age < 18 and age > 3:
    print("You are a boy.Sorry!You can't vote.")

else:
    print("You are a child.")
