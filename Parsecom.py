#Code was adapted from the tutorial provided by freeCodeCamp.org (Credit to John Elder):
#https://www.youtube.com/watch?v=byHcYRoMgI4

#Their referred url link to their github:
#https://github.com/flatplanet/Intro-To-TKinter-Youtube-Course

#A handy piece of code for clearing the screen provided by Grepper (credit to Expensive Eagle):
#https://www.codegrepper.com/code-examples/python+os.system+clear+screen

# Author: Mark Warren
# Date:	12/05/2022
# Purpose: A General Purpose built Program that removes whitespace found in between data. This file stores the commands needed for the menu.
# Version: 1.0
# Software: Python 3.8
# Dependancies:	csv, itertools, sys, os, xml.etree.ElementTree, tkinter, filedialog

# Note: This was salvaged from a fully functioning program I developed and I have remade this in case I wish to build upon the tool further.

import csv
import itertools
import sys
import os
import xml.etree.ElementTree as ET
import tkinter as tk
from tkinter import filedialog

#Schema: e.g. Pickles = "./chapter[@id='chap_pre']/section[@id='pickles_sec_1_pre']"
Pickles = "./chapter[@id='chap_pre']/section[@id='pickles_sec_1_pre']"

XMLTable = Pickles

#Tree file location
tree = ET.parse('pickles.xml')
root = tree.getroot()

#Change tree default location
def changetree():
	newtree = tk.Tk()
	newtree.withdraw()
	
	file_path = filedialog.askopenfilename()
	tree = ET.parse(file_path)
	print ("File Location changed to: " + file_path)

def create(XMLTable):
	
	tablename = ''
	
	for tabletitle in root.findall(XMLTable):
		tablename = tabletitle[0].text
	columns = ''
	colum0 = ''
	colum1 = ''
	colum2 = ''
	
	#Clears spaces/carriage returns found in columns
	for col0 in root.findall(XMLTable + "/table/tgroup/thead/row/entry[1]"):
		colum0 = col0.text
		colum0 = [i.replace("\n", "") for i in colum0]
		colum0 = ["".join(list(colum0))]
		colum0 = [i.replace("  ", " ") for i in colum0]
		colum0 = ["".join(list(colum0))]
	
	for col1 in root.findall(XMLTable + "/table/tgroup/thead/row/entry[2]"):
		colum1 = col0.text
		colum1 = [i.replace("\n", "") for i in colum1]
		colum1 = ["".join(list(colum1))]
		colum1 = [i.replace("  ", " ") for i in colum1]
		colum1 = ["".join(list(colum1))]
	
	for col2 in root.findall(XMLTable + "/table/tgroup/thead/row/entry[3]"):
		colum2 = col2.text
		colum2 = [i.replace("\n", "") for i in colum2]
		colum2 = ["".join(list(colum2))]
		colum2 = [i.replace("  ", " ") for i in colum2]
		colum2 = ["".join(list(colum2))]
	
	#Stores Columns
	
	idcol = 'id'
	columns = idcol, colum0, colum1, colum2
	
	#Clears spaces/carriage returns found in rows and replaces list data appropriately
	
	datarow = 'datarow'
	nospace = ''
	
	dat0 = root.findall(XMLTable + "/table/tgroup/tbody/row/entry[1]")
	
	for index, child in enumerate(dat0):
		exec(f"{listname}{index}=[]")
		nospace = child.text
		nospace = [i.replace("\n", "") for i in nospace]
		nospace = ["".join(list(nospace))]
		nospace = [i.replace("  ", " ") for i in nospace]
		nospace = ["".join(list(nospace))]
		exec(f"{listname}{index}.append(nospace)")
		
	dat1 = root.findall(XMLTable + "/table/tgroup/tbody/row/entry[2]")
	
	for index, child in enumerate(dat1):
		nospace = child.text
		nospace = [i.replace("\n", "") for i in nospace]
		nospace = ["".join(list(nospace))]
		nospace = [i.replace("  ", " ") for i in nospace]
		nospace = ["".join(list(nospace))]
		exec(f"{listname}{index}.append(nospace)")
	
	dat2 = root.findall(XMLTable + "/table/tgroup/tbody/row/entry[2]")
	
	for index, child in enumerate(dat2):
		nospace = child.text
		nospace = [i.replace("\n", "") for i in nospace]
		nospace = ["".join(list(nospace))]
		nospace = [i.replace("  ", " ") for i in nospace]
		nospace = ["".join(list(nospace))]
		exec(f"{listname}{index}.append(nospace)")
		
	#Generate filename of the table extracted
	tablename.append(".csv")
	tablefile = ''.join(str(tablename) for tablename in tablename)
	
	#Stores data per table
	
	with open(tablefile, 'w', newline='') as f:
		writer = csv.writer(f)
		writer.writerow(columns)
		for index, child in enumerate(dat0):
			exec(f"writer.writerow({datarow}{index}")
