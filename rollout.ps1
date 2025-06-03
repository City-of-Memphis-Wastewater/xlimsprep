try:
	pyenv install 3.12.10
	pyenv local 3.12.10
except:
	echo "pyenv is not installed"
	echo "Python version is 3.12.10"
	echo "Version requirement limitation not yet determined. "
	echo "Setup will proceed."

python -m venv .venv # creates a virtaul envirnment so that to install pacakges relevant to this project without impacting system Python 
try{
    .venv\Scripts\activate # activates that new environment, in PowerShell. Once activated, your PowerShell prompt will change to "(.venv) PS [path]>" instead of just "PS [path]>"
}
catch {
    source venv/bin/activate # linux
}
pip install pandas