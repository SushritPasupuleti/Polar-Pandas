include .env

nix-shell:
	@echo "Entering nix-shell"
	@nix-shell ./shell.nix --run fish

run:
	@python3 app.py

source:
	@source venv/bin/activate

install:
	@uv pip sync ./requirements.txt

freeze:
	@uv pip freeze > ./requirements.txt
