"""
=============================================================================== 
SCRIPT NAME : bandit3automator.py
DESCRIPTION : The script solves Bandit Level 3.
AUTHOR : Quany Nguyen
DATE CREATED : 2026-09-04
USAGE : python bandit3automator.py
 SECURITY NOTICE:
This tool is created for educational and authorized testing purposes ONLY.
Do not run this script against target systems without explicit authorization.
=============================================================================== 
""" 

## IMPORTS ##
import sshloader

## VARIABLES ##
level = 3

## FUNCTIONS ##
def main():
	sshloader.check_file()
	if (sshloader.has_password(level)):
		# Script entry point
		sshloader.connect_to_server("bandit" + str(level))
		
		commands = None
		answer = None
		
		if (sshloader.is_connection_active()):
			# For some reason, you will always be in home directory after cd's for paramiko
			directory_change = "cd inhere"
			sshloader.show_process(
				(directory_change + " && ls -la", directory_change + " && cat ./...Hiding-From-You")
			)
			
			answer = sshloader.execute_command(directory_change + " && cat ./...Hiding-From-You")
		
		if answer is not None:
			answer = answer.strip()
			sshloader.capture_pass(answer, level)
			sshloader.format_pass(answer, level)
			
		sshloader.exit_server()
		
		return 0
	else:
		return 1
  
## EXECUTION ##
if __name__ == "__main__": 
	main() 
