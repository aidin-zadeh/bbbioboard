# Belly-button Biodiversity Board
<p>This repository contains a Python project that implements a Flask based dashboard to explore Belly Button Diversity Dataset.
The current implementation implements the following objectives:
- USe Python and SQLAlchemy to perform data exploration and data data retrieval.
- Implement a Flask Web application.
- Build interactive data visualization by Plotyly.js and D3.js.
- Deply the webapp to Heroku.

The current implementation of this project is [here](https://git.heroku.com/bbbioboard-heroku.git).

## Data
[Belly Button Biodiversity Dataset](http://robdunnlab.com/projects/belly-button-biodiversity/) by Rob Dun Lab.

## Report

## Requirements
- flask         1.0.2
- jupyter       1.0.0 
- nb_conda      2.2.1
- sqlalchemy    1.2.10
- pandas        0.23.3
 
## Directory Structure
```
.
├── docs                <- Documents related to this project
├── images              <- Images for README.md files
├── notebooks           <- Ipythoon Notebook files
├── reports             <- Generated analysis as HTML, PDF, Latex, etc.
│   ├── figures         <- Generated graphics and figures used in reporting
│   └── logs            <- Generated log files  
└── bbbioboard
    ├── conf
    ├── data            <- data utilized in this project
    │   ├── ext
    │   ├── int
    │   └── raw
    ├── src             <- Source files used in this project
    ├── static          <- CSS/SCSS/JS/Vedoer source files
    └── templates       <- Flask templates 
```
## Installation
Install python dependencies from  `requirements.txt` using conda.
```bash
conda install --yes --file conda-requirements.txt
```

Or create a new conda environment `<new-env-name>` by importing a copy of a working conda environment at the project root directory :`conda-env-bbbioboard.yml`.
```bash
conda env create --name <new-env-name> -f conda-env-bbbioboard.yml
```
## Usage
```bash
python run.py

```
## References

## To Do

- [ ] Add Charts templates.
- [ ] Add Table

## License
MIT License 

