################# A ###############
from locale import currency

x = int(input("enter first number: "))
y = int(input("enter second number: "))
if x>y:
    print("BIG")
else:
    print ("small")



################# B ###############

for i in range(5):
    print(i)



################# C ###############


x = int(input("Please enter a number between 1 and 4: "))
while x<1 or x>4:
    print("Invalid input")
    x= int(input("Please enter a number between 1 and 4: "))
if x==1:
    print("summer")
elif x==2:
    print("winter")
elif x==3:
    print("fall")
elif x==4:
    print("spring")

################D###############

count = 1
while count < 11:
    print(count)
    count += 1
print ("\n", count-1 , "times loop run \n",count ,"number was printed last")



################E###############

age = input("enter Your age: ")
fst = input("enter Your Name: ")[0]
curr = float(input("enter current shekels dollar currency: "))
abr =  input("Did you flew abroad ? (Yes/No): ").lower()
if abr == 'yes':
    abr = True
else:
    abr = False
apartment = int(input("enter your apartment number: "))
print ('Your current age is :', age)
print ('first letter of your name is :', fst)
print ('current shekels dollar currency is :', curr)
print ('Did you flew aboard :',  abr)
print ('apartment number is :', apartment)
print ('your age with currency  :', float(age) + curr)


################F###############
num = input("enter Your phone number: ")
print ('your phone number is :', num)


################G###############
def printHello():
    return print("hello")

def calculate():
    return print(5+3.2)



##############H###############

def print_name(name):
    return print(name)

def dev_num ( num ):
    return print(float(num)/2)


###############I###############

def numbers (a, b):
    return a+b

def strings (str1, str2):
    return str1 +" "+ str2

##############K###############

for i in range(5):
    print("#")
    for j in range(5):
    print(j*"#","\n")

