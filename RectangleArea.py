def get_valid_input(prompt):
    while True:
        try:
            value = int(input(prompt))
            if 1 <= value <= 10:
                return value
            else:
                print("Invalid input. Please enter a number between 1 and 10.")
        except ValueError:
            print("Invalid input. Please enter a number.")


def draw_rectangle(length_input, width_input):
    for i in range(length_input):
        for j in range(width_input):
            print("=", end="")
        print()


def main():
    length_input = get_valid_input("What is the length you chose?\n")
    width_input = get_valid_input("What is the width you chose?\n")

    area = length_input * width_input

    print("==========================")

    print("Here is your length: ", length_input)
    print("Here is your width: ", width_input)
    input("Press Enter to see area...")

    print("=========================")
    print("Your area equals: ", area)
    print("=========================")
    draw_rectangle(length_input, width_input)
    print("==========================")


if __name__ == "__main__":
    main()
