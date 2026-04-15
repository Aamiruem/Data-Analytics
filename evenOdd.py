num = int(input("Enter a number: "))
if num % 2 == 0:
    print(f"{num} is an even number.")
else:
    print(f"{num} is an odd number.")

# or using ternary operator 

n = 10
print(f"{n} is an even number." if n % 2 == 0 else f"{n} is an odd number.")
