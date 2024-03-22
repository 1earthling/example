import subprocess

# Define your curl command
cert_file = "path/to/your/cert.pem"
cert_with_password = "path/to/your/cert.pem:your_password_here"
ca_cert_file = "path/to/your/ca_cert.pem"
url = "https://your.request.url.here/"

curl_command = [
    "curl",
    "--cacert", ca_cert_file,  # CA certificate
    "--cert", cert_with_password,  # Client certificate with password
    url  # URL to fetch
]

# Execute the curl command
result = subprocess.run(curl_command, capture_output=True, text=True)

# Check if the command was executed successfully
if result.returncode == 0:
    # Success, print the output
    print(result.stdout)
else:
    # An error occurred, print the error
    print("Error:", result.stderr)
