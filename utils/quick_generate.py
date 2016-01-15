#!/usr/bin/env python
# encoding: utf-8

"""
quick_generate.py
 
Created by Shuailong on 2016-01-15.

To quickly generate a solution template python script according to the problem name in Leetcode.

https://leetcode.com/

"""

import sys
import time

def main():
    if len(sys.argv) != 2:
    	print 'Usage: python quick_generate.py [problem_name]'
    	sys.exit(1)
    problem_name = sys.argv[1]
    print problem_name

    date = time.strftime("%Y-%m-%d")

    f = open('../solutions/'+problem_name+'.py', 'w')
    with open('template.py', 'r') as ff:
    	f.write(ff.read().replace('[problem_name]', problem_name).replace('[date]', date))

    f.close()
    
if __name__ == '__main__':
    main()
