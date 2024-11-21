for i in range(101):
    if i % 7 == 0 or str(i).endswith('7') or str(i).startswith('7') or '7' in str(i):
        continue
    print(i)


names = ["natan","shay","ronen","aaron"]
result = [name.upper() for name in names if "n" in name]
print(result)
