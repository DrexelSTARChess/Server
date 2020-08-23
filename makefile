install :
	pip3 install flask flask-cors

run :
	env FLASK_APP=server.py flask run

test :
	python3 -m unittest test_*.py
