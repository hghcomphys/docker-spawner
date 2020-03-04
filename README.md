# jupyterhub-setup
This (incomplete) repo shows how to setup a containerized jupyterhub service on a single-node GPU server.
### Current version:
- is under developement
- only tested on Ubuntu `16.4` and `18.4`
- uses dummy authentication
- user data is persistent
- hub data is not persistent for development reasons
- host docker socket is bind mounted into the hub container (may not work on a host with Windows OS)
- uses Nvidia runtime for GPU
- spawner calss is dockerspawner
- spawner options for notebook images are available 
- CPU version is also possible with small changes


### Directory structure:
```
Jupyterhub-setup
├── cull_idle_servers.py
├── docker-compose.yaml
├── Dockerfile
├── images
│   ├── make-all-images.sh
│   ├── tensorflow-v2-cpu
│   │   └── Dockerfile
│   └── tensorflow-v2-gpu
│       └── Dockerfile
├── jupyterhub_config.py
├── mycert.pem
├── mykey.key
└── requirements.txt
```

### Dependencies:
make sure that the most updated dependencies are install and working flawlessly
- [docker-engine](https://docs.docker.com/install/) 
- [docker Nvidia plugin](https://github.com/NVIDIA/nvidia-docker)
- [docker-compose](https://docs.docker.com/compose/install/)

### How to run docker-based jupyterhub:

make all notebook images
```
cd images
./make-all images
```
create docker network for the jupyterhub internal connection
```
docker network create jupyterhub-network
```

run jupyterhub server
```
docker-compose build -f docker-compose.yaml
docker-compose up -d
```

to see the logs
```
docker-compose logs
```


### How to delete the service:
stop and remove containers
```
docker-compose down 
```

remove the created network
```
docker network rm jupyterhub-network
```

remove user data volumes
```
docker container prune
docker volume prune 
```
please be careful with the `prune` command, it removes __all unused__ containers and volumes from the docker.

### Useful links:
- [https://github.com/jupyterhub/dockerspawner](https://github.com/jupyterhub/dockerspawner)


### Snapshots:
login -> spawn a selected image -> notebook with GPU access

<img src="./snapshots.gif" width="800" height="400" />

