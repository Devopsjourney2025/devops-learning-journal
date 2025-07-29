Docker Commands Overview
🚀 Run – Start a Container
bash
Copy
Edit
docker run nginx
Runs an instance of the nginx container.

If the image is not available locally, Docker pulls it from Docker Hub automatically.

📋 ps – List Containers
bash
Copy
Edit
docker ps
Lists running containers only.

bash
Copy
Edit
docker ps -a
Lists all containers, including stopped ones.

🛑 STOP – Stop a Container
bash
Copy
Edit
docker stop <container_id_or_name>
# Example:
docker stop silly_sammet
Stops a running container.

❌ rm – Remove a Container
bash
Copy
Edit
docker rm <container_id_or_name>
# Example:
docker rm silly_sammet
Permanently removes a container. The container must be stopped first.

📦 images – List Images
bash
Copy
Edit
docker images
Displays all downloaded images on your system.

🧹 rmi – Remove Images
bash
Copy
Edit
docker rmi nginx
Removes the specified image.

⚠️ Ensure no containers are using the image before removing it.

📥 pull – Download an Image
bash
Copy
Edit
docker pull ubuntu
Downloads an image without running it.

bash
Copy
Edit
docker run ubuntu
Pulls the image (if not present) and runs a container.

Since it's an OS-only image, it exits unless a process (like a web server) is running.

bash
Copy
Edit
docker run ubuntu sleep 5
Runs the container and exits after 5 seconds.

🔁 Run – Attached vs Detached Mode
bash
Copy
Edit
docker run kodekloud/simple-webapp
Runs and attaches to the container (foreground mode).

bash
Copy
Edit
docker run -d kodekloud/simple-webapp
Runs the container in detached mode (background).

bash
Copy
Edit
docker attach <container_id>
# Example:
docker attach a043d
Reattaches to a running container.

🖥️ Interactive Mode (TTY + STDIN)
Use -it for containers that require user input:

bash
Copy
Edit
docker run -it kodekloud/simple-prompt-docker
🌐 Port Mapping
bash
Copy
Edit
docker run -p 80:5000 kodekloud/webapp
Maps port 80 on the host to port 5000 in the container.

bash
Copy
Edit
docker run -p 3306:5000 mysql
Maps host port 3306 to container port 5000.

💾 Data Persistence with Volumes
By default, containers store data internally (ephemeral). To persist data:

bash
Copy
Edit
# Without volume mapping (data lost on container deletion)
docker run mysql
docker stop mysql
docker rm mysql
bash
Copy
Edit
# With volume mapping (data persisted)
docker run -v /opt/datadir:/var/lib/mysql mysql
Mounts host directory /opt/datadir to container path /var/lib/mysql.

🔍 Inspect – Container Details
bash
Copy
Edit
docker inspect <container_id_or_name>
Returns detailed container configuration in JSON format.

🧪 Example App Output
When running kodekloud/simple-webapp, output might include:

csharp
Copy
Edit
* Serving Flask app "app" (lazy loading)
* Running on http://0.0.0.0:8080/ (Press CTRL+C to quit)
This is a simple web app displaying a colored background.

docker network create Command:
bash
Copy
Edit
docker network create \
  --driver bridge \
  --subnet 182.18.0.0/16 \
  custom-isolated-network
  
Deploy Private Registry:
docker run -d -p 5000:5000 --name registry registry:2

Command	Action	Analogy
tag->Label it	Write address on the package
push->Send it	Ship the package to warehouse
pull->Receive it	Get the package from warehouse
