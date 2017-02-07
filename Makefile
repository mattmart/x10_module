init:
	pip install -r requirements.txt

test:
	nosetests tests

install:
	cp temp_recorder.service /etc/systemd/system/temp_recorder.service
	mkdir -p /var/lib/temp_recorder
	cp temp_recorder/temp_recorder.py /var/lib/temp_recorder/temp_recorder.py
	systemctl daemon-reload
