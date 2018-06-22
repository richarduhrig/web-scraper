
# coding: utf-8

# In[1]:

##### inline
import datetime
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sbn
import pandas as pd
#from __future__ import division
import pymc3 as pm3
import statsmodels.formula.api as smf
import math
import random
import scipy
import csv

import pandas_datareader.data as wb

from numba import jit


# In[26]:

#create empty DF
index = np.arange(0)
columns = ['Home Team','Away Team','Spread','Total','Home Score','Away Score','Actual Spread','Actual Total']
table = pd.DataFrame(index=index,columns = columns)
table = table.fillna(0) # with 0s rather than NaNs


# In[5]:

#team dict
team_dict = {}
#team_list[1] = 1

team_dict[0] = 'Arizona Cardinals'
team_dict[1] = 'Atlanta Falcons'
team_dict[2] = 'Baltimore Ravens'
team_dict[3] = 'Buffalo Bills'
team_dict[4] = 'Carolina Panthers'
team_dict[5] = 'Chicago Bears'
team_dict[6] = 'Cincinnati Bengals'
team_dict[7] = 'Cleveland Browns'
team_dict[8] = 'Dallas Cowboys'
team_dict[9] = 'Denver Broncos'
team_dict[10] = 'Detroit Lions'
team_dict[11] = 'Green Bay Packers'
team_dict[12] = 'Houston Texans'
team_dict[13] = 'Indianapolis Colts'
team_dict[14] = 'Jacksonville Jaguars'
team_dict[15] = 'Kansas City Chiefs'
team_dict[16] = 'Miami Dolphins'
team_dict[17] = 'Minnesota Vikings'
team_dict[18] = 'New England Patriots'
team_dict[19] = 'New Orleans Saints'
team_dict[20] = 'New York Giants'
team_dict[21] = 'New York Jets'
team_dict[22] = 'Oakland Raiders'
team_dict[23] = 'Philadelphia Eagles'
team_dict[24] = 'Pittsburgh Steelers'
team_dict[25] = 'San Diego Chargers'
team_dict[26] = 'San Francisco 49ers'
team_dict[27] = 'Seattle Seahawks'
team_dict[28] = 'St. Louis Rams'
team_dict[29] = 'Tampa Bay Buccaneers'
team_dict[30] = 'Tennessee Titans'
team_dict[31] = 'Washington Redskins'


# In[28]:

team_id1_list = []
team_id2_list = []
spread_list = []
total_list = []

home_team_score_list = []
away_team_score_list = []
spread_result_list = []
total_result_list = []

for i in range(1000):
    #game characteristics
    team_id1 = random.randint(1,31)
    team_id2 = team_id1
    team1 = team_dict[team_id1]
    team2 = team_dict[team_id1]
    while team_id2 == team_id1:
        team_id2 = random.randint(1,31)
    if team_id2 == team_id1:
        break
    team2 = team_dict[team_id2]
    spread = random.randint(-9,10)
    total = random.randint(38,59)
    
    #game results
    home_team_score = random.randint(0,45)
    away_team_score = random.randint(0,45)
    spread_result = away_team_score - home_team_score
    total_result = away_team_score + home_team_score
    
    team_id1_list.append(team1)
    team_id2_list.append(team2)
    spread_list.append(spread)
    total_list.append(total)
    
    home_team_score_list.append(home_team_score)
    away_team_score_list.append(away_team_score)
    spread_result_list.append(spread_result)
    total_result_list.append(total_result)


# In[29]:

for i in range(1000):
    rows = ([[team_id1_list[i],team_id2_list[i],spread_list[i],total_list[i],home_team_score_list[i],away_team_score_list[i],spread_result_list[i],total_result_list[i]]])
    for row in rows:
        table.loc[len(table)] = row


# In[30]:

table.head


# In[23]:

table['Spread']


# In[31]:

table.to_excel('FakeData3.xlsx')


# In[ ]:



