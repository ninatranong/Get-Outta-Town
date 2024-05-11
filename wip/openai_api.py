from openai import OpenAI
import config

client = OpenAI(api_key=config.OPENAI_API_KEY)

def interpret(content):
    completion = client.chat.completions.create(
      model="gpt-3.5-turbo",
      messages=[
        {"role": "system", "content": f'You are a person thinking about moving to another country. You see the following information: {content}'},
        {"role": "user", "content": "Compose a 2-3 sentence explanation for the information you saw."}
      ]
    )
    
    return completion.choices[0].message