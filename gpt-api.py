import openai

openai.api_key="sk-xxxxxxxxxxxxxxx"

response = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": "what is the chevrolet express cargo van 2007?"},])
print(response)

