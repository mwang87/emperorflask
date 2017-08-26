FROM cdiener/qiime-docker

USER root

RUN apt-get update
RUN apt-get -y install vim
RUN conda install --yes --quiet flask
RUN conda install --yes --quiet h5py

USER jovyan
