# Ronald Maule 9/19/2022

import json
import os
import random
import shutil
import socket
import string

NUM_SECTIONS = 9
NUM_GROUPS = 35
NUM_VICTIMS = 10

##### Setup #####
users_file = [line.split() for line in open("UsersFile.txt", "r").readlines()]
os.system("rm UsersFile.txt")

users = []
for i in range(NUM_SECTIONS):
	users.append([])
	for _ in range(NUM_GROUPS):
		users[i].append([])

for i in range(NUM_SECTIONS):
	users_file = users_file[1:]

	for j in range(NUM_GROUPS):
		users[i][j].extend(users_file[1:4])
		users_file = users_file[5:]

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(('10.254.254.254', 1))
ip = int(s.getsockname()[0].split('.')[3])

section_num = (ip - 10) // 35
group_num = (ip - 10) % 35
group_users = users[section_num][group_num]

##### Q2 #####
pwds = [line.strip() for line in open("PwnedPWs100k.txt", "r").readlines()]

with open("Solutions.json", "w") as sol_file:
	solutions = dict()
	for i, user in enumerate(group_users):
		solutions[i] = ' '.join(user)
	json.dump(solutions, sol_file)

# Randomly generates user/pass and returns it as a string
def make_user() -> str:
	pwd = random.choice(pwds)
	user_num = ''.join(random.choices(string.ascii_letters+string.digits, k=5))

	return f"U{user_num} {pwd}\n"

# Add correct users to Q2pwds
q2pwds = []
for user in group_users:
	u, p = user[0], user[1]
	q2pwds.append(f"{u} {p}\n")

# Fill Q2pwds with random users
for _ in range(12):
	q2pwds.append(make_user())
random.shuffle(q2pwds)

# Create Q2pwds
with open("Q2pwd", "w") as f:
	for user in q2pwds:
		f.write(user)

##### Close #####
os.system("chown cse:cse Q2pwd")
os.chmod("Q2pwd", 0o755)

os.system("chown cse:cse jsencoder.html")
os.chmod("jsencoder.html", 0o755)

os.mkdir("Solutions")
os.mkdir("LabGen")

shutil.move("Lab2Gen.py", "LabGen/")
shutil.move("CreateUsers.py", "LabGen/")
shutil.move("PwnedPWs100k.txt", "LabGen/")
shutil.move("Lab2VictimGen.py", "LabGen/")

os.system("chown -R  cse:cse .")
