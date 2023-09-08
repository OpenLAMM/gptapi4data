import openai
import json
from copy import deepcopy

# input your api key
openai.api_key = "sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"

# messages = [{"role":"system", "content": f"""You are an AI visual assistant, and you are seeing a single image. What you see are provided with five sentences, describing the same image you are looking at. Answer all questions as you are seeing the image. Design a conversation between you and a person asking about this photo. The answers should be in a tone that a visual AI assistant is seeing the image and answering the question. Ask diverse questions and give corresponding answers. Include questions asking about the visual content of the image, including the object types, counting the objects, object actions, object locations, relative positions between objects, etc. Only include questions that have definite answers: (1) one can see the content in the image that the question asks about and can answer confidently; (2) one can determine confidently from the image that it is not in the image. Do not ask any question that cannot be answered confidently. Also include complex questions that are relevant to the content in the image, for example, asking about background knowledge of the objects in the image, asking to discuss about events happening in the image, etc. Again, do not ask about uncertain details. Provide detailed answers when answering complex questions. For example, give detailed examples or reasoning steps to make the content more convincing and well-organized. You can include multiple paragraphs if necessary."""}]


messages = [
    {
        "role": "system",
        "content": f"""You are an AI visual assistant, and you are seeing a single image. What you see are provided with five sentences, describing the same image you are looking at. Provide a detailed description of the given image.""",
    }
]


f1 = open("./coco_captions_dump.json", "r")
Captions = json.load(f1)

f2 = open("./coco_instances_dumps.json", "r")
Instances = json.load(f2)

# f3 = open('./LLaVA-Instruct-150K/conversation_58k.json', 'r')
f3 = open("./LLaVA-Instruct-150K/detail_23k.json", "r")
# f3 = open('./LLaVA-Instruct-150K/complex_reasoning_77k.json', 'r')
Conversations = json.load(f3)

fewshot_samples = []
seed_samples = Conversations[:5]

# build examples for in-context learning
for item in seed_samples:
    image_id = str(int(item["id"]))
    conversations = str(item["conversations"])

    if image_id not in Instances.keys() or image_id not in Captions.keys():
        continue
    else:
        caption = " ".join(Captions[image_id])
        instances = Instances[image_id]
        boxes = ", ".join([str(ins).strip("{}") for ins in instances]).replace("'", "")
        context = "Captions: " + caption + " Boxes: " + boxes
        fewshot_samples.append({"context": context, "response": conversations})

for sample in fewshot_samples:
    messages.append({"role": "user", "content": sample["context"]})
    messages.append({"role": "assistant", "content": sample["response"]})

# query ChatGPT API
query_samples = Conversations[30:40]
for item in query_samples:
    image_id = str(int(item["id"]))
    conversations = str(item["conversations"])

    if image_id not in Instances.keys() or image_id not in Captions.keys():
        continue
    else:
        # load caption & bboxes
        caption = " ".join(Captions[image_id])
        instances = Instances[image_id]
        boxes = ", ".join([str(ins).strip("{}") for ins in instances]).replace("'", "")
        query = "Captions: " + caption + " Boxes: " + boxes
        message_copy = deepcopy(messages)
        # build input messages
        message_copy.append({"role": "user", "content": query})
        print(len(str(message_copy)))
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo", messages=message_copy
        )
        print("query: ", query)
        print("our gpt gen:", response)
        print("vs")
        print("llava:", conversations)
        print("\n")
