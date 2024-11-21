current_name = input("what is your name?: ")
while current_name != "quit":
    if current_name == "eden":
        continue
    if current_name == "ronen":
        break 
    print(f"Hello, {current_name}!")
    current_name = input("what is your name?: ")
else:
    ("thank you for playing!")
