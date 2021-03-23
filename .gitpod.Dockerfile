FROM gitpod/workspace-full

RUN sudo apt-get update
RUN sudo apt install snapd
RUN sudo snap install heroku --classic