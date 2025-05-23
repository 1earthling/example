# Install prerequisites
sudo apt install curl gnupg2 apt-transport-https

# Import the public repository GPG keys
curl https://packages.microsoft.com/keys/microsoft.asc | sudo gpg --dearmor -o /etc/apt/trusted.gpg.d/microsoft.gpg

# Add the Microsoft package repository
echo "deb [arch=amd64] https://packages.microsoft.com/debian/12/prod bookworm main" | sudo tee /etc/apt/sources.list.d/mssql-release.list

# Update and install the ODBC driver
sudo apt update
sudo ACCEPT_EULA=Y apt install msodbcsql18


# Create a working directory
mkdir -p ~/debian-certs-fix && cd ~/debian-certs-fix

# Download the .deb file for ca-certificates from a Debian mirror using HTTP (not HTTPS)
wget http://ftp.us.debian.org/debian/pool/main/c/ca-certificates/ca-certificates_20230311_all.deb

# Install it manually
sudo dpkg -i ca-certificates_20230311_all.deb

# Update the certs
sudo update-ca-certificates


wget https://packages.microsoft.com/debian/12/prod/pool/main/m/msodbcsql18/msodbcsql18_18.3.2.1-1_amd64.deb
sudo ACCEPT_EULA=Y dpkg -i msodbcsql18_18.3.2.1-1_amd64.deb
