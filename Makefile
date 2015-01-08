build:
	docker build -t kibana-rpm .
	docker run --name kibana-rpm kibana-rpm rpm -ivh /root/RPMS/*.rpm
	docker cp kibana-rpm:/root/RPMS/ .
	docker rm kibana-rpm
