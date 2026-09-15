try:
    numerator = float(input("Enter the numerator: "))
    denominator = float(input("Enter the denomicator: "))

    result = numerator / denominator
    print(f"The result is: {result}")

except ZeroDivisionError:
    print("Error: You cannot divide by zero.")

except ValueError:
    print("Error: Invalid input. Please enter numeric values.")

finally:
    print("Execution compleated, whether an excepion occurred of not.")

print("End pf program")