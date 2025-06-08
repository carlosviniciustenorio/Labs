# Install nginx

sudo apt install nginx -y

# Create file configuration

sudo nano /etc/nginx/sites-available/meuproxy


server {
    listen 80;

    location / {
        proxy_pass http://localhost:5000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
    }
}


# Active site

sudo ln -s /etc/nginx/sites-available/meuproxy /etc/nginx/sites-enabled/
sudo nginx -t  # testar config
sudo systemctl restart nginx

# Test

python3 -m http.server 5000
Access http://localhost