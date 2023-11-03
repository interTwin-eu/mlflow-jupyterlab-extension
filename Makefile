env:
	micromamba env create -p ./.venv --file env.yml -y
	micromamba run -p ./.venv pip install -e .