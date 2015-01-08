
%define _rpmfilename %%{NAME}-%%{VERSION}-%%{RELEASE}.%%{ARCH}.rpm

Name:		kibana		
Version:	3.1.2	
Release:	2%{?dist}
Summary:	Kibana is a browser based analytics and search interface for Elasticsearch that was developed primarily to view Logstash event data.	
Group:		Productivity/Visualization
License:	Apache-2.0	
URL:		http://www.elasticsearch.org/overview/kibana	
Source0:	https://download.elasticsearch.org/kibana/kibana/kibana-%{version}.tar.gz
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires:  tar

%description
Kibana is an open source (Apache Licensed), browser based analytics and search interface to Logstash and other timestamped data sets stored in ElasticSearch. With those in place Kibana is a snap to setup and start using (seriously). Kibana strives to be easy to get started with, while also being flexible and powerful

%prep
%setup -q

%install
install -p -d -m 0775 %{buildroot}%{install_dir}
cp -r * %{buildroot}%{install_dir}

%clean
rm -rf %{buildroot}


%files
%defattr(-,root,root,-)
%doc
%{install_dir}/*
%config(noreplace) %{install_dir}/config.js


%changelog
* Thu Jan 08 2015 Jean-François Roche <jfroche@affinitic> 1:3.1.2-2
- Set config file
- Add docker build
- Add parameter for install_dir
* Wed Nov 26 2014 Marcel Fuhrmann <github@mfsystems.me> 1:3.1.2-1
- update to kibana version 3.1.2
* Wed Oct 01 2014 Marcel Fuhrmann <github@mfsystems.me> 1:3.1.0-1
- first RPM-Release
