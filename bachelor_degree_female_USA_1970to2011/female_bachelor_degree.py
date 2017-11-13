# -*- coding: utf-8 -*-

import pandas as pd
import matplotlib.pyplot as plt
import os
import glob

cwd = os.getcwd()
path = "../data/"

women_majors = pd.read_csv(path + 'percent-bachelors-degrees-women-usa.csv')

import matplotlib.style as style
style.use('fivethirtyeight')

# 20% threshold
under_20 = women_majors.loc[0, women_majors.loc[0]<20]

colours = [(0.0,0.0,0.0), (230.0/255,159.0/255,0.0), (86.0/255,180.0/255.0,233.0/255), (0.0,158.0/255,115.0/255),
          (213.0/255,94.0/255,0.0), (0.0,114.0/255,178.0/255)]

fte_20 = women_majors.plot(x = 'Year', y = under_20.index, figsize = (12,8), color = colours, legend = False)
fte_20.tick_params(axis = 'both', which = 'major', labelsize = 18)

fte_20.set_yticklabels(labels = [-10, '0    ', '10   ', '20   ', '30   ', '40   ', '50%'])

fte_20.axhline(y = 0, color = 'black', linewidth = 1.3, alpha = 0.7)

fte_20.set_xlim(left = 1969, right = 2011)

fte_20.xaxis.label.set_visible(False)

fte_20.text(x = 1965.8, y = -7,
            s = '    pukkapad / Mariana                                                                        Source: National Center for Education Statistics  '   ,
           fontsize = 14, color = '#f0f0f0',  backgroundcolor = 'grey')

# Title and subtile
fte_20.text(x = 1966.65, y = 62.7,
           s = "Gender gap evolution for extreme cases",
           fontsize = 26, weight = 'bold', alpha = 0.75)

fte_20.text(x = 1966.65, y = 57,
           s = "Percentage of Bachelors conferred to women from 1970 to 2011 in the US for\nextreme cases where the percentage was less than 20% in 1970",
            fontsize = 19, weight = 'bold', alpha = 0.75)


# Add labels
fte_20.text(x = 1994, y = 44, s = 'Agriculture', color = colours[0], weight = 'bold', rotation = 33,
             backgroundcolor = '#f0f0f0')
fte_20.text(x = 1985, y = 42.2, s = 'Architecture', color = colours[1], weight = 'bold', rotation = 18,
              backgroundcolor = '#f0f0f0')
fte_20.text(x = 2004, y = 51, s = 'Business', color = colours[2], weight = 'bold', rotation = -5,
               backgroundcolor = '#f0f0f0')
fte_20.text(x = 2001, y = 30, s = 'Computer Science', color = colours[3], weight = 'bold', rotation = -42.5,
              backgroundcolor = '#f0f0f0')
fte_20.text(x = 1987, y = 11.5, s = 'Engineering', color = colours[4], weight = 'bold',
              backgroundcolor = '#f0f0f0')
fte_20.text(x = 1976, y = 25, s = 'Physical Sciences', color = colours[5], weight = 'bold', rotation = 27,
              backgroundcolor = '#f0f0f0')

plt.savefig(path + '../plots/under20pct.png', bbox_inches='tight')