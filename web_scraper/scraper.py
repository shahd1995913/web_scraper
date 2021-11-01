import requests
from bs4 import BeautifulSoup

link ='https://en.wikipedia.org'
link_contain = f'{link}//wiki/History_of_Mexico'


""""
function called a get_citations_needed_count that retuen a number of citation that 
contain  title Wikipedia:Citation needed  and the number is 5 

"""
def get_citations_needed_count(link_contain):

    page_data = requests.get(link_contain)

   
    parser_data = BeautifulSoup(page_data.content, 'html.parser')

    citation = parser_data.find_all('a', { "title" : "Wikipedia:Citation needed"})

    return( len(citation))

get_citations_needed_count(link_contain)

"""
 create a function called a get_citations_needed_report that take a link and 
 retuen a string .

"""
def get_citations_needed_report(link_contain):

    sentencess=[]

    page_data = requests.get(link_contain)

   
    parser_data = BeautifulSoup(page_data.content, 'html.parser')


    parse_all_data = parser_data.find_all('p')

    

    for obj in parse_all_data:

        title = obj.find('a', { "title" : "Wikipedia:Citation needed"})

        if title:

            sentencess.append(obj.text)

    return(sentencess)

get_citations_needed_report(link_contain)


quit()







