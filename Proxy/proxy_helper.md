## Install squid

- sudo apt update
- sudo apt install squid -y

## Find squid

- /etc/squid/squid.conf

# Edit o arquivo
sudo nano /etc/squid/squid.conf

# Define who can use (ex: your local network)
acl localnet src 192.168.0.0/16  # ajuste conforme sua rede
http_access allow localnet
http_access deny all

# Default Port
http_port 3128

# Restart squid
sudo systemctl restart squid
