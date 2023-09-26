# File:   project1.R
# Course: Introduction to Statistics
# Edwin Sanchez



# INSTALL AND LOAD PACKAGES ################################

library(datasets)  # Load base packages manually

# Installs pacman ("package manager") if needed
if (!require("pacman")) install.packages("pacman")

# Use pacman to load add-on packages as desired
pacman::p_load(pacman, rio) 



# LOAD DATA FROM FILES ####################################

# set our working directory
setwd("S:\\Classes\\Introduction to Statistics\\Project1\\")

# set this to be the path to where all of our data lives
BASE_PATH <- ".\\data\\pre_proc_data\\train\\"

# get data for images in the train set
img_data_train <- import(paste(BASE_PATH, "image_data.csv", sep=""))
head(IMAGE_DATA_TRAIN)

# get data for objects in the train set
obj_data_train <- import(paste(BASE_PATH, "object_data.csv", sep=""))
head(OBJ_DATA_TRAIN)


# DATA VIEWER ##############################################

?View
View(rio_csv)

# READ.TABLE FOR TXT FILES #################################

# R's built-in function for text files (used by rio)

# TEXT FILES

# Load a spreadsheet that has been saved as tab-delimited
# text file. Need to give complete address to file. This
# command gives an error on missing data but works on
# complete data.
txt_path = paste(path, "mbb.txt", sep="")
r_txt1 <- read.table(txt_path, header = TRUE)

# This works with missing data by specifying the separator: 
# \t is for tabs, sep = "," for commas. R converts missing
# to "NA"
r_txt2 <- read.table(txt_path, 
                     header = TRUE, 
                     sep = "\t")

# READ.CSV FOR CSV FILES ###################################

# R's built-in function for csv files (also used by rio)

# CSV FILES
# Don't have to specify delimiters for missing data
# because CSV means "comma separated values"
trends.csv <- read.csv(paste(path, "mbb.csv", sep=""), header = TRUE)

# CLEAN UP #################################################

# Clear environment
rm(list = ls()) 

# Clear packages
p_unload(all)  # Remove all add-ons

# Clear console
cat("\014")  # ctrl+L

# Clear mind :)