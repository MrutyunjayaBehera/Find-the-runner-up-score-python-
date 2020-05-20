#TASK

#Given the participants' score sheet for your University Sports Day,
#you are required to find the runner-up score. You are given n scores.
#Store them in a list and find the score of the runner-up.

#Input Format

#The first line contains n. The second line contains an array A[] of n integers each separated by a space.



#CODE

import math
import os
import random
import re
import sys

k = input()                #provide the input scores with a space between each....remember k is a string here with spaces.
arr = []
arr = k.split(" ")
print(arr)

large = max(arr)
n = len(arr)
for i in range(n):
	if large == max(arr):
		arr.remove(max(arr))
print(max(arr))

#ENJOY
