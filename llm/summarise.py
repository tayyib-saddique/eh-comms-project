from openai import OpenAI
from dotenv import load_dotenv
from pprint import pprint
import datetime as dt
from newscatcherapi_client import Newscatcher, ApiException

load_dotenv()

client = OpenAI(
    api_key = "",
)

newscatcher = Newscatcher(
    api_key= "", 
)

def get_chat_completion(prompt, subject, region, source, data, model="gpt-4-turbo-2024-04-09"):
  response = client.chat.completions.create(
      model=model,
      messages=[
        {"role": "user", "content": prompt},
        {"role": "system", "content": f"You are a Communications Expert. Using this data - {data}, summarise information from the news about the topic {subject} in {region} using the following this source {source} ensuring the prompt is answered. Be as specific as possible and make sure information is relevant to {region}."}
      ],
      temperature = 0.7,
    )
  return response.choices[0].message.content

def news_catcher(newscatcher=newscatcher):
  today = dt.date.today()
  week_ago = today - dt.timedelta(days=7)
  try:
    get_response = newscatcher.search.get(
            q="Police OR Crime",
            search_in="title_content",
            countries="GB",
            theme='Crime',
            from_= str(week_ago),
            to_ = str(today),
        )
    data = get_response.articles
    return data
  except ApiException as e:
      print("Exception when calling AuthorsApi.get: %s\n" % e)
      pprint(e.body)
      if e.status == 422:
          pprint(e.body["detail"])
      pprint(e.headers)
      pprint(e.status)
      pprint(e.reason)
      pprint(e.round_trip_time)

data_ = news_catcher()
description = []

for i in range(0, 100):
   description.append(data_[i]['content'])

def get_summary(prompt, subject, region, source, data):
  response = get_chat_completion(prompt, subject, region, source, data)
  return response
