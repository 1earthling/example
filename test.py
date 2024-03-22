import requests

# Your previously defined variables
cert_file_path = 'path/to/your/cert_file.pem'
cert_password = 'your_password_here'
ca_cert_file_path = 'path/to/your/ca_cert_file.pem'
url = 'https://your.request.url.here/'

# Adding custom headers
headers = {
    'Content-Type': 'application/json',
    'Custom-Header': 'YourValue',
    # Add other headers as needed
}

# Data to be sent in a POST request (as an example)
data = {
    'key': 'value',
    # Add other key-value pairs as needed
}

# For JSON payload, you can use `json` instead of `data`:
# json_payload = {'key': 'value'}

# To disable proxies
proxies = {
    "http": None,
    "https": None,
}

# For a POST request, include `data` or `json` and `headers`
response = requests.post(url, verify=ca_cert_file_path, cert=(cert_file_path, cert_password),
                         headers=headers, data=data, proxies=proxies)

# For a GET request with headers and no proxy, simply remove the `data` or `json` parameter
# response = requests.get(url, verify=ca_cert_file_path, cert=(cert_file_path, cert_password),
#                         headers=headers, proxies=proxies)

print(response.text)
