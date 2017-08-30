FROM cdiener/qiime-docker

USER root

RUN apt-get update
RUN apt-get -y install vim
RUN conda install --yes --quiet flask
RUN conda install --yes --quiet h5py
RUN conda install --yes --quiet gunicorn
RUN conda install --yes --quiet futures
RUN conda install --yes --quiet trollius

USER jovyan
