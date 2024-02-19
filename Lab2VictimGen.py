# Ronald Maule 9/16/2022
# Updated on 10/4/2023 by github.com/alarst13
# Set up Victim VMs for lab 2

import os
import shutil
from subprocess import Popen, PIPE
import sys

NUM_VICTIMS = 10
NUM_USERS_PER_VICTIM = 100

# Create list of empty lists
all_users = [[] for _ in range(NUM_VICTIMS)]

# Add users to current list in all_users
# When an empty line appears, switch to next list in all_users
vm_users = [l.strip() for l in open("utils/VMUsers.txt", "r").readlines()]
for i in range(NUM_VICTIMS):
	all_users[i].extend(vm_users[1:NUM_USERS_PER_VICTIM+1])
	vm_users = vm_users[NUM_USERS_PER_VICTIM+2:]

# Setup VMs
users = all_users[int(sys.argv[1])-1]
for user in users:
	u, p, s, _ = user.split(' ')

	# Add user to VM
	os.system(f"useradd -m {u}")

	# Set the user's password
	process = Popen(["passwd", u], stdin=PIPE, stdout=PIPE, stderr=PIPE)
	process.stdin.write(bytes(f"{p}\n", "utf-8"))
	process.stdin.write(bytes(p, "utf-8"))
	process.stdin.flush()

	# Create Q2secret
	os.system(f"echo {s} > Q2secret")

	os.system(f"chown {u}:{u} Q2secret")
	os.chmod("Q2secret", 0o400)
	shutil.move("Q2secret", f"../{u}")