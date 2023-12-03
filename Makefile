
PHONY: venv
venv:
	python -m venv .venv
	.\.venv\Scripts\activate.bat && pip install -r requirements.txt
#	source venv/bin/activate && pip install -r requirements.txt
