import sys
from myapp.app import multiply_by_two, divide_by_two, calculate_square_area  # Import the necessary functions

def main():
    num = float(input("Insert a number (side length of the square): "))  # Take input as float to match the square root value
    area = calculate_square_area(num)  # Calculate the area using the input value
    print("The double of %.2f is %.2f" % (num, multiply_by_two(num)))
    print("The half of %.2f is %.2f" % (num, divide_by_two(num)))
    print("The area of the square with side %.2f is %.2f" % (num, area))  # Display the calculated area
    
    sys.exit(0)

if __name__ == "__main__":
    main()
