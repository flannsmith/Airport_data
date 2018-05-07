Airports
========

This is a candidate solution for the term project of COMP20230.


Prerequisites
----------------------

This project was created in a Python 3.6 environment. It will be easier to set up the project if you install [Anaconda](https://conda.io/docs/user-guide/install/download.html) or [Miniconda](https://conda.io/miniconda.html). Other options, such as [PyEnv](https://github.com/pyenv/pyenv) and classic virtual environment (i.e. `venv`), will also work.


Installation and Setup
----------------------

Run the following commands in Terminal:

```sh
git clone git@github.com:flannsmith/Airport_data.git
cd Airport_data
conda env create -f=environment.yml OR conda create -n comp2023017202469 Python=3.6
source activate comp2023017202469 OR activate comp2023017202469
pip install -r requirements.txt
```

Running the Program
-------------------

From the project directory (in Terminal), run this command

```sh
python main.py 'testrouteFilePath'

where 'testrouteFilePath' is the complete path to the testroutes.csv file
```
