#!/usr/bin/python3

import argparse
import sys
import time
import os

from reportlab.lib.enums import TA_JUSTIFY
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab import platypus
from  reportlab.lib.styles import ParagraphStyle as PS

def main():
	# setup arguments
	parser = argparse.ArgumentParser(description='Put description here')
	parser.add_argument('-o', '--outfile', help='PDF file', required="True")
	parser.add_argument('-t', '--template', help='Template file to write from', required="True")

	# parse arguments
	args = parser.parse_args()

#	template = args.template.split('/')[1]
#	template = str(template.split('.')[0])

	# do stuff
	
	pdf_file = SimpleDocTemplate(args.outfile, pagesize=letter,
                        rightMargin=72,leftMargin=72,
                        topMargin=72,bottomMargin=18)
	pdf = get_template(args)
	pdf_file.multiBuild(pdf)

	print ("PDF File written to: ", args.outfile)

def get_template(args):
	Story=[]

	# Variables
	due_date = "03/05/2017"
	url = 'https://jschoeneman.com'
	logo = 'pdftemplates/logo.png'
	formatted_time = time.ctime()
	company = 'Weyland Corp'
	sender = 'Ellen Ripley'
	
	#Link Building
	click_me = 'Click Here to acknowledge you understand the new changes to the policy.'
	link = '<font color=blue><link href="' + url + '">' + click_me + '</link></font>'
	im = Image(logo,2*inch, 1*inch)
	Story.append(im)
	
	styles=getSampleStyleSheet()
	styles.add(PS(name='Justify', alignment=TA_JUSTIFY))
	
	ptext = '<font size=10>%s</font>' % formatted_time
	
	Story.append(Spacer(1, 12))
	
	# Create return address
	Story.append(Paragraph(ptext, styles["Normal"]))        
	Story.append(Spacer(1, 12))
	
	#input from template text	
	with open(args.template, 'r') as t:
		for line in t:
			Story.append(Paragraph(line, styles["Normal"]))

	# add link
	Story.append(Spacer(1, 8))
	Story.append(platypus.Paragraph(link, styles["Justify"]))
	Story.append(Spacer(1, 12))
	ptext = '<font size=10>Sincerely,</font>'
	Story.append(Paragraph(ptext, styles["Normal"]))
	
	Story.append(Spacer(1, 12))
	ptext = '<font size=10>'+ sender + '</font>'
	Story.append(Paragraph(ptext, styles["Normal"]))
	return Story

if __name__ == '__main__':
	main()