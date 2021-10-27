# Import the libraries

import pandas as pd
import numpy as np
import re
import os
import sys

# Read the file to test by using the pandas library

df_prodmap = pd.read_csv(r'C:/Users/dkarar/Desktop/Mapping project/Files to test/Dr.Reddy_Prod_map_test.csv')
#df_prodmap
df_RCmap = pd.read_csv(r'C:/Users/dkarar/Desktop/Mapping project/Files to test/Dr.Reddy_RC_map_test.csv')
#df_RCmap
df_NameCov = pd.read_csv(r'C:/Users/dkarar/Desktop/Mapping project/Company_Naming_Convention.csv')
#df_NameCov

# Concatinate both df_prodmap & df_RCmap file

final_df = pd.concat([df_prodmap, df_RCmap], axis = 1)
#final_df

index_Original_Name = []
index_Changed_Name = []
# create a list of values
list1 = df_NameCov['Original_Name'].to_list()
list2 = df_NameCov['Changed_Name'].to_list()
for string in final_df['New_desc']:
    #print(string)
    index = 0
    inc = 0
    li = list(string.split(" "))
    #print(li)
    for word in list2:
        length_word = 0
        list_word = list(word.split(" "))
        length_word = len(list_word)
        for i in range(length_word):
            if list_word[i] in li:
                inc = inc + 1
        if inc == length_word:
            #print("Matched")
            index_Changed_Name.append(index)
            inc = 0
        index = index + 1
        inc = 0
    #print(index_Changed_Name)

index_Original_Name = []
index_Changed_Name = []
list1 = df_NameCov['Original_Name'].to_list()
list2 = df_NameCov['Changed_Name'].to_list()
for string in final_df['Old_desc']:
    #print(string)
    index = 0
    inc = 0
    li = list(string.split(" "))
    #print(li)
    for word in list1:
        list_word = list(word.split(" "))
        length_word = len(list_word)
        for i in range(length_word):
            if list_word[i] in li:
                inc = inc + 1
        if inc == length_word:
            #print("Matched")
            index_Original_Name.append(index)
        index = index + 1
    #print(index_Original_Name)

# Make the final_df_1

final_df_1 = final_df.copy()
#final_df_1

# Check the length

len_of_df_NameCov = len(df_NameCov)
#len_of_df_NameCov

# Checking the length of the strings

for len_of_df_NameCov in range(0,len_of_df_NameCov):
    subval = len_of_df_NameCov
    #print(subval)
    subname = df_NameCov.iloc[subval,0]
    #print(subname)
    subname_1 = df_NameCov.iloc[subval,1]
    #print(subname_1)
    subdata = final_df_1.copy()

#Remove the first element in a string from the data set

subdata['New_desc'] = subdata['New_desc'].str.replace('ADUSA', '')
subdata['New_desc'] = subdata['New_desc'].str.replace('ABSCO', '')
subdata['New_desc'] = subdata['New_desc'].str.replace('ABSCO ABS', '')
subdata['New_desc'] = subdata['New_desc'].str.replace('ABSCO SWY', '')
subdata['New_desc'] = subdata['New_desc'].str.replace('KR', '')
subdata['New_desc'] = subdata['New_desc'].str.replace('SEG', '')
#subdata['Prod_desc']

subdata['Old_desc'] = subdata['Old_desc'].str.replace('Ahold Delhaize', '')
subdata['Old_desc'] = subdata['Old_desc'].str.replace('Albertsons Companies', '')
subdata['Old_desc'] = subdata['Old_desc'].str.replace('Albertsons Companies-Albertsons', '')
subdata['Old_desc'] = subdata['Old_desc'].str.replace('Albertsons Companies-Safeway', '')
subdata['Old_desc'] = subdata['Old_desc'].str.replace('Kroger', '')
subdata['Old_desc'] = subdata['Old_desc'].str.replace('Southeastern Grocers', '')
#subdata['RC_desc']

# Match the rows

def row_matching(final_df_1):
    index_list = []
    # Read dataframe rows
    Prod_index_count = 0
    for geo_string_prod in subdata['New_desc']:
        RC_index_count = 0
        check = 0
        #print(geo_string_prod)
        for geo_string_RC in subdata['Old_desc']:
            #print(geo_string_RC)
            if geo_string_prod == geo_string_RC:
                geo_index = RC_index_count
                #print(geo_index)
                index_list.append(geo_index)
                RC_index_count = RC_index_count + 1
                check = 1
            else:
                geo_index = "False"
                # print(geo_index)
                RC_index_count = RC_index_count + 1
                # check = 1
        if check == 0:
            index_list.append("False")
    return index_list
    # print(geo_index.head())
index_list = row_matching(final_df_1)

# Add the starting names_2

new_list1 = []
for i, j in zip (index_Original_Name,subdata['Old_desc'].astype(str)):
    value_of_prod1 = list1[i] + j
    new_list1.append(value_of_prod1)
#print(new_list1)

subdata.drop(['Old_desc'], axis=1)
subdata['Old_desc'] = pd.DataFrame(new_list1)
#subdata['RC_desc']

# Add the starting names_1

new_list2 = []
for i,j in zip (index_Original_Name,subdata['New_desc'].astype(str)):
    value_of_prod2 = list2[i] + j
    new_list2.append(value_of_prod2)
#print(new_list2)

subdata.drop(['New_desc'], axis=1)
subdata['New_desc'] = pd.DataFrame(new_list2)
#subdata['Prod_desc']

subdata['New_ID'] = final_df_1['New_ID']
#subdata['Prod_ID']

subdata['Old_ID'] = final_df_1['Old_ID']
#subdata['RC_ID']

subdata = pd.concat([subdata['New_desc'], subdata['New_ID'], subdata['Old_desc'], subdata['Old_ID']], axis = 1)
#subdata

# Match the ID's

def match_ids(index_list, subdata):
    RC_id_list = []
    RC_dec_list = []
    for val in index_list:
        try:
            RC_id_list.append(df.iloc[val, 3])
        except:
            RC_id_list.append("ID not found")
    for val in index_list:
        try:
            RC_dec_list.append(df.iloc[val, 2])
        except:
            RC_dec_list.append("Member not found")
    subdata['New_desc'] = RC_dec_list
    subdata['New_ID'] = RC_id_list
    subdata = subdata.drop(["Description", "Key"], axis=1)
    return subdata
# final_df_1 = print_ids(index_list,final_df_1)
subdata['Matched'] = pd.DataFrame(index_list)
subdata

# Create the csv file
subdata.to_csv('C:/Users/dkarar/Desktop/Mapping project/Output_name_changed.csv', header=True, index=False)
