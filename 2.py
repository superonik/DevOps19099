from email.policy import strict

your_name = input("enter your name: ")
print(your_name)
your_age = int(input("enter your age :"))
print("are you old?" + str(your_age >= 18))
print(your_age >= 18)
your_height = int(input("enter your height:"))
print ("are you tall? " + str(your_height >= 180))
if your_name == "aviel":
    print("welcome to my name")
else:
    print("welcome to nor my name")

