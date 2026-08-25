with open('../data/notes.txt', 'r') as file:
    for number, line in enumerate(file, start=1):
        print(f"Line {number}: {line.strip()}")

#for line in file:
    #print(f"Line 1: {line.strip()}")
    # Saving for posterity to see where I started.