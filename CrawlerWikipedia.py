import csv
import os        
import requests
import bs4
from bs4 import BeautifulSoup

"""Get Prominent Cajun Fiddlers"""
def result_page_spider():
    url = 'https://en.wikipedia.org/wiki/Cajun_fiddle'
    source_code = requests.get(url)
    source_text = source_code.text
    soup = BeautifulSoup(source_text,"lxml")
    header = soup.find("span", {'id':'Prominent_proponents_of_the_style'})
    unordered = header.parent.find_next_sibling("ul") 
    link_list = []      
    for link in unordered.find_all('a'): 
        fiddler_name = link.string
        fiddler_link = "https://en.wikipedia.org/wiki/Cajun_fiddle" + link.get('href')
        link_list.append(fiddler_link)
        #print(fiddler_name, fiddler_link)
    return link_list
        
        
        

result_page_spider()

"""Return Table of information"""
def individual_fiddler_data(fiddler_list):
    header_list=[]
    for link in fiddler_list:
        source_code = requests.get(link)
        source_text = source_code.text
        soup = BeautifulSoup(source_text,'lxml')
        header = soup.find('h1')
        text = header.text
        header_list.append(text)
        header_list=list(header_list)
        #print(text)
    #print(header_list)
    return header_list  
    

individual_fiddler_data(result_page_spider())

# Write to csv
def write_csv(list_of_items):
    with open('cajun_fiddlers.csv', mode='w') as fiddle_file:
        fiddle_writer = csv.writer(fiddle_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        fiddle_writer.writerows([row] for row in list_of_items)
write_csv(individual_fiddler_data(result_page_spider()))    
   
# Check to make sure that csv was written correctly
import pandas as pd
data = pd.read_csv('cajun_fiddlers.csv')
print(data.head())


# Prevent duplicates
from more_itertools import unique_everseen
with open('cajun_fiddlers','r') as fiddlers, open('cajun_fiddlers2.csv','w') as current_file:
    current_file.writelines(unique_everseen(fiddlers))