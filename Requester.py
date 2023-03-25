import requests

url = "$IP"
search_string = "HTB{"
requests_per_check = 1000

count = 0
found = False

while not found:
    response = requests.get(url)
    if search_string in response.text:
        found = True
        print("Found search string in response!")
        print(response.text)
    count += 1
    if count % requests_per_check == 0:
        print(f"Checked {count} requests, still no match...")
    else:
        print(f"Checked {count} requests...", end="\r")