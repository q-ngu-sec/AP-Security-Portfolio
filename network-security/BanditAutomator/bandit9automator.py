"""
=============================================================================== 
SCRIPT NAME : bandit9automator.py
DESCRIPTION : The script solves Bandit Level 9.
AUTHOR : Quany Nguyen
DATE CREATED : 2026-09-04
USAGE : python bandit9automator.py
 SECURITY NOTICE:
This tool is created for educational and authorized testing purposes ONLY.
Do not run this script against target systems without explicit authorization.
=============================================================================== 
""" 

## IMPORTS ##
import sshloader

## VARIABLES ##
level = 9

## FUNCTIONS ##
def main():
	sshloader.check_file()
	if (sshloader.has_password(level)):
		# Script entry point
		sshloader.connect_to_server("bandit" + str(level))
		
		commands = None
		answer = None
		
		if (sshloader.is_connection_active()):
			# 9th substring between spaces
			sshloader.show_process(("strings data.txt | grep \"==\"",))
			answer = sshloader.execute_command("strings data.txt | grep \"==\"").split()[8]
		
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
