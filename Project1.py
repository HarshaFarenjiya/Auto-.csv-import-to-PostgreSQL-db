#!/usr/bin/env python
# coding: utf-8

# # Automated .csv file import into a PostgreSQL database

# ## Introduction :

# ### In PostgreSQL, it is necessary to specify the data types of columns before importing data. This can be more cumbersome, especially when dealing with tables with a large number of columns. The requirement to define the data types in advance can make the import process more time-consuming and error-prone, as it involves accurately specifying the data types for each column.
# ### However, it's important to note that PostgreSQL's approach of explicitly defining data types offers the advantage of data integrity enforcement and stricter control over the data being imported. It ensures that the imported data aligns with the defined table schema, reducing the risk of data inconsistencies or integrity violations.

# In[1]:


import os
import numpy as np
import pandas as pd
import psycopg2


# In[2]:


h = os.getcwd()


# In[3]:


os.listdir(h)


# In[4]:


#find CSV files in my current working directory #isolate only the CSV files

csv_files = []
for file in os.listdir(os.getcwd()):
    if file.endswith('.csv'):
        csv_files.append(file)


# In[5]:


#make a new directory
dataset_dir = 'Data'

#create the bash command to make a new directory
# mkdir dataset_dir
try:
    mkdir = 'mkdir {0}'.format(dataset_dir)
    os.system(mkdir)
except:
    pass


# In[6]:


#move the CSV files in the new directory
import shutil
#mv filename directory
for csv in csv_files:
    src_file = os.path.join(h, csv)  # Full path of the source file
    dst_file = os.path.join(dataset_dir, csv)  # Full path of the destination file
    shutil.move(src_file, dst_file)
    print(f"Moved {csv} to {dst_file}")


# In[7]:


data_path = h+'/'+dataset_dir+'/'

df = {}  # Use curly braces to initialize an empty dictionary instead of a list
for file in csv_files:
    try:
        df[file] = pd.read_csv(data_path+file)
    except UnicodeDecodeError:
        df[file] = pd.read_csv(data_path+file, encoding="UTF-8")
    print(file)


# In[8]:


for k in csv_files:
    dataframe = df[k]
    clean_tbl_name =  k.lower().replace(" ","_").replace("?","") \
                        .replace("-","_").replace(r"/","_").replace("\\","_").replace("%","") \
                        .replace(")","").replace(r"(","").replace("$","")

    # remove.csv extension from clean_tbl_name
    tbl_name = '{0}'.format(clean_tbl_name.split('.')[0])
    print(tbl_name)

    #clean table columns
    dataframe.columns = [x.lower().replace(" ","_").replace("?","") \
                        .replace("-","_").replace(r"/","_").replace("\\","_").replace("%","") \
                        .replace(")","").replace(r"(","").replace("$","") for  x in dataframe.columns]
    

    #replacement dictionary that maps pandas dtypes to sql dtypes
    replacements = {
        'object' : 'varchar', 'float64' : 'float',
        'int64' : 'int',
        'datetime64' : 'timestamp',
        'timedelta64 [ns]' : 'varchar'
    }
    #table schema
    col_str = ", ".join("{} {}".format (n, d) for (n, d) in zip(dataframe.columns, dataframe.dtypes.replace(replacements))) 
    print(col_str)

    #open a database connection

    host = 'localhost'
    dbname = 'postgres'
    username = 'postgres'
    password = '1111'
    
    conn_string = "host=%s dbname=%s user=%s password=%s" % (host, dbname, username, password)
    conn = psycopg2.connect (conn_string)
    cursor = conn.cursor()
    print('opened database successfully')

    #drop table with same name 
    cursor.execute("drop table if exists %s;" % (tbl_name))
    
    #create table
    query = 'CREATE TABLE "%s" (%s);'
    cursor.execute(query % (tbl_name, col_str))

    #cursor.execute("create table %s (%s);" % (tbl_name, col_str))
    print('{0} was created successfully'.format(tbl_name))
    
    #insert values to table
    
    #save df to csv
    dataframe.to_csv (k, header=dataframe.columns, index=False, encoding='UTF-8')
    
    #open the csv file, save it as an object
    my_file = open(k)
    print('file opened in memory')

    #upload to db
    
    SQL_STATEMENT = """
    COPY %s FROM STDIN WITH
        CSV
        HEADER
        DELIMITER AS ','
    """
    
    cursor.copy_expert (sql=SQL_STATEMENT % tbl_name, file=my_file)
    print('file copied to db')

    cursor.execute("grant select on table %s to public" % tbl_name)
    conn.commit()
    
    cursor.close()
    print('table {0} imported to db completed'.format(tbl_name))

#for loop end message
print('all tables have been successfully imported into the db')


# In PostgreSQL, column names cannot contain certain special characters, such as colons (":"). The error is caused by the colon in the column name "unnamed:_0".
#To fix this issue, you should choose a valid column name that follows the naming rules:

#1.Column names must start with a letter or an underscore (_).
#2.Subsequent characters can include letters, digits, and underscores.
#3.Avoid using special characters or spaces in column names.




