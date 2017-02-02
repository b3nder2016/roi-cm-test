#!/bin/bash

sudo apt-add-repository -y ppa:ansible/ansible
sudo apt-get update
sudo apt-get install -y ansible

export ANSIBLE_INVENTORY=`pwd`/hosts
export ANSIBLE_CONFIG=`pwd`/ansible.cfg

ansible-playbook playbook.yml

mvn clean
rm -f roles/docker/files/TestWebApp.war

