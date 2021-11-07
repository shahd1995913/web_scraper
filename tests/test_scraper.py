from web_scraper.scraper import (get_citations_needed_count , get_citations_needed_report)



def test_get_citations_needed_count():

    link ='https://en.wikipedia.org'

    link_contain = f'{link}//wiki/History_of_Mexico'


    excepted = 5

    actual = get_citations_needed_count(link_contain)


    assert excepted == actual
    
    
def test_get_citations_needed_report():

    link ='https://en.wikipedia.org'

    link_contain = f'{link}//wiki/History_of_Mexico'


    excepted = get_citations_needed_report(link_contain)
    
    assert 'The Spanish had no intention to turn over Tenochtitlan to the Tlaxcalteca.' in excepted

