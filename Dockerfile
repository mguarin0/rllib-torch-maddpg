ARG BASE_IMG=rayproject/ray:1.5.2-py38-gpu
ARG PRJ_DIR=/usr/src/app/rllib-torch-maddpg

FROM ${BASE_IMG}

USER ${RAY_UID}
ENV HOME=${PRJ_DIR}
RUN mkdir -p /usr/src/app/rllib-torch-maddpg

# install packages
RUN apt-get update -y \
  && apt-get install -y swig \
  && apt-get install -y cmake \ 
  && apt-get install ffmpeg libsm6 libxext6  -y \
  && apt-get install python-opengl -y \
  && apt-get install freeglut3-dev -y \
  && apt-get clean
