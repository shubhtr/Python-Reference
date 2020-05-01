#!/usr/bin/env python3

import csv

with open('monty.py', newline='\n') as csvfile:
	spamreader = csv.reader(csvfile, delimiter=',')
	for row in spamreader:
		print(', '.join(row))

