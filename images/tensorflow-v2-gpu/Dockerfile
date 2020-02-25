FROM d4n1el/tensorflow-2-notebook-gpu 
ENV NB_USER=user
ENV HOME=/home/user
ENV XDG_CACHE_HOME=/home/user/.cache/
USER root
RUN useradd -rm -d /home/user -s /bin/bash user
USER user
WORKDIR /home/user
CMD [ "start-notebook.sh" ]

#FROM tensorflow/tensorflow:nightly-gpu-py3-jupyter 
# #RUN apt update && apt install -y npm \
#     && pip install jupyterhub==0.9.4 notebook=5.7.2 \
#     && npm install -g configurable-http-proxy \
#     && apt clean && rm -rf /var/lib/apt/lists/*
#USER root
#RUN useradd -rm -d /home/user -s /bin/bash user
#USER user
#WORKDIR /home/user
#CMD ["jupyterhub-singleuser"]

