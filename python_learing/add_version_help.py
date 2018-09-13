#!/usr/bin/env python 
import sys

'''
- add version command
- add help command
- add sub command e.g: run_test.py run_demo1 
'''

Version = ' Version:1.0.0   Time: 2018/09/07'

def get_name():
    print "print name..."

def get_age():
    print "print age..."

if __name__== "__main__":

    
    if sys.argv[1].startswith('--'):
        option = sys.argv[1][2:]
        if option == 'version':
            print Version
        elif option == 'help':
            print '''Get aws resource command in python script.

Usage:

	./get_aws_resource.py <command>

The commands are:
  \t    aws get_ec2
            aws get_subnet

Additional help topics:
            --version : Prints the version number
            --help     : Display this help'''
        else:
            print "Unknow option.Please check your syntax carefully."
    else:
        if sys.argv[1] == 'get_age':
            get_age()
        elif sys.argv[1] == 'get_name':
            get_name()
        else:
            print "Unknow option.."
