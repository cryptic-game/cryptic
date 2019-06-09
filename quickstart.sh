#!/bin/bash

# try to install everything needed to run

if [ -f "/etc/arch-release" ]; then
  # TODO packages for arch linux
  echo "::: Arch linux detected but installing the basic dependencies is not yet implemented"
elif [ -f "/etc/debian_version" ]; then
  echo "::: Debian based linux detected, updating system"
  sudo apt-get update
  echo "::: Installing basic programs"
  sudo apt install -y git curl python3.7 python3-pip
  echo "::: Installing pipenv"
  sudo python3.7 -m pip install pipenv
else
  echo "::: Unknown operating system, assuming that all necessary packages are installed..."
fi

# clone the "base" repo and run the dev installer

mkdir cryptic && cd cryptic
echo "::: Cloning base repository"
git clone https://github.com/cryptic-game/cryptic.git
cd cryptic
echo "::: Installing dependencies for development environment installer"
pipenv install
echo "::: Cloning/Installing microservices and so on"
pipenv run python install-dev.py install
