#!/usr/bin/env python3

import sys
import subprocess


def check_container(containers):
	docker_command = "docker ps --format '{{.Names}}'".split(" ")
	running_containers = subprocess.check_output(docker_command).decode("utf-8").split("\n")
	running_containers.pop()
	new_running_containers = []
	for i in running_containers:
		new_running_containers.append(i.replace("'", ""))

	# Check if containers exists in running containers
	check_containers = all(elem in new_running_containers for elem in containers)

	if check_containers:
		return True

	return False


def update_container(containers):
	subprocess.check_call(["clear"])
	print("=================================")
	print("Updating: " + ",".join(containers))
	print("=================================")

	try:
		for container in containers:
			subprocess.check_call(["docker-compose", "pull", f"{container}"])
		
		for container in containers:
			subprocess.check_call(["docker-compose", "up", "-d", f"{container}"])

		print("============================")
		print("Updating containers complete")
		print("============================")

	except Exception as e:
		print(f"Updating failed: {e}")

def main():
	if len(sys.argv) < 2:
		print(f"(+) Usage: {sys.argv[0]} <containername>")
		print(f"(+) Example: {sys.argv[0]} container1 container2")
		sys.exit()

	containers = []
	for container in sys.argv:
		containers.append(container)
	
	containers.pop(0)

	if check_container(containers):
		update_container(containers)
	else:
		print("Container(s) does not exist")


if __name__ == '__main__':
	main()