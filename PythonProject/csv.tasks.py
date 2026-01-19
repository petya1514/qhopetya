def read_csv(file_path):

    file = open(file_path, 'r')

    try:

        headings = file.readline().strip()
        print(f"Headings:\n{headings}")


        print("Values:")


        for line in file:
            print(line.strip())

    finally:
        # Close the file
        file.close()
