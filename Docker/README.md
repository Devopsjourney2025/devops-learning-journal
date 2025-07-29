# Docker
Docker
In application we have different servers like web, Database, Rabbit MQ, Reddis 
So we need to ensure all servers are compatabile with application libraries, dependencies and OS.
<img width="848" height="632" alt="image" src="https://github.com/user-attachments/assets/a088a3e0-e884-4f4f-9626-1d35a95138c5" />
Docker basically contaninerize the application without distrubing the OS and has all dependicies and libraries each component has seperate Containers(web, DB and Message broker(rabbit MQ) and Orchestration)
<img width="846" height="687" alt="image" src="https://github.com/user-attachments/assets/e6fc5ded-951e-4ea6-909b-bfb35a41dc2f" />
CONTAINERS: 
Has it's own network,mount and process but share same OS kernel(Linux).Docker containers share any OS(centos,debian) as long as the kernal is matching.
LXC stands for Linux Containers - It’s a lightweight virtualization technology that allows you to run multiple isolated Linux systems (containers) on a single host, without needing full virtual machines.
VM and conatainers:
<img width="1002" height="645" alt="image" src="https://github.com/user-attachments/assets/5f0f0f57-a601-4552-abf8-cfaf2be21997" />
VM needs it's own OS and hardware - run's above hypervisers which allocates the VM and hardwares
Conatiners and Images:
Image -Contains application code + dependencies
Built from a Dockerfile
Stored in a registry (like Docker Hub) Eg - docker pull python:3.10
Conatiner - A live, isolated environment running your image
Has its own file system, network, processes
You can run, stop, pause, or delete it
<img width="800" height="800" alt="image" src="https://github.com/user-attachments/assets/5f0d8cd6-368e-4aaf-8c6c-3e683871e160" />
