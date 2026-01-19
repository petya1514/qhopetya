def display_chars(file_path, num_chars):
     with open(file_path, "r") as file:
        text = file.read(num_chars)
        print(text)


def display_line(file_path):
    with open(file_path) as file:
        line = file.readline().strip()
        print(line)


def display_text(file_path):
    with open(file_path) as file:
        text = file.read()
        print(text)

def run_task2():
    display_chars(file_path="library.txt", num_chars=10)
    display_line("library.txt")
    display_text("library.txt")



