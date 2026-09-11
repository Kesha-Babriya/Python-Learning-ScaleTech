import requests

# Send a GET request.

response = requests.get("https://example.com")

# Print the status code.
if response.status_code == 200:
    print("Request succedded")
else:
    print("Request failed")

# Print the response URL.
print("Url: ",response.url)

# Print the Content-Type from the response headers.
print("Content-type: ",response.headers.get("content-Type"))

# Print the first 300 characters of response.text.
print("First 300 char: ",response.text[:300])


print("------------------another url-----------------")
try:
    params = {
        "name":"kesha",
        'age':20
    }
    response = requests.get("https://httpbin.org/get",params=params,timeout=10)

    response.raise_for_status()

    print("Status code : ",response.status_code)
    print("Response Url: ",response.url)
    print("Response text: ",response.text)

except requests.RequestException as error:
    print("Request failed ",error)
