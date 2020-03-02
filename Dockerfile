# base image 
FROM jupyterhub/jupyterhub:0.9.4

# install python packages
COPY requirements.txt /tmp/requirements.txt
RUN python3 -m pip install --no-cache -r /tmp/requirements.txt

# jupyterhub configration
COPY jupyterhub_config.py /srv/jupyterhub/jupyterhub_config.py

# SSL certificate and key
COPY mycert.pem mykey.key /srv/jupyterhub/

# idle service
COPY cull_idle_servers.py /srv/jupyterhub/cull_idle_servers.py
