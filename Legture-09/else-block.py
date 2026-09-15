try:
    value = int(input("Enter anumber: "))
    result =10/value
except ZeroDivisionError:
    print("Cannot divide by zero!")
else:
    print(f"The result is {result}")

print("End of program")