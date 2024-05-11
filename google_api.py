import config
import pathlib
import textwrap

import google.generativeai as genai

from IPython.display import display
from IPython.display import Markdown


def to_markdown(text):
  text = text.replace('•', '  *')
  return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))

# Or use `os.getenv('GOOGLE_API_KEY')` to fetch an environment variable.
GOOGLE_API_KEY=config.GOOGLE_API_KEY

genai.configure(api_key=GOOGLE_API_KEY)
model = genai.GenerativeModel('gemini-pro')

def interpret(countries, categories):
    results = {}
    for country in countries:
        results[country] = {}
        for category in categories:
            response = model.generate_content(f'Compose a 2-3 sentence explanation for the following text: Status of #{category} in #{country}')
            results[country][category] = response.text
    print('Results created')
    return results

