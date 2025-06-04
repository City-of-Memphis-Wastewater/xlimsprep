#!/bin/bash
cat main.sh
python -m venv .venv 
source venv/bin/activate # linux
pip install -r requirements.txt
python -m src.main
python -m src.view
python -m src.xplor