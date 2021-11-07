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
  
    citation = parser_data.find_all('a', href="/wiki/Wikipedia:Citation_needed")
  
    return len(citation)

"""
 create a function called a get_citations_needed_report that take a link and 
 retuen a string .

"""

def get_citations_needed_report(link_contain):

    page_data = requests.get(link_contain)

    parser_data = BeautifulSoup(page_data.content, 'html.parser')

    parse_all_data = parser_data.find_all('sup', class_= 'noprint Inline-Template Template-Fact')

    sentencess = ""

    for citation in parse_all_data:

        sentencess += f'Citation needed for "{citation.parent.text}"'

    return sentencess




if __name__ =='__main__':

    print(get_citations_needed_count(link_contain))

    print(get_citations_needed_report(link_contain))

# quit()



