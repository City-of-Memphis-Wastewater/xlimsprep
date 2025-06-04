cat main.ps1
python -m venv .venv 
.venv\Scripts\activate # activates that new environment, in PowerShell. Once activated, your PowerShell prompt will change to "(.venv) PS [path]>" instead of just "PS [path]>"
pip install -r requirements.txt
python -m src.main
python -m src.view
python -m src.xplor