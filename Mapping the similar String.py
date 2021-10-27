# Import the libraries
import pandas as pd
import numpy as np
import re

# Import the datasets
df1 = pd.read_csv(r'C:/Users/dkarar/Desktop/Mapping project/Files to test/Dr.Reddy_Prod_map_test.csv')
#df1
df2 = pd.read_csv(r'C:/Users/dkarar/Desktop/Mapping project/Files to test/Dr.Reddy_RC_map_test.csv')
#df2
df = pd.concat([df2, df1], axis=1)
#df

# Print the data in rows
def row_printing(df):
    for index, row in df.iterrows():
        print(row['Old_desc'], ' ', row['Old_ID'], ' ',row['New_desc'], ' ', row['New_ID'])
row_printing(df)

# Match the similar rows
def string_matching(df):
    index_list = []
    # Read dataframe rows
    Prod_index_count = 0
    for geo_string_prod in df['New_desc']:
        RC_index_count = 0
        check = 0
        #print(geo_string_prod)
        for geo_string_RC in df['Old_desc']:
            #print(geo_string_RC)
            if geo_string_prod == geo_string_RC:
                geo_index = RC_index_count
                #print(geo_index)
                index_list.append(geo_index)
                RC_index_count = RC_index_count + 1
                check = 1
            else:
                geo_index = "False"
                #print(geo_index)
                RC_index_count = RC_index_count + 1
                #check = 1
        if check == 0:
            index_list.append("False")
    return index_list
    #print(geo_index.head())
index_list = string_matching(df)

# Match the ID's
def match_ids(index_list,df):
    RC_id_list = []
    RC_dec_list = []
    for val in index_list:
        try:
            RC_id_list.append(df.iloc[val,3])
        except:
            RC_id_list.append("ID not found")
    for val in index_list:
        try:
            RC_dec_list.append(df.iloc[val,2])
        except:
            RC_dec_list.append("Member not found")
    df['New_desc'] = RC_dec_list
    df['New_ID'] = RC_id_list
    df = df.drop(["Description", "Key"],axis =1)
    return df
#df = print_ids(index_list,df)
df['Matched'] = pd.DataFrame(index_list)
df

# Create the csv file
df.to_csv('C:/Users/dkarar/Desktop/Mapping project/Output_similar_string.csv', header=True, index=False)