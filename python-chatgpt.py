import requests

api_endpoint="https://api.openai.com/v1/completions"


headers={
    "Content-Type": "application/json",
    "Authorization": "Bearer " + api_key
}

request_data={
    "model":"text-davinci-003",
    "prompt":"Write python script for hello world",
    "max_tokens":100,
    "temperature":0.5
}

response=requests.post(api_endpoint,headers=headers,json={})

if response.status_code==200:
    print(response.json())
else:
    print(f"Request failed with status code:{str(response.status_code)}")    
