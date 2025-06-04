# Why?
This program is meant for sanitizing and plotting data exported from the X-LIMS system.
Inherently, X-LIMS tends to export CSV files that look something like this:

| SampledDate | Parameter                   | SWPPRCalc | ReportedResult | Unit     |
| ----------- | --------------------------- | --------- | -------------- | -------- |
| 6/1/2024    | Biochemical Oxygen Demand   | 586       | 586            | mg/L     |
| 6/1/2024    | pH                          | 6.66      | 6.66           | pH Units |
| 6/1/2024    | % Volatile Suspended Solids | 85        | 85             | %        |
| 6/1/2024    | Total Suspended Solids      | 814       | 814            | mg/L     |
| 6/1/2024    | TSS - Change in Wt          | 0.68      | 0.68           | %        |
| 6/1/2024    | Volatile Suspended Solids   | 690       | 690            | mg/L     |

Notice that the **Parameter** column has multiple parameters in it, and that the **SampledDate** column has redundant values.
Let's use pandas to get this CSV into **wide format**, with a column for each parameter and one row per time stamp! This will help with plotting curves, analyzing trends, and making our lives generally easier.

# Organization:

- src: Python source code
- exports: CSV and PNG files generated during the run
- imports: CSV files downloaded from X-LIMS. It is assumed that three lines will be skipped. The file names will be cleaned up to be used as chart titles, and the CSV import filenames will also be altered to make the export PNG and CSV filenames.
- configs: Users can dictate which data is ignored.

# Configuration:

- Edit /configs/exclude_parameters.toml to control which variables are shown (and not) in the PNG export charts, by commenting the ones you want to see.
- To print easy copy-and-paste variable lists from each file, edit /configs/show_parameter_lists.toml, so that ```show_parameter_lists = true```; The default is false, as in ```show_parameter_lists = false```.


# Quick Start
## Windows:
```
git clone https://github.com/City-of-Memphis-Wastewater/xlimsprep

cd xlimsprep

cat main.ps1

.\main 
```

## Linux:
```
git clone https://github.com/City-of-Memphis-Wastewater/xlimsprep

cd xlimsprep

cat main.sh

chmod +x main.sh

./main.sh 
```

# Step-by-step
## Windows:
Clone this repository, generating a folder in your current folder.

```git clone https://github.com/City-of-Memphis-Wastewater/xlimsprep ```

Navigate into the newly cloned directory.

```cd xlimsprep ```

Check the contents of the /imports/ directory.

```ls imports```

Generate a directory called **.venv**, to hold a Python virtual environment.
This virtual environment will use the same version of Python as your system installation unless otherwise specifed.
Alterantively you can use pyenv (not shown).
If you already have an environment, running this again should not hurt anything.

```python -m venv .venv```

Activate the virtual environment.
If you already have an environment active, running this again should not hurt anything.

```.venv\Scripts\activate ```

Prepare your local virtual environment with the packages necessary to run this software.
This is preferred to pip installing packges to your system Python. Why? Ask a friend. Ask a chatbot. Ask your father.

```pip install -r requirements.txt```

Run the main script to import your CSV files.
Export columnar CSV files (without ignoring any parameters).
Export PNG charts, which will ignore any parameters listed in /configs/exclude_parameters.toml. 

```python -m src.main```

Launch an image viewer to see the images in your /exports/ directory.

```python -m src.view```

Launch a tkinter window to enjoy navigating multiple CSV export files quickly. 
Small column titles? Tooltips to the rescue. Hover that mouse.

```python -m src.xplor```

Turn off your *venv* virtural environment.
It is easy to forget to turn your venv on and off, which is a major argument in favor of [Poetry](https://github.com/python-poetry/poetry).

```Deactivate```


See which parameters are suppressed from plotting to the PNG charts.
If a parameters is commented out using a pound sign in the skip_parameters list, it will *not* be suppressed.
Confusing, right?
The list is of items that will be suppressed.
So, if you prevent an item from being in the list by commenting it out, it will be kept in the plots.

```
cat .\configs\exclude_variables.toml
notepad .\configs\exclude_variables.toml
```

Okay, good luck.

# Rollout:

My projects typically use poetry and pyenv, but this one does not. 

This one just uses venv and a requirements.txt file.

Why? Because Termux has my attention right now.

# AI Disclaimer:

Artificial Intelligence was used for partial code generation and troubleshooting.
