t:
	python3 -m unittest discover -v
c:
	coverage run -m unittest discover -v && coverage report
ch:
	coverage run -m unittest discover -v && coverage html && google-chrome htmlcov/index.html
