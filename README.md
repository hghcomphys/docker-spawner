# jupyterhub-setup
This shows how to setup a containerized jupyterhub on GPU.

### Current version:
- only tested on Ubuntu `16.4` and `18.4`
- use dummy authentication
- user data is persistent
- hub data is not persistent for development reasons
- host docker socket is bind mounted into the hub container (may not work on windows host)
- use Nvidia runtime for GPU
- spawner calss is dockerspawner
- spawner options for notebook image 


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

to see the log
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


### Useful links:
- [https://github.com/jupyterhub/dockerspawner](https://github.com/jupyterhub/dockerspawner)
