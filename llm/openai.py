import os
from openai import OpenAI
from dotenv import load_dotenv
    
load_dotenv()

client = OpenAI(
    api_key = os.environ.get("OPENAI_API_KEY"),
)

def get_chat_completion(prompt, model="gpt-3.5-turbo"):
  
   # Creating a message as required by the API
   messages = [{"role": "user", "content": prompt}]
  
   # Calling the ChatCompletion API
   response = client.ChatCompletion.create(
       model=model,
       messages=messages,
       temperature=0,
   )

   # Returning the extracted response
   return response.choices[0].message["content"]

response = get_chat_completion("Translate into Spanish: As a beginner data scientist, I'm excited to learn about OpenAI API!")

print(response)


