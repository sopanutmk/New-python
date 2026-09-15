class negativeNumberError(Exception):
    def __init__(self,value):
        self.value = value
        super().__init__(f"Invalid input: {value} is a negative number")

def check_positive_number(num):
    if num<0:
        raise negativeNumberError(num)
    else:
        print(f"{num} is a valid positive number")

try:
    number= int(input("Enter a positive number: "))
    check_positive_number(number)
except negativeNumberError as e:
    print(e)
except ValueError:
    print("Error: please enter a valid integer.")
finally:
    print("Program execution finished.")