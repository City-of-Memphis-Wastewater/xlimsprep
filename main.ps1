cat main.ps1
python -m venv .venv 
.venv\Scripts\activate # activates that new environment, in PowerShell. Once activated, your PowerShell prompt will change to "(.venv) PS [path]>" instead of just "PS [path]>"
pip install -r requirements.txt
python -m src.main
python -m src.view
python -m src.xplor
echo "Edit \\configs\\exclude_parameters.toml to control which variables are shown (and not) in the PNG export charts, by commenting the ones you want to see." 
deactivate