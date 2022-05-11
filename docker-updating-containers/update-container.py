#!/usr/bin/env python3

import sys
import subprocess


def update_container(containers):
	print("=================================")
	print("Updating: " + ",".join(containers))
	print("=================================")

	try:
		for container in containers:
			subprocess.check_call(["docker-compose", "pull", f"{container}"])
		
		for container in containers:
			subprocess.check_call(["docker-compose", "up", "-d", f"{container}"])

		print("Updating containers complete")
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

	update_container(containers)


if __name__ == '__main__':
	main()