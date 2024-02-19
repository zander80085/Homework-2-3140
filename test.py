if __name__ == "__main__":
    print("This is a test script!")


import sys
def log_command_line():
    with open('Q1B.out', 'a') as log_file:
        log_file.write(' '.join(sys.argv) + '\n')
log_command_line()
