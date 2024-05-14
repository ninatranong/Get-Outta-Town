import config
import pathlib
import textwrap
import time

import google.generativeai as genai

from IPython.display import display
from IPython.display import Markdown


def to_markdown(text):
  text = text.replace('•', '  *')
  return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))

def safe_request(country, category, max_retries=5, delay=60):
    for _ in range(max_retries):
        try:
            response = model.generate_content(f'Compose a 2-3 sentence explanation for the following: Status of #{category} in #{country}')
            return response.text
        except:
            print("Retrying after 60 seconds.")
            time.sleep(delay)  # Wait before retrying
    return None

# Or use `os.getenv('GOOGLE_API_KEY')` to fetch an environment variable.
GOOGLE_API_KEY=config.GOOGLE_API_KEY

genai.configure(api_key=GOOGLE_API_KEY)
model = genai.GenerativeModel('gemini-pro')

def interpret(countries, categories):
    results = {}
    for country in countries:
        results[country] = {}
        for category in categories:
            results[country][category] = safe_request(country, category)
            print(results[country][category])
    print('Results created')
    return results