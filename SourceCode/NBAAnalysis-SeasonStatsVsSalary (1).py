
# coding: utf-8

# In[2]:


get_ipython().magic(u'matplotlib inline')

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
sns.set(style="darkgrid")


# In[3]:


df = pd.read_csv('Seasons_Stats.csv')


# In[4]:


df


# In[5]:


df.drop(df.index[:9547], inplace=True)


# We are only interested in player stats since 1990, so I am dropping the player stats from before that time.

# In[6]:


df


# In[7]:


df.drop('Unnamed: 0', axis=1)


# In[8]:


df.plot(x = 'G', y = 'PTS', kind = 'scatter')


# This graph shows the relationship between the points a player has in a season vs the number of games played.

# I am aware the finding behind this visualization is quite obvious. The point is for me to practice using pandas and Jupyter while exploring NBA data.

# In[9]:


df.plot(x = 'PTS', y = 'AST', kind = 'scatter')


# I was curious to see how Points and Assists related with a large sample size. This is an interesting distribution. Since every player in the NBA is included, there is a large population of points in the low ends of both points and assists, given these players log little to no time. It would be interesting to test this again on the best players in the league, as I believe the league is heavily dependent on points, and averaging PPG is likely a more important stat (in regards to getting a large contract) than any other stat in the league.

# In[10]:


df.rename(columns={'Player': 'player'}, inplace=True)


# In[11]:


df.dtypes


# In[12]:


df2 = pd.read_csv('nba_salaries.csv')


# In[13]:


df2


# In[14]:


df2.plot(x = 'player', y = 'salary', kind = 'box')


# This graph shows a distribution of salaries amongst the players in the dataset. This plot does not consider the date of the salary, which is significant given the rise in player salary over the years.

# In[15]:


df2.tail()


# In[16]:


df2.describe()


# Using the describe feature gives us a general understanding how the salaries are distributed in this data frame.
# As I claimed earlier that salaries have been increasing with time, the distribution shown above supoprts that intution given the salaries are larger for later years.

# In[17]:


df2.plot(x = 'season_end', y = 'salary', kind = 'scatter')


# This scatterplot visualizes the relationship between time and Salary in the NBA since 1990. The trend on the graph clearly demonstrates that NBA salary has been increasing overtime.

# In[18]:


df2.plot(x = 'season_end', y = 'salary', kind = 'line')


# Here I was simply curious to see what a line plot of this data would look like

# These visualizations show our intution to be true. Now we shall combine the salary data with player stats. Hopefully by combining the data we will get a better understanding between the relationship of players stats and players salaries. Intuition would lead us to believe that players producing better stats would be better paid. 

# In[19]:


df3 = pd.merge(df, df2, on = "player")


# In[20]:


df3


# In[21]:


df3.drop('Unnamed: 0', axis=1)


# I merged the two data frames by combining on the player attribute. This way each player now has both all his stats listed along with how much he made that season. 

# After looking more closly at the Season_Stats data set, there are new rows for the different team players played on, along with there total stats for that season. That could have important implications depending on the analysis being made. 

# In[22]:


df3.plot(x = 'PTS', y = 'salary', kind = 'scatter')


# With the current data frame, here is a scatter plot of the Points Vs the salary. To get a better understanding, I need to remve duplicate player information by only keeping season stats, and removing stats 
# indivudal players have when they switch team. Additionally, I need less data points, or need to add another variable. The current visualization basically 
# shows its all over the place, and the salary depends on a lot much more than points.

# In[23]:


df3.plot(x = 'G', y = 'salary', kind = 'scatter')


# From ths graph, we see that salaries do gradually increase as more games are played. It makes sense that NBA Teams value durability in a player, leading to these higher salaries.

# In[24]:


df3.plot(x = 'MP', y = 'salary', kind = 'scatter')


# There is a slight increase when comparing minutes played to the player salary. This is not as dramatic as the one when comparing salary to games. Different teams likely have different philosophies on how long to play a player/ different teams have different depths. Additionally, when teams are up by a lot, they sub out their top players who normally would log a lot of minutes and have the highest salaries. This could explain why this graph shows less of a direct relationship compared to the previous graph.

# In[27]:


df3.plot(x = 'TOV', y = 'salary', kind = 'scatter')


# I was interested in looking at how the turnover - salary ratio effects salary. This graph is pretty misleading, however, given that players who rarely play will log no minutes, leading to less chances to turn the ball over. Compared to a top point guard in the league who pay log 40 minutes a game, giving them a high chance to turn the ball over. For a better analysis, we should perform a regression and attempt to see how various variables account for the differentiation in salary.

# In[28]:


df3.plot(x = 'Age', y = 'salary', kind = 'scatter')


# The plot between age and salary goes about as expected. The highest paid players are the ones in their "Peak athletic age of about 22-27. After that the salaries begin to drop off, as teams are less likely to invest in long term, max contract for older players out of their prime

# In[30]:


df3.plot(x = 'Year', y = 'salary', kind = 'scatter')


# This plot looks visualizes salaries compared to time. Salaries have been increasing as the NBA is expanding and bringing in larger revenues.
