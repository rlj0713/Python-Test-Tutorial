
def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    return a / b


# Add this functionality
# def power(a, b):
    # Write this functionality after you write the test


def main():
    while True:
        print("\nSimple Calculator")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Quit")

        choice = input("Choose: ")

        if choice == "5":
            break

        a = float(input("First number: "))
        b = float(input("Second number: "))

        if choice == "1":
            print("Result:", add(a, b))

        elif choice == "2":
            print("Result:", subtract(a, b))

        elif choice == "3":
            print("Result:", multiply(a, b))

        elif choice == "4":
            print("Result:", divide(a, b))

        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()