"""
=============================================================================== 
SCRIPT NAME : bandit6automator.py
DESCRIPTION : The script solves Bandit Level 6.
AUTHOR : Quany Nguyen
DATE CREATED : 2026-09-04
USAGE : python bandit6automator.py
 SECURITY NOTICE:
This tool is created for educational and authorized testing purposes ONLY.
Do not run this script against target systems without explicit authorization.
=============================================================================== 
""" 

## IMPORTS ##
import sshloader

## VARIABLES ##
level = 6

## FUNCTIONS ##
def main():
	sshloader.check_file()
	if (sshloader.has_password(level)):
		# Script entry point
		sshloader.connect_to_server("bandit" + str(level))
		
		commands = None
		answer = None
		
		if (sshloader.is_connection_active()):
			directory_change = "cd /"
			sshloader.show_process(
				(directory_change + " && find . -user bandit7 -group bandit6 -size 33c 2>/dev/null", 
				directory_change + " && cat ./var/lib/dpkg/info/bandit7.password")
			)
			answer = sshloader.execute_command(directory_change + " && cat ./var/lib/dpkg/info/bandit7.password")
		
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
