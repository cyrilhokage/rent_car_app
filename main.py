#!/usr/bin/python3

import sys, getopt
from Test import Test

#To test  : main.py data/input.json outputfile.json

def main(argv):
   inputfile = argv[0]
   outputfile = argv[1]

   test = Test()
   test.test(inputfile, outputfile)

   print ("Input file is : {} ".format(inputfile))
   print ("Output file is : {} ".format(outputfile))

if __name__ == "__main__":
   main(sys.argv[1:])