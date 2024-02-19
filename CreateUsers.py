# Ronald Maule - 2/6/2023
# Creates users for each victim VM
# Assigns users to each group

import os
import random
import string

NUM_SECTIONS = 9
NUM_GROUPS = 35
NUM_VICTIMS = 10
NUM_USERS_PER_VICTIM = 100

pwds = [line.strip() for line in open("PwnedPWs100k.txt", "r").readlines()]

# Randomly generates user/pass/secret and returns it as a string
def make_user(vm:int) -> str:
	pwd = random.choice(pwds)
	user_num = ''.join(random.choices(string.ascii_letters+string.digits, k=5))
	secret = ''.join(random.choices(string.ascii_letters+string.digits, k=10))

	return f"U{user_num} {pwd} {secret} VM_{vm}\n"

# Create list of empty lists for each victim VM
users = [[] for _ in range(NUM_VICTIMS)]

# Create users for each machine
for i in range(NUM_VICTIMS):
	for _ in range(NUM_USERS_PER_VICTIM):
		users[i].append(make_user(i+1))

# Create file listing user/pass/secret for each Victim VM
with open("Lab2_Victims/utils/VMUsers.txt", "w") as vm_file:
	for vm, vm_list in enumerate(users):
		vm_file.write(f"VM {vm+1}:\n")
		for user in vm_list:
			vm_file.write(f"\t{user}")
		vm_file.write('\n')

# Create file which lists each user/pass/secret for every group
with open("UsersFile.txt", "w") as users_file:
	for section in range(NUM_SECTIONS):
		users_file.write(f"Section {section+1}:\n")

		for group in range(NUM_GROUPS):
			users_file.write(f"\tGroup {group+1}:\n")

			# Each user must be from a unique VM
			chosen = []
			for _ in range(3):
				# Randomly select unused VM
				while (vm := random.randrange(len(users))) in chosen: continue
				chosen.append(vm)

				# Randomly select unused user
				vm_list = users[vm]
				user = random.randrange(len(vm_list))
				users_file.write(f"\t\t{vm_list[user]}")

				# Remove user and VM (if empty)
				users[vm].pop(user)
				if len(users[vm]) == 0: users.pop(vm)
			users_file.write('\n')
	
	users_file.write('\n')

os.system("cp UsersFile.txt ../Lab2")
