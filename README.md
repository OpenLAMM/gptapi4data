# GPT API Example

This is code for generate instruction data via GPT-API following LLaVA style.

## How to use

Run following command to run GPT API and for coco samples. In-context examples are from [LLaVA dataset](https://huggingface.co/datasets/liuhaotian/LLaVA-Instruct-150K/tree/main).
```python
python llava-instruction.py
```

## Access GPT

Normally, only api key needed.
```python
import openai
openai.api_key = "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"
```
Change version of ChatGPT you want to use.
```python
response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo", # or "gpt-4"
    messages=message_copy
)
```
Sometimes, organization ID may also be required.
```python
openai.organization = "org-xxxxxxx"
```
