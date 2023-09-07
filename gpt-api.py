import openai

openai.api_key="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"

response = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": "what is the chevrolet express cargo van 2007?"},])
print(response)

