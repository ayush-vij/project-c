#all the imports
import openpyxl as op
import numpy as np
import io
import requests
import pandas as pnds
import calendar as cldr

#linking states
link_states = "https://raw.githubusercontent.com/nytimes/covid-19-data/master/us-states.csv"
#linking US
link_us = "https://raw.githubusercontent.com/nytimes/covid-19-data/master/us.csv"

#reading the data
read_states = requests.get(link_states).content
read_us = requests.get(link_us).content

#creating Excel files
address_states = pnds.read_csv(io.StringIO(read_states.decode('utf-8')))
address_us = pnds.read_csv(io.StringIO(read_us.decode('utf-8')))
