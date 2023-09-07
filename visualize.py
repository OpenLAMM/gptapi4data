import json


f1 = open('./LLaVA-Instruct-150K/conversation_58k.json', 'r')
f2 = open('./LLaVA-Instruct-150K/detail_23k.json', 'r')
f3 = open('./LLaVA-Instruct-150K/complex_reasoning_77k.json', 'r')
Conversations = json.load(f1)
Details = json.load(f2)
Complexs = json.load(f3)

print(len(Conversations))
print(len(Details))
print(len(Complexs))

dict1 = {}
dict2 = {}
dict3 = {}

for conv in Conversations:
    id = conv['id']
    dict1[id] = conv

for detail in Details:
    id = detail['id']
    dict2[id] = detail

for comp in Complexs:
    id = comp['id']
    dict3[id] = comp



id1 = set(dict1.keys())
id2 = set(dict2.keys())
id3 = set(dict3.keys())

print(len(id1))
print(len(id2))
print(len(id3))

ids = id1.intersection(id2, id3)
print(len(ids))
