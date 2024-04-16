import sys
import os
current = os.path.dirname(os.path.realpath(__file__))
print(current)
parent = os.path.dirname(current)
parent_ = os.path.dirname(parent)
parent__ = os.path.dirname(parent_)
sys.path.append(parent__)

from openai import OpenAI
from dotenv import load_dotenv
from llm.summarise import get_summary

load_dotenv()

client = OpenAI(
    api_key = "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",
)

def get_chat_completion(prompt, model="gpt-4-turbo-2024-04-09"):
  response = client.chat.completions.create(
      model=model,
      messages=[
        {"role": "user", "content": prompt},
      ],
      temperature = 0.7,
    )
  print(response.choices[0].message.content)
  return response.choices[0].message.content


def generate_questions(prompt, subject, region, source, data):
  response = get_summary(prompt, subject, region, source, data)
  return get_chat_completion(f"You are a news reporter at a press conference.  Using this summarised brief {response}, generate open-ended questions aimed at a Minister.")

