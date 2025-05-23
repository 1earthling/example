# Install prerequisites
sudo apt install curl gnupg2 apt-transport-https

# Import the public repository GPG keys
curl https://packages.microsoft.com/keys/microsoft.asc | sudo gpg --dearmor -o /etc/apt/trusted.gpg.d/microsoft.gpg

# Add the Microsoft package repository
echo "deb [arch=amd64] https://packages.microsoft.com/debian/12/prod bookworm main" | sudo tee /etc/apt/sources.list.d/mssql-release.list

# Update and install the ODBC driver
sudo apt update
sudo ACCEPT_EULA=Y apt install msodbcsql18
