import requests

print("|=====================================================|",
      "\n|=== Day 17: HTTP Methods, Status Codes, Endpoints ===|",
      "\n|=============== Programmed by: Vince ================|",
      "\n|=====================================================|")

test = requests.get('https://jsonplaceholder.typicode.com/')

if test.status_code == 200:
    print("\nRequest successful.\n")
else:
    print("\nRequest failed.\n")
