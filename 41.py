age = int (input("Enter your age: "))
if 31 < age < 41:
    print("you are ok")

years_of_experience = int(input("Enter your years of experience: "))
if 2 < years_of_experience < 10:
    print("you have experience")

def square(n):
    print(n * n)

square(5)


def check_in_interval(what_to_ask, min_value, max_value):
    current_value = int(input(what_to_ask))
    if min_value< current_value < max_value:
       return True
    return False

result = check_in_interval("enter your age: ",
                  0,
                  20)
if result:
    print("your age was entered correctly")
result = check_in_interval("enter your years of experience: ",
                  2,
                  10)


