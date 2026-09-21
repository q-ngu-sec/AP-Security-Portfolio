"""
=============================================================================== 
SCRIPT NAME : sshloader.py
DESCRIPTION : The script provides basic ssh commands to be used by other scripts
AUTHOR : Quany Nguyen
DATE CREATED : 2026-09-04
USAGE : Used alongside other Bandit Python scripts
 SECURITY NOTICE:
This tool is created for educational and authorized testing purposes ONLY.
Do not run this script against target systems without explicit authorization.
=============================================================================== 
""" 

## WARNING : THE SCRIPT DOESN'T WORK ON SCHOOL WIFI. SO, SET UP A MOBILE HOTSPOT. ##

## IMPORTS ##
import sys 
import argparse

# SSHv2 Python library
import paramiko

## VARIABLES ##
newline = '\n'
passwords_file = "banditpasswords.txt"
password_starter = "bandit0"

total_levels = 11

ssh_client = None
bandit_host = "bandit.labs.overthewire.org"
bandit_port = 2220
bandit_username = None
bandit_password = None

BOUNDS = 40 # For lines between each level being automated
SENTINEL = -1 # In free-play mode, where when the user enters the SENTINEL, the program exits

# Config
time_out = 5 # Seconds taken until you get kicked out when connecting
auth_time_out = 10 # Same thing above but for authentication waiting

full_process = True # While automating, the script will use commands in order to achieve the answer if full_process = True. Otherwise, the answer will only be visible.

## FUNCTIONS ##
	
def connect_to_server(name):
	global ssh_client, username, password
	
	# Removing the bandit[number] portion
	bandit_username = name
	level = int("".join(list(bandit_username)[6:]))
	
	with open(passwords_file, "r") as bandit_passwords:
		# Create list of lines
		password_lines = [line.strip() for line in bandit_passwords]
		bandit_password = password_lines[level]
	
	print("")
	print("=" * BOUNDS)
	print(f"Level: {level}")
	print(f"Username: {bandit_username}")
	print(f"Password: {bandit_password}")
	print("")
	
	ssh_client = paramiko.SSHClient()
	# Avoid fingerprint
	ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	
	ssh_client.connect(
		hostname = bandit_host,
		port=bandit_port,
		username=bandit_username,
		password=bandit_password,
		timeout = time_out,
		auth_timeout = auth_time_out,
		look_for_keys = False, 
		allow_agent = False
	)
	
	
def is_connection_active():
	global ssh_client
	transport = ssh_client.get_transport()
	return (transport and transport.is_active())

def execute_command(command):
	global ssh_client
	server_returned = None
	if (is_connection_active()):
		# stdout only matters.
		_1, stdout, _2 = ssh_client.exec_command(command)
	
		try:
			output = stdout.read().decode("utf-8")
		except UnicodeDecodeError:
			output = f"Output for \"{command}\" isn't human-readable to decode from utf-8."
	
		if (output):
			server_returned = output
	
	return server_returned
	
def print_process(command):
	print("$ " + command)
	print(execute_command(command))
	
def show_process(commands):
	if (full_process):
		for c in commands:
			print_process(c)
	
def format_pass(next_bandit_pass, level):
	print(f"Password for Level {level + 1}: {next_bandit_pass}")
	
def capture_pass(next_bandit_pass, level):
	next_bandit_pass = next_bandit_pass.strip()
	password_lines = None
	
	with open(passwords_file, "r") as bandit_passwords:
		password_lines = bandit_passwords.readlines()
		
	password_lines[level + 1] = next_bandit_pass + newline
	
	with open(passwords_file, "w") as bandit_passwords:
		for password_line in password_lines:
			bandit_passwords.write(password_line)
		
	
def exit_server():
	global ssh_client
	ssh_client.close()
	
def check_file():
	print(f"Checking for {passwords_file}...")
	try:
		with open(passwords_file, "x") as bandit_passwords:
			bandit_passwords.write(password_starter + newline)
			for i in range(total_levels):
				# To access list within bounds for capture_pass
				bandit_passwords.write(newline)
			print(f"{passwords_file} has been created to store passwords for future use.")
	except FileExistsError:
		print(f"{passwords_file} exists already.")
		
def has_password(level):
	has_password = False
	with open(passwords_file, "r") as bandit_passwords:
		# Check if password is there
		password_lines = [line.strip() for line in bandit_passwords]
		bandit_password = password_lines[level]
		if (bandit_password != ""):
			has_password = True
		
	if (not has_password):
		with open(passwords_file, "r") as bandit_passwords:
			password_lines = [line.strip() for line in bandit_passwords]
			i = 0
			while (password_lines[i + 1] != ""):
				i += 1
			print(f"There's no recorded password for Level {level}. Start at Level {i}.\n")
		return False
	return True
