FROM centos:centos6
MAINTAINER Jean-François Roche <jfroche@affinitic.be>

RUN yum -y install git
RUN yum -y install rpm-build
RUN yum -y install yum-utils
RUN yum -y install rpmdevtools
RUN yum -y install wget
ENV HOME /root
WORKDIR /root/
COPY . /root
RUN echo '%_topdir %(echo $HOME)' > /root/.rpmmacros
RUN yum-builddep -y SPECS/kibana.spec
RUN rpmbuild -bb --define="install_dir /var/www/kibana" SPECS/kibana.spec
