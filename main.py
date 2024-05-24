import os
import json
import sys
import boto3
print("imported sucessfully")


prompt = """"
You are a smart assistant and please let me know what is machine learning in a smartest way.
"""

bedrock = boto3.client(service_name="bedrock-runtime")

payload = {
    "prompt": "[INST]"+prompt+"[/INST]",
    "temperature": 0.3,
    "top_p": 0.9
}

body = json.dumps(payload)

model_id = "meta.llama2-70b-chat-v1"

response = bedrock.invoke_model(
    body=body,
    modelId=model_id,
    accept="application/json",
    contentType="application/json",
)


response_body=json.loads(response.get("body").read())
response_text=response_body['generation']

print(response_text)
