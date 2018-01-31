#-*- coding: utf-8 -*-
import sys
import math
import os
from operator import itemgetter
import pandas as pd
import numpy as np
from scipy import interpolate
import csv

f = open('dataset.txt')
new_f = open('data2.txt', 'w')
linenum = 1
for line in f.readlines():
    line = line.strip('\n\r')
    print(line,file = new_f)
    if linenum == 5000:
        break
    linenum +=1
    #print(len(line))
f.close()
new_f.close()


