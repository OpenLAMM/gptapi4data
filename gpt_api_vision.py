import os
import json
import openai
import base64
import argparse
import requests


MODELS = ['gpt-4-1106-preview', 'gpt-4-1106-vision-preview', 'gpt-4', 'gpt-4-32k', 'gpt-3.5-turbo-1106', 'gpt-3.5-turbo-instruct', 'gpt-3.5-turbo']


def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')


def complete_vision_chat(client, args):
    if os.path.isfile(args.image_path):
        base64_image = encode_image(args.image_path)
        image_url = f"data:image/jpeg;base64,{base64_image}"
    else:
        image_url = args.image_path
    response = client.chat.completions.create(
        model="gpt-4-vision-preview",
        messages=[
            {
                "role": "user",
                "content": [
                    {
                    "type": "text",
                    "text": args.text
                    },
                    {
                    "type": "image_url",
                    "image_url": {
                        "url": image_url
                    }
                    }
                ],
            }
        ],
        # max_tokens=300,
    )
    return response.choices[0]

def complete_chat(client, args):
    response = client.chat.completions.create(
        model="gpt-4-preview",
        messages=[
            {
                "role": "user",
                "content": [
                    {
                    "type": "text",
                    "text": args.text
                    },
                ],
            }
        ],
        # max_tokens=300,
    )
    return response.choices[0]


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--model', type=str, default='gpt-4-1106-vision-preview')
    parser.add_argument('--text', type=str, default='')
    parser.add_argument('--image_path', type=str, default=None)
    args = parser.parse_args()
    return args


def main():
    openai.api_key = "sk-xxxxxxxxxxxxxxxxxxxxxxxxx"
    args = parse_args()
    client = open.OpenAI()
    # choose model
    # model_name = 'gpt-4-vision-preview'
    assert args.model_name in MODELS, print(f'{args.model_name} not found!')
    if args.image_path:
        response = complete_vision_chat(client, args)
    else:
        response = complete_chat(client, args)

    content = {
            'Instruction': args.text,
            'Image': args.image_path,
            'OpenAI Assistant': response
        }
    print(json.dumps(content, indent=4), flush=True)