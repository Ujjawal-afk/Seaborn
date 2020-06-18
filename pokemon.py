import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('Pokemon.csv', encoding = 'unicode_escape', index_col = 0)

df.head()

sns.lmplot(x = 'Attack', y = 'Defense', data = df)

sns.lmplot(x = 'Attack', y = 'Defense' , data = df, fit_reg = False, hue ='Stage')

plt.xlim(0,None)
plt.ylim(0,None)

sns.boxplot(data = df)

df.columns

stats_df = df.drop(['Total','Legendary','Stage'], inplace = False, axis = 1)
stats_df.head()
sns.boxplot(data = stats_df)

sns.set_style('whitegrid')

sns.violinplot(x='Type 1',y='Attack',data = df)

pkmn_type_colors = ['#78C850',  # Grass
                    '#F08030',  # Fire
                    '#6890F0',  # Water
                    '#A8B820',  # Bug
                    '#A8A878',  # Normal
                    '#A040A0',  # Poison
                    '#F8D030',  # Electric
                    '#E0C068',  # Ground
                    '#EE99AC',  # Fairy
                    '#C03028',  # Fighting
                    '#F85888',  # Psychic
                    '#B8A038',  # Rock
                    '#705898',  # Ghost
                    '#98D8D8',  # Ice
                    '#7038F8',  # Dragon
                   ]

sns.violinplot(x='Type 1',y='Attack',data = df,palette = pkmn_type_colors)

sns.swarmplot(x='Type 1', y='Attack', data=df, 
              palette=pkmn_type_colors)

df['Type 1'].value_counts()

# Set figure size with matplotlib
plt.figure(figsize=(10,6))
 
# Create plot
sns.violinplot(x='Type 1',
               y='Attack', 
               data=df, 
               inner=None, # Remove the bars inside the violins
               palette=pkmn_type_colors)
 
sns.swarmplot(x='Type 1', 
              y='Attack', 
              data=df, 
              color='k', # Make points black
              alpha=0.7) # and slightly transparent
 
# Set title with matplotlib
plt.title('Attack by Type')

# Melt DataFrame
'''so melt function melts down all the columns of the DATAFRAME that we have selected
only those columns are not melted those are in ID_VARS
and then all the melted columns are then put in a new column which is specified in VAR_NAME
the specified column name in VAR_NAME store the column names of the columns that are melted
and a new column is made automatically named VALUES that stores the VALUES correspending to the
column name in column name specified by VAR_NAME
'''
melted_df = pd.melt(stats_df, 
                    id_vars=["Name", "Type 1", "Type 2"], # Variables to keep
                    var_name="Stat") # Name of melted variable
melted_df.head()

plt.figure(figsize=(10,6))
# Swarmplot with melted_df
sns.swarmplot(x='Stat', y='value', data=melted_df, 
              hue='Type 1')

	
# 1. Enlarge the plot
plt.figure(figsize=(10,6))
 
sns.swarmplot(x='Stat', 
              y='value', 
              data=melted_df, 
              hue='Type 1', 
              split=True, # 2. Separate points by hue
              palette=pkmn_type_colors) # 3. Use Pokemon palette
 
# 4. Adjust the y-axis
plt.ylim(0, 260)
 
# 5. Place legend to the right
plt.legend(bbox_to_anchor=(1, 1), loc = 2)

# Calculate correlations
corr = stats_df.corr()
 
# Heatmap
sns.heatmap(corr)

	
# Distribution Plot (a.k.a. Histogram)
sns.distplot(df.Attack)

# Count Plot (a.k.a. Bar Plot)
sns.countplot(x='Type 1', data=df, palette=pkmn_type_colors)
 
# Rotate x-labels
plt.xticks(rotation=45)

# Factor Plot
g = sns.factorplot(x='Type 1', 
                   y='Attack', 
                   data=df, 
                   hue='Stage',  # Color by stage
                   col='Stage',  # Separate by stage
                   kind='swarm') # Swarmplot
 
# Rotate x-axis labels
g.set_xticklabels(rotation=-45)
 
# Doesn't work because only rotates last plot
# plt.xticks(rotation=-45)


# Density Plot
sns.kdeplot(df.Attack, df.Defense)

# Joint Distribution Plot
sns.jointplot(x='Attack', y='Defense', data=df)