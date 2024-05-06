import config
import requests
import json
from types import SimpleNamespace
from bs4 import BeautifulSoup
import openai_api

language_code = 'en'
number_of_results = 1
headers = {
'Authorization': config.token,
'User-Agent': config.app
}
base_url = 'https://api.wikimedia.org/core/v1/wikipedia/'
endpoint = '/search/page'

def search(country, categories):
    url = base_url + language_code + endpoint
    search_query = country
    parameters = {'q': search_query, 'limit': number_of_results}

    # Check if country exists
    response = requests.get(url, headers=headers, params=parameters)
    if response.status_code == 200:

        # We're storing information about each category here
        results = {}

        # Goes through each category and finds out related info for the country
        for category in categories:
            search_query = f'{country} {category}'
            response = requests.get(url, headers=headers, params=parameters)
            if response.status_code == 200:
                
                # Get the page object
                results_object = json.loads(response.text, object_hook=lambda d: SimpleNamespace(**d))
                url = base_url + language_code + '/page/' + results_object.pages[0].key + '/bare'
                response = requests.get(url, headers=headers)
        
                # Get the html contents
                results_object = json.loads(response.text, object_hook=lambda d: SimpleNamespace(**d))
                page_html = requests.get(results_object.html_url, headers = {'Accept-Encoding': 'identity'})
                page_text = BeautifulSoup(page_html.text, "html.parser").get_text()

                # Interpret the results and add it to the 
                conclusion = openai_api.interpret(page_text)
                results[category] = conclusion
                
            else:
                results[category] = "Unable to determine"
        return results
    else:
        return None