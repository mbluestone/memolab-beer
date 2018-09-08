# MemoLab Beer Data Analysis
# An analysis of the MemoLab members' beer ratings using the Hypertools package

# change working directory
import os
os.chdir('/Users/mbluestone/Psych/')
cwd = os.getcwd()

# import pkgs
import numpy
import pandas
import matplotlib
import hypertools as hyp

# import data
beers = pandas.read_csv('Group.csv')
print(beers.head())

# plot
hue = beers['Taster']
plot = hyp.plot(beers, '.', hue=hue, labels=hue) # plots dots
