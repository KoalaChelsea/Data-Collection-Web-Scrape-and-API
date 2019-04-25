###########################################################
##
##     Week 4 Assignment: Python
##     Part Two
##
##     Course: Advanced Programming Topics 
##     Instructor: Dr. A. Gates
##     Author: Yingjie(Chelsea) Wang
##     Date: 07/29/2018
##
###########################################################

from datetime import date
import pandas as pd

def main():
    
    #add title to the txt file
    title='Zipcode\tDateIssue\tDateForecast\tReportingArea\tStateCode\tLatitude\tLongitude\tParameterName\tAQI\tCategory\tActionDay\tDiscussion'

    with open('OUTFILE.txt', 'w') as f:
        f.write(title)
        f.write('\n')
        f.close()

    #list to append the zipcode
    ls=[]
    
    #make sure we have 4 chance to enter the valid zipcode
    while len(ls) < 4:
        
        #get zipcode
        print("Pleas enter zip codes to get data, or enter Q to quit.")
        zipcode = input()
        
        #test duplicated zipcode
        if zipcode in ls:
            print("Duplicated Zipcode!")
            continue
        else: 
            ls.append(zipcode)
        
        #quit
        if 'Q' in zipcode or 'q' in zipcode:
            print('Bye!')
            break

        
        #URL
        BaseURL="http://www.airnowapi.org/aq/forecast/zipCode/"

        URLPost = {'API_KEY': 'FD898FF4-1C31-4B07-BC1C-F48423406133',
                        'zipCode': zipcode, 
                        'date': str(date.today()),
                        'distance': '25',
                        'format': 'application/json'}
        UseRequest(BaseURL, URLPost, zipcode)
        UseUrllib(BaseURL, URLPost, zipcode)

    df = pd.read_csv("OUTFILE.txt",delimiter="\t")
    #print(df)
    #print(df.head())
    #print(df.columns)
    #print(studentdf.shape)
    #print(studentdf.info())
    
    ##  zipcode, the date, the state, the city, and the AQI results
    newdf = df.filter(['Zipcode', 'DateIssue', 'DateForecast', 'StateCode', 'ReportingArea', 'AQI']) 
    #print(newdf.head())
    #print(newdf.info())
    
    print('\n',file=open("OUTFILE.txt", "a"))
    print(newdf, file=open("OUTFILE.txt", "a"))
    
    
def UseRequest(BaseURL, URLPost, zipcode):
    #Uses request library
    import requests
    import json
    
    response=requests.get(BaseURL, URLPost)
    jsontxt = response.json()
    print(jsontxt, "\n")
    
    

    for list in jsontxt:
        DateIssue = list['DateIssue']
        DateForecast=list['DateForecast']
        ReportingArea=list['ReportingArea']
        StateCode=list['StateCode']
        Latitude=list['Latitude']
        Longitude=list['Longitude']
        ParameterName=list['ParameterName']
        AQI=list['AQI']
        Category=list['Category']
        #CategoryName=list['Category']
        ActionDay=list['ActionDay']
        Discussion=list['Discussion']

        #append necessary info to the txt file
        djson = zipcode+'\t'+str(DateIssue)+'\t'+str(DateForecast)+'\t'+str(ReportingArea)+'\t'+str(StateCode)+'\t'+str(Latitude)+'\t'+str(Longitude)+'\t'+str(ParameterName)+'\t'+str(AQI)+'\t'+str(Category)+'\t'+str(ActionDay)+'\t'+str(Discussion)
        
        with open('OUTFILE.txt', "a+") as f:
            f.write(djson)
            f.write('\n')
            f.close()
            
        print("Zipcode", zipcode,"DateIssue ", DateIssue, " DateForecast ", DateForecast, 
              " ReportingArea ", ReportingArea, " StateCode ", StateCode,
              " Latitude ", Latitude, " Longitude ",Longitude,
              " ParameterName ",ParameterName, " AQI ",AQI," Category ", Category, " ActionDay ", ActionDay, " Discussion ", Discussion,
              "\n")
    
    
                 


def UseUrllib(BaseURL, URLPost, zipcode):
    #Uses urllib library
    import urllib
    from urllib.request import urlopen
    import json
    
    URL = BaseURL + "?"+ urllib.parse.urlencode(URLPost)
    WebURL = urlopen(URL)
    data = WebURL.read()
    encoding = WebURL.info().get_content_charset('utf-8')
    jsontxt = json.loads(data.decode(encoding))
    
    print(jsontxt, "\n")
    

    for list in jsontxt:
        DateIssue = list['DateIssue']
        DateForecast=list['DateForecast']
        ReportingArea=list['ReportingArea']
        StateCode=list['StateCode']
        Latitude=list['Latitude']
        Longitude=list['Longitude']
        ParameterName=list['ParameterName']
        AQI=list['AQI']
        Category=list['Category']
        #CategoryName=list['CategoryName']
        ActionDay=list['ActionDay']
        Discussion=list['Discussion']
        
        #append necessary info to the txt file
        djson = zipcode+'\t'+str(DateIssue)+'\t'+str(DateForecast)+'\t'+str(ReportingArea)+'\t'+str(StateCode)+'\t'+str(Latitude)+'\t'+str(Longitude)+'\t'+str(ParameterName)+'\t'+str(AQI)+'\t'+str(Category)+'\t'+str(ActionDay)+'\t'+str(Discussion)
        with open('OUTFILE.txt', "a+") as f:
            f.write(djson)
            f.write('\n')
            f.close()
            
        print("Zipcode", zipcode,"DateIssue ", DateIssue, " DateForecast ", DateForecast, 
              " ReportingArea ", ReportingArea, " StateCode ", StateCode,
              " Latitude ", Latitude, " Longitude ",Longitude,
              " ParameterName ",ParameterName, " AQI ",AQI," Category ", Category, " ActionDay ", ActionDay, " Discussion ", Discussion,
              "\n") 
    
main() 
