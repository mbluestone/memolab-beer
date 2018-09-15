#!/usr/local/bin/python3
# MemoLab Beer Data Analysis Test
# Python script for testing Hypertools with our beer data

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
print(beers)
small_beers = beers[beers.Taster != 'Dan'] #didn't rate all of the beers

# plot
hue = small_beers['Taster']

plot = hyp.plot(small_beers, 'o', hue=hue, labels=list(hue), title='Beer Space') # plots dots
