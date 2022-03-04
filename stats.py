##Page for adding csv to MySQL and statistical exploration
import pandas as pd
import sqlalchemy

##Bring back connection to Mysql and connect CSVs to mysql
con=sqlalchemy.create_engine('mysql+pymysql://root:4242@localhost/Puppy')

#I commented out the connection to mysql to prevent additional information from being added
df_puppy = pd.read_csv('Puppy_table.csv', index_col = False, delimiter =',')
#df_puppy.to_sql('puppies', con, schema = 'puppy', if_exists='append', index = False)

df_owner = pd.read_csv('Owner_table.csv', index_col = False, delimiter =',')
#df_owner.to_sql('owner', con, schema = 'puppy', if_exists='append', index = False)







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





