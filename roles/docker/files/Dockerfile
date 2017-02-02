FROM ubuntu:16.04

ENV ANSIBLE_INVENTORY /root/hosts
ENV ANSIBLE_CONFIG /root/ansible.cfg
ENV JAVA_HOME /usr/lib/jvm/java-8-openjdk-amd64
ENV DEBIAN_FRONTEND noninteractive

RUN apt-get update
RUN apt-get install -y apt-utils
RUN apt-get install -y tomcat8 ansible openjdk-8-jdk

RUN echo "JAVA_HOME=/usr/lib/jvm/java-8-openjdk-amd64 >> /etc/default/tomcat8"

COPY ansible.cfg /root
COPY hosts /root
COPY TestWebApp.war /root
COPY deploy.yml /root

RUN cd /root && ansible-playbook deploy.yml

EXPOSE 8080

CMD service tomcat8 start || tail -f /var/lib/tomcat8/logs/catalina.out
