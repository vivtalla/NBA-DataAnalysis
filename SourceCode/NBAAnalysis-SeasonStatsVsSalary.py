
# coding: utf-8

# In[1]:


get_ipython().run_line_magic('matplotlib', 'inline')

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
sns.set(style="darkgrid")


# In[3]:


df = pd.read_csv('Seasons_Stats.csv')


# In[4]:


df


# In[6]:


df.drop(df.index[:9547], inplace=True)


# We are only interested in player stats since 1990, so I am dropping the player stats from before that time.

# In[7]:


df


# In[8]:


df.drop('Unnamed: 0', axis=1)


# In[33]:


df.plot(x = 'G', y = 'PTS', kind = 'scatter')


# This graph shows the relationship between the points a player has in a season vs the number of games played.

# I am aware the finding behind this visualization is quite obvious. The point is for me to practice using pandas and Jupyter while exploring NBA data.

# In[34]:


df.plot(x = 'PTS', y = 'AST', kind = 'scatter')


# I was curious to see how Points and Assists related with a large sample size. This is an interesting distribution. Since every player in the NBA is included, there is a large population of points in the low ends of both points and assists, given these players log little to no time. It would be interesting to test this again on the best players in the league, as I believe the league is heavily dependent on points, and averaging PPG is likely a more important stat (in regards to getting a large contract) than any other stat in the league.

# In[36]:


df.rename(columns={'Player': 'player'}, inplace=True)


# In[37]:


df.dtypes


# In[14]:


df2 = pd.read_csv('nba_salaries.csv')


# In[15]:


df2


# In[22]:


df2.plot(x = 'player', y = 'salary', kind = 'box')


# This graph shows a distribution of salaries amongst the players in the dataset. This plot does not consider the date of the salary, which is significant given the rise in player salary over the years.

# In[23]:


df2.tail()


# In[24]:


df2.describe()


# Using the describe feature gives us a general understanding how the salaries are distributed in this data frame.
# As I claimed earlier that salaries have been increasing with time, the distribution shown above supoprts that intution given the salaries are larger for later years.

# In[26]:


df2.plot(x = 'season_end', y = 'salary', kind = 'scatter')


# This scatterplot visualizes the relationship between time and Salary in the NBA since 1990. The trend on the graph clearly demonstrates that NBA salary has been increasing overtime.

# In[27]:


df2.plot(x = 'season_end', y = 'salary', kind = 'line')


# Here I was simply curious to see what a line plot of this data would look like

# These visualizations show our intution to be true. Now we shall combine the salary data with player stats. Hopefully by combining the data we will get a better understanding between the relationship of players stats and players salaries. Intuition would lead us to believe that players producing better stats would be better paid. 

# In[40]:


df3 = pd.merge(df, df2, on = "player")


# In[41]:


df3


# In[42]:


df3.drop('Unnamed: 0', axis=1)


# I merged the two data frames by combining on the player attribute. This way each player now has both all his stats listed along with how much he made that season. 

# After looking more closly at the Season_Stats data set, there are new rows for the different team players played on, along with there total stats for that season. That could have important implications depending on the analysis being made. 

# In[44]:


df3.plot(x = 'PTS', y = 'salary', kind = 'scatter')


# In[ ]:


With the current data frame, here is a scatter plot of the Points Vs the salary. To get a better understanding, I need to remve duplicate player information by only keeping season stats, and removing stats 
indivudal players have when they switch team. Additionally, I need less data points, or need to add another variable. The current visualization basically 
shows its all over the place, and the salary depends on a lot much more than points.

