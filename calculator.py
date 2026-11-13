from sys import exit



def main():
    print(f"Initial value is 0.\nPress ctrl+d to see answer and exit the program")

    print(values())


def values():
    answer = 0
    while True:
        try:
            operator = input("Enter one acceptable operator. (+ - * /) ")
            if operator not in ["+", "-", "/", "*"]:
                exit(f"Enterd operator isn't functionable\nAnd your answer is {answer}")

            try:
                operand = float(input("Enter the number: "))
            except ValueError:
                exit(f"Entered value isn't appropiate. (ValueError)\nAnd your answer is {answer}")

            if operator == "+":
                answer = add(answer, operand)
            elif operator == "-":
                answer = sub(answer, operand)
            elif operator == "*":
                answer = mul(answer, operand)
            elif operator == "/":
                try:
                    answer = div(answer, operand)
                except ZeroDivisionError:
                    return("Can't divide by zero. Your answer is {answer}")

        except EOFError:
            return (f"\nYour answer is {answer}")


def add(a, o):
    return a + o


def sub(a, o):
    return a - o


def mul(a, o):
    return a * o


def div(a, o):
    return a / o


if __name__ == "__main__":
    main()
