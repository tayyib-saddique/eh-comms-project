import os
from openai import OpenAI
from dotenv import load_dotenv
from pprint import pprint
from newscatcherapi_client import Newscatcher, ApiException

load_dotenv()

client = OpenAI(
    api_key = os.environ.get("OPENAI_API_KEY"),
)

newscatcher = Newscatcher(
      api_key= os.environ.get("NEWSCATCHER_API_KEY"), 
  )

def get_chat_completion(prompt, model="gpt-3.5-turbo"):
  response = client.chat.completions.create(
      model=model,
      messages=[
        {"role": "user", "content": prompt}
      ],
      temperature = 0.7
    )
  return response.choices[0].message["content"]

def news_catcher(newscatcher):
  try:
      # [Get] Search By Author Request
      get_response = newscatcher.search.get(
          q="raises AND series A",
          search_in="title_content"
      )
      return get_response
  except ApiException as e:
      print("Exception when calling AuthorsApi.get: %s\n" % e)
      pprint(e.body)
      if e.status == 422:
          pprint(e.body["detail"])
      pprint(e.headers)
      pprint(e.status)
      pprint(e.reason)
      pprint(e.round_trip_time)


# user_input = input('Enter input')
# response = get_chat_completion(user_input)

response = get_chat_completion("Tell me more information about local policing in the North East of England")
print(response)

api_response = news_catcher()
print(api_response)

