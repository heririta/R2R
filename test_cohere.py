import os
from litellm import embedding
os.environ["COHERE_API_KEY"] = "edu0YGrVajstvkGOoKvPsG6LV1wcHnBvYB1jLGMX"

# cohere call
response = embedding(
    model="embed-english-v3.0",
    input=["good morning from litellm", "this is another item"],
    input_type="search_document" # optional param for v3 llms
)
print(response)
