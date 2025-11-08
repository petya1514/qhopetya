# Ask user for sequence and marker
print("Please enter a sequence:")
sequence = input()

print ("Please enter the character for the marker:")
marker = input()

# find markers
marker_1 position =-1
marker_2 =-1

for position in range(0,len(sequence),1):
    letter = sequence[position]

    if letter == marker:
        if (marker_1 position == -1):
            marker_1 = position
        else:
            marker_2 = position
print(f"The distance between the markers is {marker_2 position - marker_1 position -1}.")
