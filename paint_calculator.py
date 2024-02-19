# Paint Calculator

# Get height, width, length from user
length = int(input("Enter length of the room in feet: "))
width = int(input("Enter width of the room in feet: "))
height = int(input("Enter height of the room in feet: "))

# Get number of windows, doors, from user
doors = int(input("Enter number of doors: "))
windows = int(input("Enter number of windows: "))

# Set wall area to (2 * length * height) + (2 * width * height)
wall_area = (2 * length * height) + (2 * width * height) 

# Set NoPaintArea to 20 * doors + 15 * windows
no_paint_area = 20 * doors + 15 * windows

# Set PaintArea to wall area - NoPaintArea
paint_area = wall_area - no_paint_area

# Print PaintArea
print(f"Total surface area to paint: {paint_area}")

# Set gallons to paint area / 350
gallons = paint_area / 350

# Print gallons after rounding to 2 places
print(f"Number of gallons of paint needed: {gallons:.2f}")


