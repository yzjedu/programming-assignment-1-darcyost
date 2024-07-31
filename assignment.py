# Name: [Darcy Ostrander]
# Course: CS701/GB735, Dr. Yalew
# Date: [8/6/2024]
# Programming Assignment: 1
# Program Inputs: Dimensions of the room (length, width, height) in feet
# Program Outputs: Total area to be painted (in square feet), amount of primer (in gallons), amount of paint (in gallons)

def main():
    
    '''This program Computes the amount of paint needed one more'''
    # Step 1: Ask the user for the dimensions of the room
    # The three dimensions are length - height - width 
    userInput= input("What is the length of the room in feet: ")
    roomLength = float(userInput)
    userInput= input("What is the width of the room in feet: ")
    roomWidth = float(userInput)
    userInput= input("What is the height of the room in feet: ")
    roomHeight = float(userInput)

    # Step 2: Compute the total area of the four walls and ceiling
    # Area of walls = 2 * (length * height + width * height)
    wallArea = (2 * (roomLength * roomHeight + roomWidth * roomHeight))
   
    # Area of ceiling = length * width
    ceilingArea = (roomLength * roomWidth)
   
    # Total area = Area of walls + Area of ceiling
    totalArea = (wallArea + ceilingArea)


    # Step 3: Calculate the amount of primer and paint needed
    # Primer coverage = 200 square feet per gallon
    primerNeeded = float(totalArea / 200)
    
    # Paint coverage = 350 square feet per gallon
    paintNeeded = float(totalArea / 350)

    # Step 4: Output the total area and the amount of primer and paint needed
    # Uncomment the three lines below for the output
    print(f"Total area to be painted: {totalArea:.2f} square feet")
    print(f"Amount of primer needed: {primerNeeded:.2f} gallons")
    print(f"Amount of paint needed: {paintNeeded:.2f} gallons")

if __name__ == "__main__":
    main()