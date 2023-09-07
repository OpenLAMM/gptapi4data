import openai

openai.api_key = "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"

response1 = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {
            "role": "user",
            "content": "Given text: a city in southwestern Switzerland at the western end of Lake Geneva; it is the headquarters of various international organizations. Please ask ten question and give corresponding answers"
        },
    ]
)

response2 = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[
                                         {"role": "user", "content": "a city in southwestern Switzerland at the western end of Lake Geneva; it is the headquarters of various international organizations. Please ask ten question and give corresponding answers"},])

response3 = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[
                                         {"role": "user", "content": "Please ask ten question and give corresponding answers based on a city in southwestern Switzerland at the western end of Lake Geneva; it is the headquarters of various international organizations. "},])

response4 = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[
                                         {"role": "user", "content": "Given text: a city in southwestern Switzerland at the western end of Lake Geneva; it is the headquarters of various international organizations. Please generate instruction tunning data."},])

print("response1:", response1)
print("response2:", response2)
print("response3:", response3)
print("response4:", response4)
