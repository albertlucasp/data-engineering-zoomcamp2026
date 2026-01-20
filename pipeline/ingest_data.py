#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


# Read a sample of the data
prefix = 'https://github.com/DataTalksClub/nyc-tlc-data/releases/download/yellow/'
url = f"{prefix}/yellow_tripdata_2021-01.csv.gz"
df = pd.read_csv(url)


# In[3]:


# Display the data
df


# In[5]:


# Display first rows
df.head()


# In[6]:


# Size of data
len(df)


# In[7]:


# The warning occurs because pandas cant determine the missing data dtype. So we need to specify it

dtype = {
    "VendorID": "Int64",
    "passenger_count": "Int64",
    "trip_distance": "float64",
    "RatecodeID": "Int64",
    "store_and_fwd_flag": "string",
    "PULocationID": "Int64",
    "DOLocationID": "Int64",
    "payment_type": "Int64",
    "fare_amount": "float64",
    "extra": "float64",
    "mta_tax": "float64",
    "tip_amount": "float64",
    "tolls_amount": "float64",
    "improvement_surcharge": "float64",
    "total_amount": "float64",
    "congestion_surcharge": "float64"
}

parse_dates = [
    "tpep_pickup_datetime",
    "tpep_dropoff_datetime"
]

df = pd.read_csv(
    url,
    dtype=dtype,
    parse_dates=parse_dates
)


# In[8]:


df


# In[9]:


df.head()


# In[10]:


df['tpep_pickup_datetime']


# In[11]:


# Dependencies (library) that used to interact between pandas and other DB (MySQL,oracle,Postgres,ets)
get_ipython().system('uv add sqlalchemy psycopg2-binary')


# In[12]:


# Create a DB connection
from sqlalchemy import create_engine
engine = create_engine('postgresql://root:root@localhost:5432/ny_taxi')


# In[13]:


# Get DDL Schema
print(pd.io.sql.get_schema(df, name='yellow_taxi_data', con=engine))


# In[14]:


# Create the table from the header,  head(n=0) ensure that we only create the table without data inside
df.head(n=0).to_sql(name='yellow_taxi_data', con=engine, if_exists='replace')


# Now that we have the table & the header only, we dont want to insert all of the data at once
# (take a long of time, we dont know the current progress / state, is it broken ?)
# Instead, we partition the data into chunks with equal size . Let's say chunks = 100,000 records
# read records for the first chunks - load to db, second chunks - load to db, so on..

# In[26]:


# State df_iter
df_iter = pd.read_csv(
    url,
    dtype = dtype,
    parse_dates = parse_dates,
    iterator = True,
    chunksize = 100000
)


# In[27]:


print(next(df_iter))


# In[28]:


# Libray to see the database loading process
get_ipython().system('uv add tqdm')
from tqdm import tqdm


# In[29]:


# Inserting data by iterate over chunks
for df_chunk in tqdm(df_iter):
    df_chunk.to_sql(name='yellow_taxi_data', con = engine, if_exists = 'append')


# In[ ]:




