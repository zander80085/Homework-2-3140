import os

def driver():
    directory_path = "C:\\Users\\Zander\\Desktop\\Homework 2 3140"

    files = os.listdir(directory_path)
    with open('FileNames.txt', 'w', encoding= 'utf-8') as file:
        for line in files:
            if line == "__pycache__": pass
            else: file.write(f"{line}\n")


