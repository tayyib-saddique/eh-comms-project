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
  return response.choices[0].message.content


response = get_chat_completion("Tell me information about local policing in the North East of England")
print(response)

def news_catcher(newscatcher=newscatcher):
  try:
      get_response = newscatcher.search.get(
        q="Policing",
        search_in="title_content",
        countries='GB'
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

api_response = news_catcher()
print(api_response)

fine_tuned_model = client.fine_tuning.jobs.create(
    model="gpt-3.5-turbo-0125",
    training_file=api_response,
)


