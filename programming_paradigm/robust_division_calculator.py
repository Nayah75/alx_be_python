def safe_divide(numerator, denominator):
    try:
        numerator = float(input("Enter the numerator: "))
        denominator = float(input("Enter the denominator: "))
        result = numerator / denominator
    except ValueError:
        print("Invalid input. Please enter numeric values.")
    except ZeroDivisionError:
        print("Cannot divide by zero.")
    else:
        print(f"Result: {result}")
