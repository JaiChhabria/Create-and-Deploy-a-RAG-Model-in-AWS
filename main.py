import os
import json
import sys
import boto3
print("imported sucessfully")


prompt = """"
You are a smart assistant and please let me know what is machine learning in smartest way.
"""

bedrock = boto3.client(service_name="bedrock-runtime")

payload = {
    
    
}

body = json.dumps(payload)

model_id = "meta.llama2-70b0-chat-v1"

response = bedrock.invoke_model(
    body=body,
    match_id=model_id,
    accept="application/json",
    content_type="application/json",
)


response_body=json.loads(response.get("body").read())
response_body['generation']
