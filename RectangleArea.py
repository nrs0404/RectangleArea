length_input = int(input("What is the length you chose?\n"))
width_input = int(input("What is the width you chose?\n"))

def draw_rectangle(length_input, width_input):
    for i in range(length_input):
        for j in range(width_input):
            print("=" , end="")
        print()

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

