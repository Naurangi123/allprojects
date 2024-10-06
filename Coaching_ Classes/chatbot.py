
import openai

from openai import *

openai.api_key = "sk-6mAFM4nFbOfihnsx-AgLQ3UeELxVYLvzwTE3kHQGfBT3BlbkFJ-ajrtuS1ylq3iBB2XJJ0J1dUjoNBZoicAsrTvB7fEA"  # Set your API key here
messages = [{'role': 'system', 'content': "For assistant"}]
while True:
    query = input("User: ")
    messages.append({"role": "user", "content": query})
    chat = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages
    )
    reply = chat['choices'][0]['message']['content']
    print(f"ChatGPT: {reply}")
    messages.append({"role": "asst_9M5QPuRdMP9ofSgiVrNHTwrL", "content": reply})
