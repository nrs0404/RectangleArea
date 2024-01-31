
import time

def draw_rectangle(length, width):
    """Draws a rectangle with the given length and width using '=' characters."""
    for i in range(length):
        for j in range(width):
            time.sleep(.3) 
            print("=", end="")
        print()

def main():

    """Main entry point for the program."""
    # Get user input for length and width
    length_input = int(input("Enter the length of the rectangle 1-10: "))
    width_input = int(input("Enter the width of the rectangle 1-10: "))
    divider = "====================="

    #calculate the area
    area = length_input * width_input
    perim = 2 * (length_input + width_input)

    unit_choice = input("Press [1] for centimeters , [2] for inches , [3] for feet")
   
    correct_user_choice = False

    while not correct_user_choice:
        if unit_choice == '1':
            correct_user_choice = True
            unit_choice = "centimeters"
        elif unit_choice == '2':
            correct_user_choice = True
            unit_choice = "inches"
        elif unit_choice == '3':
            correct_user_choice = True
            unit_choice = "feet"
        else:
            print(divider)
            print("Invalid response, please input [1], [2], or [3]")
            print(divider)
            unit_choice = input("Press [1] for centimeters , [2] for inches , [3] for feet")
            correct_user_choice  = False
    
    #to check initial input as valid
    valid_length = 1 <= length_input <= 10
    valid_width = 1 <= width_input <= 10
    
    #logic
    answered_correctly = valid_length and valid_width

    # Display length and width
    print(divider)
    print("Length: ", length_input , unit_choice)
    print("Width: ", width_input , unit_choice)
    print(divider)

    while not answered_correctly:
        length_input = int(input("Please enter a valid length of the rectangle 1-10: "))
        width_input = int(input("Please enter the width of the rectangle 1-10: "))
        
        #reassign value
        area = length_input * width_input
        perim = 2 * (length_input + width_input)

        # Recalculate the conditions for validity
        valid_length = 1 <= length_input <= 10
        valid_width = 1 <= width_input <= 10
    
        # Update answered_correctly based on new input
        answered_correctly = valid_length and valid_width
    
        if answered_correctly:
            break
        else:
            print("Please input a length value between 1 and 10.")

    #Display area
    print("Area: ", area , unit_choice,  "^2" )
    print("Perimeter: " , perim, unit_choice)
    print("Unit: " , unit_choice)
    print(divider)

    # # Draw the rectangle
    draw_rectangle(length_input, width_input)
    
if __name__ == "__main__":
    # Call the main function if the script is executed directly
    main()
    
