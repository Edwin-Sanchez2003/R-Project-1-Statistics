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

import os
import json
import csv

import math

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
parser.add_argument('-i', '--input_file_path', help="The path to the MSCOCO json file we want to collect information on.")
parser.add_argument('-o', '--output_dir', default="./pre_proc_data/", help="Where to write the collected data to. This is the path to a folder. If the folder doesn't exist, it will be created. If it already exists, it will be overwritten.")

# get arguments from user
args = parser.parse_args()

# Constants/Params #
INPUT_FILE_PATH = args.input_file_path
OUTPUT_DIR = args.output_dir


def main():
    # make output directory, if it doesn't already exist
    file_output_data_dir = os.path.join(
        OUTPUT_DIR, # the dir to output the data to
        os.path.splitext(os.path.basename(INPUT_FILE_PATH))[0] # make a folder specifically for this data
    ) # end os.path.join
    make_dir(path=file_output_data_dir)

    # load input MSCOCO json file
    data = load_json_file(file_path=INPUT_FILE_PATH)

    # collect the data that we want from the file
    collected_data = collect_data(data=data)

    # write data to csv files
    write_data_to_csvs(output_dir=file_output_data_dir, collected_data=collected_data)
# end main


# make dir for output data
def make_dir(path:str)-> None:
    # check if the path DOESN'T exist
    if os.path.exists(path) == False:
        # if it doesn't exist, make it
        os.makedirs(path)
    # end if
# end make_dir


# loads a json file into a python dictionary
def load_json_file(file_path:str)-> dict:
    with open(file_path, "r") as file:
        return json.load(file)
# end load_json_file


# collect the data that we want from an MSCOCO python dict
def collect_data(data:dict)-> tuple[dict, dict, dict]:
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
        - x, y coord for the center of the bbox. Location data of the object.
        - also, keep track of the image each object belongs to, as an index.
        
        This data is stored as the following:
        - metadata.csv, storing info from the entire dataset
        - imagedata.csv, storing the table with image information
        - objectdata.csv, storing the table for the objects (bboxes)

        However, this function simply outputs the data into a tuple of dicts:
        - output: (meta_data, image_data, object_data)
    """
    # data to store global information about the dataset
    meta_data = {
        "fields": ["image_count", "object_count"],
        "entries": [[len(data["images"]), len(data["annotations"])]]
    } # end meta_data dict

    # data to store with respect to the images
    image_data = {
        "fields": ["id", "file_name", "object_count", "width", "height", "area", "aspect_ratio", "aspect_ratio_float"],
        "entries": []
    } # end image_data dict

    # data to store with respect to the objects
    object_data = {
        "fields": ["image_id", "x", "y", "width", "height", "area", "aspect_ratio", "aspect_ratio_float"],
        "entries": []
    } # end object_data dict

    # collect data for image_data dict
    image_data["entries"]:list = []
    for image in data["images"]: # loop over each image entry in the MSCOCO dataset
        # get the data for one image
        image_id = int(image["id"])
        file_name = str(os.path.basename(image["file_name"]))
        width = int(image["width"])
        height = int(image["height"])
        area = width*height
        aspect_ratio = get_int_aspect_ratio(width=width, height=height)
        aspect_ratio = str(aspect_ratio[0]) + ":" + str(aspect_ratio[1])
        aspect_ratio_f = width/height # width / height
        
        # find out how many annotations belong to this image
        object_count = 0
        for annotation in data["annotations"]:
            # check if this annotation belongs to this image
            if int(annotation["image_id"]) == image_id:
                # add to object_count
                object_count += 1
            # end if
        # end for loop

        # append to our image_data entries as an image entry
        # must match our fields!
        # "fields": ["id", "file_name", "object_count", "width", "height", "area", "aspect_ratio", "aspect_ratio_float"]
        image_data["entries"].append(
            (image_id, file_name, object_count, width, height, area, aspect_ratio, aspect_ratio_f)
        ) # end append
    # end loop over images

    # collect data for object_data dict
    object_data["entries"]:list = []
    for annotation in data["annotations"]:
        # get data for one image
        image_id = int(annotation["image_id"])
        # bbox is in [x, y, width, height] format
        width = int(annotation["bbox"][2]) # width value in mscoco annotation format
        height = int(annotation["bbox"][3])
        # left x coord plus half the width gets us the x coord for the center of the bbox
        x = int(annotation["bbox"][0]) + (width//2)
        y = int(annotation["bbox"][1]) + (height//2)
        area = width*height
        aspect_ratio = get_int_aspect_ratio(width=width, height=height)
        aspect_ratio = str(aspect_ratio[0]) + ":" + str(aspect_ratio[1])
        aspect_ratio_f = width/height # width / height

        # append to our object_data entries as an object entry
        # must match our fields!
        # "fields": ["image_id", "x", "y", "width", "height", "area", "aspect_ratio", "aspect_ratio_float"]
        object_data["entries"].append(
            (image_id, x, y, width, height, area, aspect_ratio, aspect_ratio_f)
        ) # end append
    # end for loop over annotations

    # return the data we've collect on the file
    # tuple of (meta_data, image_data, object_data)
    return (meta_data, image_data, object_data)
# end collect_data


# take the data we collected and write it to a csv file
def write_data_to_csvs(output_dir:str, collected_data:tuple[dict, dict, dict])-> None:
    # create a dict of file names and data dicts for our output files
    csv_data:dict = {
        "meta_data.csv": collected_data[0],
        "image_data.csv": collected_data[1],
        "object_data.csv": collected_data[2]
    } # end csv_data dict

    # loop over each file we want to make
    for file_name, data in csv_data.items():
        # get the path of where to write the file
        file_path = os.path.join(output_dir, file_name)
        # get the fields and the entries from our data
        fields = data["fields"]
        entries = data["entries"]

        # open a file to write data to
        with open(file_path, 'w', newline='') as file:
            # create a csv writer to write to our file
            writer = csv.writer(file)
            
            # write our fields as the first row of the file
            writer.writerow(fields)

            # write all of our entries to the file
            for entry in entries:

                writer.writerow(entry)
            # end for loop writing entries
        # end file context
    # end for loop over files to write
# end write_data_to_csv


# get the aspect ratio as integers
# returns the values by (width, height)
def get_int_aspect_ratio(width:int, height:int)->tuple[int, int]:
    # find gcf (a.k.a. gcd) of width and height
    gcd = math.gcd(width, height)

    # divide width and height by gcd
    # use // (integer division) to coerce integer output instead of floating point output
    w_factor = width//gcd
    h_factor = height//gcd
    return (w_factor, h_factor)
# end get_int_aspect_ratio


if __name__ == "__main__":
    main()
