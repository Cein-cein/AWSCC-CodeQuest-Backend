import requests

print("|=============================================|",
      "\n|=== Day 19: Request and Response Handling ===|",
      "\n|=========== Programmed by: Vince ============|",
      "\n|=============================================|")

print("\nGood day, my fellow space monkey! The following information is all about the latest SpaceX launch.\n")

apiEnd = "https://api.spacexdata.com/v5/launches/latest"
send = requests.get(apiEnd)

if send.status_code == 200:

    data = send.json()
    
    date = data["date_utc"]
    name = data["name"]
    fNum = data["flight_number"]
    rocket = data["rocket"]
    launchpad = data["launchpad"]
    result = data["success"]

    print(f"Date and time: {date} (UTC)")
    print("Name:", name)
    print("Flight Number:", fNum)
    print("Rocket:", rocket)
    print("Launchpad:", launchpad)

    if result == True:
        print("Launch Successful:", result)
    else:
        print("Launch Successful:", result)
    
else:
    print("Request failed. HTTP status code: ", send.status_code)