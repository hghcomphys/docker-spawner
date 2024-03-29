import os

# user authentication
c.JupyterHub.authenticator_class = 'dummyauthenticator.DummyAuthenticator'
c.DummyAuthenticator.password = "testpass"
c.Authenticator.admin_users = {'admin'}
c.JupyterHub.admin_access = True
#c.Spawner.args = ['--allow-root']

# set lab as default user interface
c.Spawner.default_url = '/lab'

# named server
c.JupyterHub.allow_named_servers = True
c.JupyterHub.named_server_limit_per_user = 2

# spawn docker container
c.JupyterHub.spawner_class = 'dockerspawner.DockerSpawner'

# we need the hub to listen on all ips when it is in a container
c.JupyterHub.hub_ip = '0.0.0.0'
#c.JupyterHub.hub_port = 8080
#c.JupyterHub.ip = '0.0.0.0'
c.JupyterHub.port = 8080

# the hostname/ip that should be used to connect to the hub
# this is usually the hub container's name
c.JupyterHub.hub_connect_ip = 'jupyterhub'
# tell the user containers to connect to our docker network
c.DockerSpawner.network_name = 'jupyterhub-network'
c.DockerSpawner.debug = True
c.DockerSpawner.use_internal_ip = True
#c.Spawner.ip = '127.0.0.1'
c.DockerSpawner.extra_host_config = { 'network_mode': 'jupyterhub-network' }
c.DockerSpawner.extra_start_kwargs = { 'network_mode': 'jupyterhub-network' }

## Path to SSL certificate file for the public facing interface of the proxy
#
#  When setting this, you should also set ssl_key
# c.JupyterHub.ssl_cert = '/srv/jupyterhub/mycert.pem'
## Path to SSL key file for the public facing interface of the proxy
#
#  When setting this, you should also set ssl_cert
# c.JupyterHub.ssl_key = '/srv/jupyterhub/mykey.key'

# pick a docker image. This should have the same version of jupyterhub
# in it as our Hub.
c.DockerSpawner.image =  os.environ.get('DOCKER_NOTEBOOL_IMAGE') 
c.DockerSpawner.image_whitelist = {
    "tensorflow-v2-gpu": "notebook:tensorflow-v2-gpu",
    "tensorflow-v2-cpu": "notebook:tensorflow-v2-cpu",
}
# user account inside the conainer
#c.DockerSpawner.extra_create_kwargs = {'user': 'user'}
#c.Spawner.environment = {'GRANT_SUDO': 'yes'}

# CPU 
c.Spawner.mem_limit = '2G'
c.Spawner.cpu_limit = 1

# GPU 
#c.DockerSpawner.extra_host_config = {'--gpus': '1'}
#c.DockerSpawner.extra_start_kwargs = { 'gpus': 'all' }
#c.DockerSpawner.extra_create_kwargs = {'runtime': 'nvidia'}
c.DockerSpawner.extra_host_config = {'runtime': 'nvidia'}

# delete containers when the stop
c.DockerSpawner.remove = True

# user data persistence
notebook_dir = os.environ.get('DOCKER_NOTEBOOK_DIR')
c.DockerSpawner.notebook_dir = notebook_dir
c.DockerSpawner.volumes = { 'jupyterhub-user-{username}': notebook_dir, 'jupyterhub-shared': '/home/user/shared' }

# shutdown idle notbooks
c.JupyterHub.services = [
    {
        'name': 'cull-idle',
        'admin': True,
        'command': [os.sys.executable, 'cull_idle_servers.py', '--timeout=1800'],
    }
]
