init:
	pip install -r requirements.txt

test:
	nosetests tests

install:
	cp x10_controller.service /etc/systemd/system/x10_controller.service
	mkdir -p /var/lib/x10_controller
	cp x10_controller/x10_controller.py /var/lib/x10_controller/x10_controller.py
	chmod +x /var/lib/x10_controller/x10_controller.py
	systemctl daemon-reload
