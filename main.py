#all the imports
import openpyxl as op
import numpy as np
import io
import requests
import pandas as pnds
import calendar as cldr
import csv
import datetime

#weekdays
weekDays = ("Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday")
#linking states
link_states = "https://raw.githubusercontent.com/nytimes/covid-19-data/master/us-states.csv"
#linking US
link_us = "https://raw.githubusercontent.com/nytimes/covid-19-data/master/us.csv"

#reading the data
read_states = requests.get(link_states).content
read_us = requests.get(link_us).content

#saving csv
def getCsv(url, name):
    req = requests.get(url)
    url_content = req.content
    csv_file = open("csv_files/"+name+".csv", "wb")
    csv_file.write(url_content)
    csv_file.close()

#to create csv
getCsv(link_states, "US_States")
getCsv(link_us, "US")

#adding new column
def addDay(filename):
    with open("csv_files/"+filename+".csv",'r', encoding='utf-8') as csvinput:
        with open("csv_files/"+filename+".csv", 'a', encoding='utf-8') as csvoutput:
            writer = csv.writer(csvoutput, lineterminator='\n')
            reader = csv.reader(csvinput)
            all= []
            row = next(reader)
            row.append("Weekday")
            # all.append(row)
            writer.writerow(row)
            # for row in reader:
            #     date = datetime.datetime.strptime(row[0],"%Y-%m-%d")
            #     day = date.weekday()
            #     row.append(weekDays[day])
            #     all.append(row)
            # # writer.writerows(all)
            

addDay("US_States")
#creating Excel files
address_states = pnds.read_csv(io.StringIO(read_states.decode('utf-8')))
address_us = pnds.read_csv(io.StringIO(read_us.decode('utf-8')))
