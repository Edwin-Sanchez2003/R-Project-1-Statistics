"""
    Introduction to Statistics
    R Project 1

    Python version: 3.11.X
    
    Synthesize Data
    This python file contains code that takes MSCOCO json annotations
    and organizes them in a way that R can easily understand the data.

    What is our data?
    Our data is object annotations; ie bounding boxes (bboxes) which
    specify where in an image an object is located. This data is usually
    used to train Convolutional Deep Neural Networks (CNNs) to identify
    and classify objects for vision processing. Our data contains a list
    of images and a list of annotations (ie. bboxes) that correspond to 
    the images and tell us where objects are in each image.

    We have 3 datasets:
    - train
    - validation
    - test
    We will perform analysis on all 3 sets to draw some conclusions from
    the data that will be used to train models.
    
    (Again, repeat this for each of the 3 datasets.)
    What are we collecting?:
    - total # of objects
    - total # of images
    - # of objects in each image (avg, std dev, mean, median, etc.)
    - area of each bounding box
    - width and height of each bounding box
    - calculate and store aspect ratio of each bounding box

    How can we view the data? (for later)
    - By image. What are the characteristics of each of our images?
    - By object. What do all of our objects have in common?
"""

import json
import csv

import argparse

# the description of the file when used on the terminal
descr = """
    Collects useful data from MSCOCO annotation file and 
    organizes it into a csv file to be read by R program.
"""

# for parsing arguments from the command line
parser = argparse.ArgumentParser(
    prog='Data Synthesizer for R Project 1',
    description=descr
) # end ArgumentParser construction

# arguments to be passed in by the user via the command line/terminal
parser.add_argument('-i', '--input_file_path', help="The MSCOCO json file we want to collect information on.")
parser.add_argument('-o', '--output_file_path', help="Where to write the collected data to. This is the path to a csv file, along with the file name. EX: './data.csv'")

# get arguments from user
args = parser.parse_args()

# Constants/Params #
INPUT_FILE_PATH = args.input_file_path
OUTPUT_FILE_PATH = args.output_file_path


def main():
    # load input MSCOCO json file
    data = load_json_file(file_path=INPUT_FILE_PATH)

    # collect the data that we want from the file
    collected_data = collect_data(data=data)

    # write data to csv file
    write_data_to_csv(file_path=OUTPUT_FILE_PATH, collected_data=collected_data)
# end main


# loads a json file into a python dictionary
def load_json_file(file_path:str)-> dict:
    with open(file_path, "r") as file:
        return json.load(file)
# end load_json_file


# collect the data that we want from an MSCOCO python dict
def collect_data(data:dict)-> tuple():
    """
        Collect the data we want from the MSCOCO annotations.
        The data we want:

        Metadata:
        - Total # of objects (integer). How many objects are in the entire dataset?
        - Total # of images (integer). How many images are in the entire dataset? 
       
        Image Data:
        - Number of objects in each image (integer). How many objects are in each image?
          Store this as a column in a table, where each row is a new image.
        - Width, height, Area, and Aspect Ratio of each image.
        - store file name for convenience
        
        Object Data:
        - Area of each object bbox (integer). What is the area of each object
          in the dataset? Store this as another table, with each row being an annotation
          and a column corresponding to the area.
        - Width and Height of each objects. Two more columns for our object table.
        - Calculate and store aspect ratio of each bounding box. Another column
          for the objects table.
        - also, keep track of the image each object belongs to, as an index.
        
        This data is stored as the following:
        - metadata.csv, storing info from the entire dataset
        - imagedata.csv, storing the table with image information
        - objectdata.csv, storing the table for the objects (bboxes)
    """
    # data to store global information about the dataset
    meta_data = {
        "image_count": len(data["images"]),
        "object_count": len(data["annotations"])
    } # end meta_data dict

    # data to store with respect to the images
    image_data = {
        "fields": ["id", "file_name", "object_count", "width", "height", "area", "aspect_ratio"],
        "entries": []
    } # end image_data dict

    # data to store with respect to the objects
    object_data = {
        "fields": ["image_id", "width", "height", "area", "aspect_ratio"],
        "entries": []
    } # end object_data dict




# end collect_data


# take the data we collected and write it to a csv file
def write_data_to_csv(file_path:str, collected_data)-> None:
    # open a file to write data to
    with open(file_path, 'w', newline='') as file:
        writer = csv.writer(file)
        field = ["name", "age", "country"]
        
        writer.writerow(field)
        writer.writerow(["Oladele Damilola", "40", "Nigeria"])
        writer.writerow(["Alina Hricko", "23", "Ukraine"])
        writer.writerow(["Isabel Walter", "50", "United Kingdom"])
    # end file context
# end write_data_to_csv


if __name__ == "__main__":
    main()
