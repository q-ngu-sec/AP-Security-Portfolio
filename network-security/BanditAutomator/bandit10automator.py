"""
=============================================================================== 
SCRIPT NAME : bandit10automator.py
DESCRIPTION : The script solves Bandit Level 10.
AUTHOR : Quany Nguyen
DATE CREATED : 2026-09-04
USAGE : python bandit10automator.py
 SECURITY NOTICE:
This tool is created for educational and authorized testing purposes ONLY.
Do not run this script against target systems without explicit authorization.
=============================================================================== 
""" 

## IMPORTS ##
import sshloader

## VARIABLES ##
level = 10

## FUNCTIONS ##
def main():
	sshloader.check_file()
	if (sshloader.has_password(level)):
		# Script entry point
		sshloader.connect_to_server("bandit" + str(level))
		
		commands = None
		answer = None
		
		if (sshloader.is_connection_active()):
			# 4th substring between spaces
			sshloader.show_process(("base64 -d data.txt",))
			answer = sshloader.execute_command("base64 -d data.txt").split()[3]
		
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
