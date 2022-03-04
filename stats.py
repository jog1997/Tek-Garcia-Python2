##Page for statistical exploration
import pandas as pd
import sqlalchemy

##Bring back connection to Mysql
con=sqlalchemy.create_engine('mysql+pymysql://root:4242@localhost/Puppy')

## Import both databases using mysql and pandas
df_puppy=pd.read_sql('puppies',con)
df_owner=pd.read_sql('owner',con)
print('This is the puppy table.\n', df_puppy)
print('This is the owner table.\n', df_owner)
print('\n')
'''I exported the CSV from MySQL query and stored in the same directory 
(This was mainly for my use to explore data statistics prior Mysql connection
df_puppy = pd.read_csv('Puppy_table.csv')
df_owner = pd.read_csv('Owner_table.csv')
print(df_owner)'''


##Statistics for Puppy Table

#this gives us a brief overview of the table
print("A brief overview of the Puppy table with the count being the amount of variables. \n", df_puppy.describe())
#this code gives us the amount of variables in each column
print("This shows the different columns. \n", df_puppy.count())




##Statistics for Owner Table // Follow
print('\nThe following are the statistics for the Owner Table')

print("A brief overview of the Owner table with the count being the amount of variables. \n", df_owner.describe())
print("This shows the different columns. \n", df_owner.count())


print('\n The Group By function is below:')
groupcolor = df_puppy.groupby(['color'])['color'].count()
print(groupcolor)





