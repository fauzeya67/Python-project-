from openai import OpenAI
# client = OpenAI()
client = OpenAI(
    api_key="",
)
completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "you are a virtual assistant named jarvis skilled in general tasks like Alexa and google cloud."},
          
        {"role": "user", "content":"what is coding.content"},

    ]
)
print(completion.choice[0].message)
