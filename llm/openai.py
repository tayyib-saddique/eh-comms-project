import os
from openai import OpenAI
from dotenv import load_dotenv
    
load_dotenv()

client = OpenAI(
    api_key = os.environ.get("OPENAI_API_KEY"),
)

def get_chat_completion(prompt, model="gpt-3.5-turbo"):
  
  response = client.chat.completions.create(
      model=model,
      messages=[
        {"role": "system", "content": "You are a helpful assistant designed to summarise text."},
        {"role": "user", "content": prompt}
      ]
      temperature = 0,
    )
  return response.choices[0].message["content"]

response = get_chat_completion("Tell me more information about local policing in the North East of England")
print(response)


