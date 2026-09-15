def divide(a,b):
    try:
        result = a/b
    except ZeroDivisionError as e:
        print("Exception: ",e)
    else:
        return result
a,b = map(int,input("Enter two number separated by space:").split())
print(f"the result of {a} divide by {b} is: {divide(a,b)}")
print("End of program")