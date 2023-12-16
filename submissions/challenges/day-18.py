import requests
print("|=====================================================|",
      "\n|=== Day 18: Query String Parameters, Headers, Body===|",
      "\n|=============== Programmed by: Vince ================|",
      "\n|=====================================================|")

#Set Custom Headers:
api_end = "https://jsonplaceholder.typicode.com/posts"
req = requests.get(api_end)
header = {"User-Agent": "MyApp/1.0"}

#Send the GET Request:
sendReq = requests.get(api_end, headers=header)

#Inspect the Response:
print("HTTP status code: ", req.status_code)
for key, value in sendReq.headers.items():
    print(f"Response headers: {key}: {value}")
print("\nResponse content: ", sendReq.text)

print("=====================================================================================================================================")

#Prepare Data for POST Request:
postDict = {
    "title": "lorem ipsum dolor sit amet",
    "body": "this does not mean anything"
}

#Send a POST Request:
sendPost = requests.post(api_end, json=postDict)

#Inspect the POST Response:
print("HTTP status code: ", sendPost.status_code)
print("\nResponse content: ", sendPost.text)
