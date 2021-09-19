dob:
	docker build -t weltyt .
dor:
	docker run -it weltyt
dobr:
	make dob && make dor 