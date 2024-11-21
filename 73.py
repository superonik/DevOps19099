
##############################K#######################

for i in range(6):
    for j in range(i):
        print("#", end="")
   print("\n")

###########################L##########################


k=0
for i in range(2,-1, -1):
    for j in range(5,-1,-1):
        print(' '*(5-(i))+'#'+' '*(j+i-k-1)+'#')
        k+=1
        break
k=0
print("      #")
for i in range(3):
    for j in range(5,-1,-1):
        print(' '*(5-(i))+'#'+' '*(j-(3-i)+k)+'#')
        k+=1
        break

##############################M#######################

def get_num ():
    num = int(input("Enter a number: \n"))
    return num

def sum_of_digits():
    sum=0
    x = get_num()
    while (x > 0):
        y = x % 10
        sum = y + sum
        x = (x // 10)
    return (sum)



