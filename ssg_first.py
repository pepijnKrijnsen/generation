###############################
#### STATIC SITE GENERATOR ####

import os
import datetime
import re

def main():
	project_directory = os.getcwd()
	templates_directory = project_directory + "/templates"
	website_directory = project_directory + "/sites_generated"
#	get the template pieces
	try:
		os.chdir(templates_directory)
	except:
		print("No directory called 'templates' in project directory")
		quit()
	all_contents_template_dir = os.listdir()
	index = 0
	for name in all_contents_template_dir:
		if re.search(".html$", name):
			index += 1
			f = open(name)
			
			f.close()
	