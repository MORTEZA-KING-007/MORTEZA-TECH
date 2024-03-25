#!/usr/bin/python3.11
import sys
import os

try:
	argv = sys.argv[1]
except:
	print(f'\x1b[1;37m Usage : \n\t python setup.py Install')
	sys.exit()

def requirements_installer(argv):
	if argv == "Install":
		os.system('clear')
		print('\x1b[1;37m[✅] INSTALLING REQUIREMENTS ....')
		# --- It will check the modules
		try:
			import requests
			import colorama
			import mechanize
			import rich
			import bs4
		except:
			os.system('pkg install espeak -y')
			os.system('pip install requests')
			os.system('pip install colorama')
			os.system('pip install mechanize')
			os.system('pip install rich')
			os.system('pip install bs4')
			os.system('pip install futures')
			os.system('pip install lolcat')
		
		os.system('clear')
		print('\x1b[1;37m[✅] REQUIREMENTS INSTALLED SUCCESSFULLY ....')
		t = input('\x1b[1;37m[⚡] DO YOU WANT TO RUN THE FB CLONER TOOL (Y/n) ÷> ')
		if t in ['Y', 'y']:
			os.system('python MORTEZA-TECH.py')
		elif t in ['n', 'N']:
			pass
	else:
		print(f'\x1b[1;37m Usage : \n\t python setup.py Install')
		sys.exit()

requirements_installer(argv)
