# pattern_drawing.py

# Prompt user for pattern size
size = int(input("Enter the size of the pattern: "))

# Draw the pattern
i = 0
while i < size:
    for j in range(size):
        print("*", end="")  # print without newline
    print()  # move to next row
    i += 1
