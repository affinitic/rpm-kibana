rpm-kibana
==============
This repository provides the neccessary Files for building Specfile to build an RPM for Kibana. 


Build Requirements
==================

* add new User for the rpmbuild
	* `useradd builder`


Install Directory
=================

* /srv/kibana

Install Build Tools
===================

```
yum install rpm-build make gcc

#Before you install the the fedora-packer / mock you need to install the EPEL-Repository (Rebuild of Fedora packages for RHEL or compatible derivatives)


#RHEL6 EPEL
yum install http://dl.fedoraproject.org/pub/epel/6/x86_64/epel-release-6-8.noarch.rpm


#RHEL7 EPEL
yum install http://dl.fedoraproject.org/pub/epel/7/x86_64/e/epel-release-7-2.noarch.rpm


#Install fedora-packager
yum install fedora-packager
```

Buildout Proccess
=================

```
# change in Users Homedir
cd

# Clone Repository
git clone https://github.com/SOLDIERz/rpm-kibana.git

# build SRPM 
rpmbuild --define="install_dir /var/www/kibana" -bs rpmbuild/SPECS/kibana.spec

# build RPM for RHEL7
/usr/bin/mock -r epel-7-x86_64 --rebuild rpmbuild/SRPMS/kibana-3.1.0.x86_64.src.rpm

# build RPM for RHEL6
/usr/bin/mock -r epel-6-x86_64 --rebuild rpmbuild/SRPMS/kibana-3.1.0.x86_64.src.rpm
```

Docker Process
==============

Create rpm using docker images:

make build

Install kibana trough yum
=========================

`yum install kibana-3.1.0.x86_64.rpm`


Install kibana through puppet
=============================

```
# If you install through package type you need to create an repo for your rpms

package {'kibana':
	ensure	=> installed
}

or

exec {'Install Kibana':
	command	=> 'yum install -y kibana-3.1.0.x86_64.rpm',
	path	=>	['/usr/bin','/usr/sbin']
}
```
