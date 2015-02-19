#!/usr/bin/python
#country.py
#Roos Vermeulen

import sys

class Country:
	
	def __init__(self, name):
		self.name = name

	def __str__(self):
		return "Hello from " + self.name
	
def main(argv):
    if len(argv) >= 2:
        country = Country(argv[1])
        print("\n" + str(country) + "\n")
    else:
        print("Usage: country.py Arg1, voer voor Arg1 een string in.")
        exit(-1)

if __name__=="__main__":
    main(sys.argv)
