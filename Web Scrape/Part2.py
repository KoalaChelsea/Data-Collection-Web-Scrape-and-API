#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep  9 22:36:04 2018

@author: Chelsea Wang
"""

# =============================================================================
# This is The python file for ANLY501 Homework of 09/10 Class Part 2 
# =============================================================================
# ## Part 2
# Part 2:  
# 1.      Use your API Key to write a Python 3 program to directly query the 
# AirNow API for AQI data.
# a.      Your program should read in data from an input file that contains any 
# 10 zip codes and should gather AQI data for each zip code location
#  (include at least ozone and PM2.5). Name the input file, INPUT.txt.
# b.      Your program should print out a table of the results and should create
#  a .csv file of the results. Name file AQI_output.csv.
# 2.      Repeat all of the above using latitude and longitude instead. 
# Create the appropriate input and output files.
#  
# Using a zip folder, submit your .py program, your input files, 
# and the output of results (as .csv), 
# and your Word or text document containing the answers to part 1. 
# Include a README.txt file that explains what each document contains. 
# This is an individual assignment.
# 
# =============================================================================
#input1: a file contains at least 10 zip code
#input2: a file conatins at least 10 latitude and longtitude
# =============================================================================

# Python 3 program to query AQI data by zip code 


import urllib
from urllib.request import urlopen
import json
from pathlib import Path
import pandas as pd
#%%


## this is the help function to query by zip code
def UseUrllib_by_zipcode(BaseURL, URLPost,outfile):
    try:
        #format the url 
        URL=BaseURL + "?"+ urllib.parse.urlencode(URLPost)
        WebURL=urlopen(URL)
        data=WebURL.read()
        #encode the content and convert to json format
        encoding = WebURL.info().get_content_charset('utf-8')
        jsontxt = json.loads(data.decode(encoding))
        #define column names of the dataframes 
        col_names=['zipcode', 'DateObserved', 'state', 'City', 'AQIType', 'AQIValue']
        my_df  = pd.DataFrame(columns = col_names)
        #extract necessary infomation to print out
        if(len(jsontxt)!=0):
            for list in jsontxt:               
                    AQIType = list['ParameterName']
                    City=list['ReportingArea']
                    AQIValue=list['AQI']
                    zipcode=URLPost['zipCode']
                    DateObserved=list['DateObserved']
                    state=list['StateCode']
                    my_df=my_df.append({col_names[0]:zipcode, col_names[1]:DateObserved ,\
                    col_names[2]:state, col_names[3]:City ,\
                    col_names[4]:AQIType, col_names[5]:AQIValue \
                    }, ignore_index=True)
            my_df.to_csv(outfile, index=None, sep=',', mode='a',header=None)
            return 1
        else:
            return -1
    except:
        print("No revelant zipcode infomation found. Please check your input")
        return -1

## this is the help function to query by latituede and longitude 
def UseUrllib_by_lat_long(BaseURL, URLPost,outfile):
    try:
        URL=BaseURL + "?"+ urllib.parse.urlencode(URLPost)
        WebURL=urlopen(URL)
        data=WebURL.read()
        encoding = WebURL.info().get_content_charset('utf-8')
        jsontxt = json.loads(data.decode(encoding))
        #print(jsontxt)
        col_names2=['latitude','longitude','DateObserved', 'state', 'City', 'AQIType', 'AQIValue']
        my_df2  = pd.DataFrame(columns = col_names2)
        if(len(jsontxt)!=0):
            for list in jsontxt:
                    AQIType = list['ParameterName']
                    City=list['ReportingArea']
                    AQIValue=list['AQI']
                    DateObserved=list['DateObserved']
                    state=list['StateCode']
                    latitude=list['Latitude']
                    longitude=list['Longitude']
                    my_df2=my_df2.append({col_names2[0]:latitude,\
                                        col_names2[1]:longitude,\
                                        col_names2[2]:DateObserved ,\
                    col_names2[3]:state, col_names2[4]:City ,\
                    col_names2[5]:AQIType, col_names2[6]:AQIValue \
                    }, ignore_index=True)
            my_df2.to_csv(outfile, index=None, sep=',', mode='a',header=None)
            return 1
        else:
            return -1
    except:
        print("No revelant infomation found. Please check your input")
        return -1
            

#%%    
    
def main():
    
# =============================================================================
# The query tool to query by zipcode
# =============================================================================
    outfile="AQI_output.csv"
    my_file = Path(outfile)
    if my_file.is_file():
        open(outfile, "w").close()
    col_names=['zipcode', 'DateObserved', 'state', 'City', 'AQIType', 'AQIValue']
    my_df  = pd.DataFrame(columns = col_names)
    my_df.to_csv(r'AQI_output.csv', index=None,sep=',', mode='a')
    BaseURL="http://www.airnowapi.org/aq/observation/zipCode/current/"
    ##query tool: https://docs.airnowapi.org/CurrentObservationsByZip/query
    #http://www.airnowapi.org/aq/observation/zipCode
    #/current/?format=text/csv&zipCode=20002&distance=25&
    #API_KEY=DBECFD03-FF12-42D2-9E67-778A5211D1CD    
    URLPost = {'API_KEY': 'DBECFD03-FF12-42D2-9E67-778A5211D1CD',
               'format': 'application/json',
               'zipCode':'00000',
               'distance': '25'
               }  
    input_zip=open('INPUT.txt','r').readlines()
    for zipcode in input_zip:
        URLPost['zipCode']=str(zipcode)
        status=UseUrllib_by_zipcode(BaseURL, URLPost,outfile)
    output1=pd.read_csv(outfile,sep=',')
    print(output1)
# =============================================================================
# The query tool to query by latitude and longitude
# =============================================================================  
    outfile2="AQI_output_lat_long.csv"
    my_file2 = Path(outfile2)
    if my_file2.is_file():
        open(outfile2, "w").close()
    col_names2=['latitude','longitude','DateObserved', 'state', 'City', 'AQIType', 'AQIValue']
    my_df2  = pd.DataFrame(columns = col_names2)
    my_df2.to_csv(r'AQI_output_lat_long.csv', index=None,sep=',', mode='a')
    BaseURL2="http://www.airnowapi.org/aq/observation/latLong/current/"  
    URLPost2 = {'API_KEY': 'DBECFD03-FF12-42D2-9E67-778A5211D1CD',
               'format': 'application/json',
               'zipCode':'00000',
               'latitude':'33.487007',
               'longitude':'-117.143784',
               'distance': '25'
               }  
    input_info=open('INPUT2.txt','r').readlines()
    for info in input_info:
        URLPost2['latitude']=str(info.replace("\n","").split('\t')[1])
        URLPost2['longitude']=str(info.replace("\n","").split('\t')[2])
        status=UseUrllib_by_lat_long(BaseURL2, URLPost2,outfile2)      
    output2=pd.read_csv(outfile2,sep=',')
    print(output2)
if __name__ == '__main__':
    main()


