#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 13 23:26:01 2018

@author: Chelsea Wang

API keys: 6c8af59ba394197923d2779ae842de75
"""

# =============================================================================
# Part 4:
# 1.     Write Python code to read data from the request URL into a json file
# and into a second text file in which the data is written using the following text format:
# City|Cnt
# Temp|Temp Min|Temp Max|Humidity
#  
# Example:
# Munchen|36
# 287.67|281.556|286.67|75
# 
# =============================================================================
import urllib
from urllib.request import urlopen
import json
from pathlib import Path
import dateutil.parser
#%%
def main():
    #Will need to use lat and long query, 
    # by specifying a cnt 
    # the weather conditions returned will be printed out 
    outfile="weatherdata.txt"
    my_file = Path(outfile)
    if my_file.is_file():
        open(outfile, "w").close()
    outfile1="weatherdataraw.json"
    my_file = Path(outfile1)
    if my_file.is_file():
        open(outfile1, "w").close()
    BaseURL="http://api.openweathermap.org/data/2.5/find"
    URLPost = {'lat':'55.5',
               'lon':'37.5',
               'cnt':'10',
               'appid': '6c8af59ba394197923d2779ae842de75'}
    input_info=open('city.txt','r').readlines()
    file_out=open(outfile,"a")
    file_out1=open(outfile1,"a")
    for info in input_info:
        URLPost['lat']=str(info.replace("\n","").split('\t')[0])
        URLPost['lon']=str(info.replace("\n","").split('\t')[1])
        URLPost['cnt']=str(info.replace("\n","").split('\t')[2])
        URL=BaseURL + "?"+ urllib.parse.urlencode(URLPost)
        WebURL=urlopen(URL)
        data=WebURL.read()
        encoding = WebURL.info().get_content_charset('utf-8')
        jsontxt = json.loads(data.decode(encoding))
        citylist=jsontxt['list']
        cnt=len(citylist)
        json.dump(jsontxt, file_out1)
        for templist in citylist:
            city=templist['name']
            temp=templist['main']['temp']
            temp_min=templist['main']['temp_min']
            temp_max=templist['main']['temp_max']
            humidity=templist['main']['humidity']
            file_out.write(city+"|"+str(cnt)+"\n")
            file_out.write(str(temp)+"|"+str(temp_min)+"|"+str(temp_max)+"|"+str(humidity)+"\n")
    file_out.close()
    
if __name__ == '__main__':
    main()    
