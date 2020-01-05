#!/usr/bin/python3
import sys,os
from termcolor import colored

def usage():
	print('Usage: python3 <' + sys.argv[0] + '> <path_to_file>')
	print('Help:  python3 <' + sys.argv[0] + '> --help')
	exit(1)

# Help menu
def form():
	print("The dfa file format must be: ")
	print('States\nSymbols-Alphabet\nInitial state\nFinal state\nTransitions\n(All seperated with tabs or spaces)\n')
	print('Example:\n3\n0 1\n0\n0 1\n0 1 1\n0 0 0')
	exit(23)

if (len(sys.argv) != 2):
	usage()
else:
	hp = '--help'

	# File open
	filename = sys.argv[1].strip()  
	if (filename == hp):
		form()
		exit(1312)
	f = open(filename, 'r') 

	# Variables
	total_states = '' 		
	symbols = {}	 		
	init_state = '' 		
	final_states = {}		
	transitions = {}		
	current_state = ''			

	line = 1 	# Each line of the file
	trans = 0 	# Used for my transition list 
	for i in f:
		if line == 1:
			total_states = i.split()
			if (int(total_states[0]) >= 10):
				print('Total states must be less than 10.')
				exit(2)
			line += 1
		elif line == 2:
			symbols = i.split()
			if (len(symbols) >= 10):
				print('Total symbols must be less than 10.')
				exit(3)
			line += 1 
		elif line == 3:
			init_state = i.split()
			line += 1 
		elif line == 4:
			final_states = i.split()
			line += 1
		else:
			transitions[trans] = i.split()
			trans += 1
			line += 1

	# Prints the file data 
	print('\n' + '*'*20 + 'AUTOMATA' + '*'*20)
	print('Total states: \t\t', total_states[0])
	
	temp_symbols = ''
	for i in range(0, len(symbols)):
		temp_symbols += symbols[i] + ' '
	print('Symbols-Alphabet: \t', temp_symbols)

	print('Initial state: \t\t', 'q' + init_state[0])
	
	temp_final = ''
	for i in range(0, len(final_states)):
		temp_final += 'q' + final_states[i] + ' '
	print('Final states: \t\t', temp_final)

	print('Transitions: ')
	for i in range(0, len(transitions)):
		print('\t\t\t', transitions[i])
	print('*'*48)


	# Main menu
	flag = True 
	while flag:
		text = input('\nInsert string for checking: ') # user's text for checking
		current_state = init_state[0]

		# In case this does not work on windows, comment out the 'colored' lines and uncomment the others below them
		print(colored('[+] Current state:\t[q' + current_state +']', 'yellow'))
		#print('[+] Current state:\t[' + current_state + ']') 
		for k in text:
			invalid = False # For invalid characters
			for i in transitions:
				if (transitions[i][0] == current_state): 	# if the state in transition is current state
					if (k == transitions[i][1]):			# if the letter of input text is the 'trigger' to change state
						current_state = transitions[i][2]	# current state = new_current_state (the third element of the transition list)
						print(colored('    Checking:\t\t(' + k + ')', 'blue'))
						#print('    Checking:\t\t(' + k + ')')
						print(colored('[+] Current state:\t[q' + current_state +']', 'yellow'))
						#print('[+] Current state:\t[q' + current_state + ']')
						invalid = True
						break
			if (invalid == False):
				print(colored('[!] Invalid character detected! [' + k + ']. Exiting..\n', 'red'))
				#print('[!] Invalid character detected! [' + k + ']. Exiting..\n')
				exit(69)

		accept = False # For acceptance of the input string
		for t in range(0, len(final_states)):
			if (current_state == final_states[t]):
				print('\nString: ' + text, colored('[+] Accepted! [+]', 'green'))
				#print('\nString: ' + text,'[-] Accepted! [-]')
				accept = True
				break
		if (accept == False):
			print('\nString: ' + text, colored('[-] Rejected! [-]', 'red'))
			#print('\nString: ' + text,'[-] Rejected! [-]')

		ans = input('\nIf you want to check another one, press "y" or "Y": ')
		if (ans != 'y' and ans != 'Y'):
			flag = False

	print('\n~Goodbye~\n')
	f.close()


