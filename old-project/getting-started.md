1. How to Install Docker
🖥️ For Ubuntu (Linux)
Go to https://docs.docker.com/
# Update packages
sudo apt update

# Install prerequisites
sudo apt install apt-transport-https ca-certificates curl software-properties-common

# Add Docker’s GPG key
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /etc/apt/trusted.gpg.d/docker.gpg

# Add Docker repo
echo "deb [arch=$(dpkg --print-architecture)] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" | \
  sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

# Update and install Docker
sudo apt update
sudo apt install docker-ce -y
sudo docker version - Run after installation done

# Start Docker and enable on boot
sudo systemctl start docker
sudo systemctl enable docker

# Optional: Run Docker without sudo
sudo usermod -aG docker $USER
🔁 Reboot or re-login after adding yourself to the docker group.

Popular images will be find here - https://hub.docker.com/

For Windows / macOS
1. Download Docker Desktop from https://www.docker.com/products/docker-desktop
Install and run it.

2. Verify Installation -  docker --version          # Check Docker version
docker info               # System info
Use the Docker CLI from a terminal (cmd, PowerShell, or WSL).

3. Basic Docker Commands
docker run redis - Docker pulls and Runs instance of Redis image locally from Docker hub
Search & Pull Images
bash
Copy
Edit
docker search nginx         # Search for images on Docker Hub
docker pull nginx           # Download nginx image locally
📦 Run an Image (as a container)
bash
Copy
Edit
docker run -d -p 8080:80 nginx
-d → Detached (runs in background)

-p → Port mapping: host:container

Open http://localhost:8080 in your browser.

🧾 List Running Containers
bash
Copy
Edit
docker ps                 # Running containers
docker ps -a              # All containers (including stopped)
🛑 Stop / Remove Containers

docker stop <container_id>
docker rm <container_id>
🧹 Remove Images

docker rmi <image_id>
📂 View Images, Networks, Volumes

docker images             # List all images
docker network ls         # List networks
docker volume ls          # List volumes
📄 View Logs of a Container

docker logs <container_id>
⚙️ 4. Common Use Cases
Create custom images using a Dockerfile

Use docker-compose.yml for multi-container apps

Mount volumes for persistent data

Set environment variables with -e

