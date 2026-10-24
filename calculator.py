"""A small command-line calculator for four basic arithmetic operations."""

def calculate(first, operator, second):
    if operator == "+":
        return first + second
    if operator == "-":
        return first - second
    if operator == "*":
        return first * second
    if operator == "/":
        if second == 0:
            raise ValueError("Cannot divide by zero.")
        return first / second
    raise ValueError("Choose one of: +, -, *, /")


def main():
    print("Simple Python Calculator")
    try:
        first = float(input("First number: "))
        operator = input("Operation (+, -, *, /): ").strip()
        second = float(input("Second number: "))
        result = calculate(first, operator, second)
        print(f"Result: {result:g}")
    except ValueError as error:
        print(f"Input error: {error}")


if __name__ == "__main__":
    main()
