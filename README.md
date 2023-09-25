Introduction to Statistics
Edwin Sanchez
# R Project 1: Statistical Analysis of Ship Data for Object Detection
This is the GitHub repo for the first R project for STAT 300 - Introduction to Statistics. This README details what the repo contains and other details.

* **Python Version:** `3.11.X`
* **Dependencies:** `None`, *base python installation.*

## Setup
To use the tools in the repo, you must first set up an environment. It is recommended that you use an environment/package manager. I use [anaconda](https://www.anaconda.com/), but you may use whatever you like.

* **Anaconda Link:** https://www.anaconda.com/

Setup your environment with python version `3.11.X` - any version of python `3.11` will work. This may work with older versions of python, but this has only been tested with version `3.11.2`.

## Data Synthesizer
In order to perform our statistical analysis, we need to collect the useful data from our annotation files. This means reading in the annotation files, extracting only the data we want to look at, then writing it to a csv file so we can perform data analysis in R. I have chosen to do this with a python script, called `synthesize_data.py`. Below is how to use the file.

*Note: This script assumes the input data is in MSCOCO (Microsoft Common Objects in Context) format. This is a format developed by Microsoft for their object detection and segmentation challenges.*
* **Link to COCO Website:** https://cocodataset.org/#home
* **Link to MSCOCO Format on COCO Website:** https://cocodataset.org/#format-data

### Usage
To use `synthesize_data.py`, you will execute the python script from the terminal. You must specify the following arguments:
* **--input_file_path (-i):** The path to the MSCOCO json file we want to collect information on.
* **--output_dir (-o):** *Default: "./pre_proc_data/"* Where to write the collected data to. This is the path to a folder. If the folder doesn't exist, it will be created. If it already exists, it will be overwritten.

It is worth noting that the **output_dir** will be more or less the home for the data being generated. It is assumed that this script will be used multiple times on different data files. With that in mind, the script creates a subdirectory in the **output_dir** with the same name as the annotation file being processed. The data synthesized from the input file is then stored in this subdirectory, created specifically for this file's data.

### Example Usages
This is an example usage of the `synthesize_data.py` file, where the following command is executed at the root directory of this project:

* **Short Flags:** `python ./src/synthesize_data.py -i ./data/raw_data/train.json -o ./data/pre_proc_data/`
* **Long Flags:** `python ./src/synthesize_data.py --input_file_path ./data/raw_data/train.json -output_dir ./data/pre_proc_data/`
* **No ouput_dir specified (default output_dir):** `python ./src/synthesize_data.py -i ./data/raw_data/train.json`
