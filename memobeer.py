#!/usr/local/bin/python3
# MemoLab Beer Data Analysis
# An analysis of the MemoLab members' beer ratings using the Hypertools package

# change working directory
import os
os.chdir('/Users/mbluestone/Psych/beerdata/')
cwd = os.getcwd()

# import pkgs
import numpy
import pandas as pd
import matplotlib
import hypertools as hyp

## Wide Data Plotting
# import data
beers = pd.read_csv('Group_Wide.csv')
#print(beers.head())
small_beers = beers[beers.Taster != 'Dan']

# plot
hue = small_beers['Taster']
#plot = hyp.plot(small_beers, '.', hue=hue, title='Wide Data') # plots dots

## Multiple Data Sets Plotting w/ Alignment
# import data
ind_path = cwd + '/Individual/'
tasters = numpy.unique(hue)
taster_data = {}
for f in tasters:
    taster_data[f] = pd.read_csv(ind_path + "%s.csv" % f)
