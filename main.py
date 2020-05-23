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
        reader = csv.reader(csvinput)         
        all = []
        head = next(reader)
        head.append('weekday')
        all.append(head)
        for row in reader:
                date = datetime.datetime.strptime(row[0],"%Y-%m-%d")
                day = date.weekday()
                row.append(weekDays[day])
                all.append(row)
        with open("csv_files/"+filename+".csv", 'w', encoding='utf-8') as csvoutput:
            writer = csv.writer(csvoutput, lineterminator='\n')    
            writer.writerows(all)

addDay("US_States")
addDay("US")

#creating Excel files
def createExcel(filename):
    dataFrame = pnds.read_csv("csv_files/"+filename+".csv", encoding='utf-8')
    dataFrame.to_excel("excel_files/"+filename+".xlsx", sheet_name=filename, index=False)

createExcel("US_States")
createExcel("US")