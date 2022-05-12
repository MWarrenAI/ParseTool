#Code was adapted from the tutorial provided by freeCodeCamp.org (Credit to John Elder):
#https://www.youtube.com/watch?v=byHcYRoMgI4

#Their referred url link to their github:
#https://github.com/flatplanet/Intro-To-TKinter-Youtube-Course

#A handy piece of code for clearing the screen provided by Grepper (credit to Expensive Eagle):
#https://www.codegrepper.com/code-examples/python+os.system+clear+screen

# Author: 		Mark Warren
# Company: 		Staffordshire University
# Date:			12/05/2022
# Purpose:		A General Purpose built Program that removes whitespace found in between data. This file stores the menu.
# Version: 		1.0
# Software: 	Python 3.8
# Dependancies:	csv, itertools, sys, os, xml.etree.ElementTree, tkinter, tk, filedialog

# Note: This was salvaged from a fully functioning program I developed and I have remade this in case I wish to build upon the tool further.

#This clears the command prompt

def clearpage():
    #windows
    if name == 'nt':
        _ = system ('cls')
    # mac/linux
    else:
        _ = system ('clear')

# Basic Menu allows user to call functions stored in the Parse Commands file.

def selopt():
    optmenu()
    opt = 0
    whilte opt == 0:
        try:
            opt = int(input("Enter a option from the above:"))
            if opt < 1 or opt > 3:
                raise Exception
        except Exception:
            clearpage()
            print("Invalid Entered Choice. Choose from available Options below.")
            optmenu()
            opt = 0
        
        else:
            if opt == 1:
                ask()
                yesno()
                Parsecom.create()
                print("Data Parsed and created.")
                backtomainmenu()
            if opt == 2:
                Parsecom.changetree()
                backtomainmenu()
            if opt == 3:
                sys.exit()

def optmenu():
    clearpage()
    print("Welcome to the Basic Parser Program")
    print("Choose an Option:")
    print("1. Parse some Pickles")
    print("2. Change Pickle File Location")
    print("3. Exit Program")

def ask():
    clearpage()
    print("Are you sure you wish to Create or Reset the default table(s) generated?")
    print("{:<10}".format("Y- Yes"), "{:<10}".format("N- No"))
    
def yesno():
    yn = None
    while yn not in ("yes", "no", "y", "n"):
        try:
            yn = str(input("Enter a option from the above:"))
            if yn.lower() not in ("yes", "no", "y", "n"):
                raise Exception
        except Exception:
            clearpage()
            print("Invalid Entered Choice. Choose from the available Options below.")
            yn = None
            ask()
        else:
            if yn.lower() == "yes" or yn.lower() == "y":
                print("Creating...")
                break
            elif yn.lower() == "no" or yn.lower() == "n":
                backtomainmenu()
                
def backtomainmenu():
    input("Enter anything to continue...")
    clearpage()
    selopt()

clearpage()
selopt()