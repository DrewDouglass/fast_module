#!/usr/bin/python3

import os
import sys
import io
import urllib.request
import shutil
import tkinter as tk
from tkinter import filedialog
import time

def main():
	print("\n This will create a new module in this directory.")
	fm_continue = input("\n To continue type Y. To cancel type anything else.\n")
	if(fm_continue.lower() == "y"):
		print("\nLet's do this. Create a directory.")
		root = tk.Tk()
		root.withdraw()
		#fm_mod_name = input("\n What is the name of the module, including the 'mod_' prefix?\n")
		fm_mod_name_abs = filedialog.askdirectory(initialdir='.')
		#quit(fm_mod_name)
		#Main modules folder
		if(os.path.isdir(fm_mod_name_abs) == False):
			os.makedirs(fm_mod_name_abs)
		fm_mod_name = os.path.basename(os.path.normpath(fm_mod_name_abs))
		#create tmpl inside new folder
		os.makedirs(os.path.join(fm_mod_name_abs, "tmpl"))
		#Create default.php inside tmpl/
		with urllib.request.urlopen('https://raw.githubusercontent.com/DrewDouglass/mod_starter/master/tmpl/default.php') as response, open(os.path.join(fm_mod_name_abs, "tmpl", "default.php"), 'wb') as out_file:
			shutil.copyfileobj(response, out_file)
		#create index.html inside tmpl/
		with urllib.request.urlopen('https://raw.githubusercontent.com/DrewDouglass/mod_starter/master/index.html') as response, open(os.path.join(fm_mod_name_abs, "tmpl", "index.html"), 'wb') as out_file:
			shutil.copyfileobj(response, out_file)
		#create helper.php
		with urllib.request.urlopen('https://raw.githubusercontent.com/DrewDouglass/mod_starter/master/helper.php') as response, open(os.path.join(fm_mod_name_abs, "helper.php"), 'wb') as out_file:
			shutil.copyfileobj(response, out_file)
		#create index.html
		with urllib.request.urlopen('https://raw.githubusercontent.com/DrewDouglass/mod_starter/master/index.html') as response, open(os.path.join(fm_mod_name_abs, "index.html"), 'wb') as out_file:
			shutil.copyfileobj(response, out_file)
		#create mod_*.php
		with urllib.request.urlopen('https://raw.githubusercontent.com/DrewDouglass/mod_starter/master/mod_starter.php') as response, open(os.path.join(fm_mod_name_abs, fm_mod_name + ".php"), 'wb') as out_file:
			shutil.copyfileobj(response, out_file)
		#create mod_*.xml
		with urllib.request.urlopen('https://raw.githubusercontent.com/DrewDouglass/mod_starter/master/mod_starter.xml') as response, open(os.path.join(fm_mod_name_abs, fm_mod_name + ".xml"), 'wb') as out_file:
			shutil.copyfileobj(response, out_file)
		#Now replace all mod_starter strings with given module name.
		replacement = fm_mod_name
		for dname, dirs, files in os.walk(os.path.join(os.getcwd(), fm_mod_name_abs)):
		    for fname in files:
		        fpath = os.path.join(dname, fname)
		        with open(fpath) as f:
		            s = f.read()
		        s = s.replace("mod_starter", replacement)
		        with open(fpath, "w") as f:
		            f.write(s)
		print("\n\nAll Done. Cleaning up and closing window.\n\n")
		time.sleep(3)
	else:
		print("Cancelled, no actions taken.")

if __name__ == '__main__':
	main()