"""
=============================================================================== 
SCRIPT NAME : bandit0automator.py
DESCRIPTION : The script solves Bandit Level 0.
AUTHOR : Quany Nguyen
DATE CREATED : 2026-09-04
USAGE : python bandit0automator.py
 SECURITY NOTICE:
This tool is created for educational and authorized testing purposes ONLY.
Do not run this script against target systems without explicit authorization.
=============================================================================== 
""" 

## IMPORTS ##
import sshloader

## VARIABLES ##
level = 0

## FUNCTIONS ##
def main():
	sshloader.check_file()
	if (sshloader.has_password(level)):
		# Script entry point
		sshloader.connect_to_server("bandit" + str(level))
		
		commands = None
		answer = None
		
		if (sshloader.is_connection_active()):
			sshloader.show_process(
				("ls -la", "cat readme")
			)
			# index 399 starts with the password
			answer = sshloader.execute_command("grep \"is: \" readme | cut -d ' ' -f 8")
		
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

