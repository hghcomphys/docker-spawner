FROM jupyter/tensorflow-notebook 

ENV NB_USER=user
ENV HOME=/home/user
ENV XDG_CACHE_HOME=/home/user/.cache/
USER root
ARG JUPYTERHUB_VERSION=1.0.0
RUN pip install --no-cache jupyterhub==${JUPYTERHUB_VERSION}
RUN useradd -rm -d /home/user -s /bin/bash user
USER user
WORKDIR /home/user
# RUN mkdir -p /home/user/shared
CMD [ "start-notebook.sh" ]

