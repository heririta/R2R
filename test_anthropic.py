import os
from litellm import completion

# set env - [OPTIONAL] replace with your anthropic key
os.environ["ANTHROPIC_API_KEY"] = ""

messages = [{"role": "user", "content": "siapa presiden indonesia?"}]
response = completion(model="claude-3-opus-20240229", messages=messages)
print(response)
