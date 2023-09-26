# File:   project1.R
# Course: Introduction to Statistics
# Edwin Sanchez



# INSTALL AND LOAD PACKAGES ################################

# Installs pacman ("package manager") if needed
if (!require("pacman")) install.packages("pacman")

# Use pacman to load add-on packages as desired
pacman::p_load(pacman, rio, psych) 

p_help(psych, web = F)  # Opens help in R Viewer

# LOAD DATA FROM FILES ####################################

# set our working directory
setwd("S:\\Classes\\Introduction to Statistics\\Project1\\")

# set this to be the path to where all of our data lives
BASE_PATH <- ".\\data\\pre_proc_data\\train\\"

# get data for images in the train set & take a sneak peek in console
img_data_train <- import(paste(BASE_PATH, "image_data.csv", sep=""))
head(img_data_train)

# get data for objects in the train set & take a sneak peek in console
obj_data_train <- import(paste(BASE_PATH, "object_data.csv", sep=""))
head(obj_data_train)



# DATA VIEWER ##############################################
# opens up a spreadsheet viewer in r to see our data
?View
View(img_data_train)
View(obj_data_train)



# FIRST TOUCH ON DATA ######################################
# take a quick look at data to get an idea of what's going on
# try to identify interesting things

## Image Data
# describe each quantitative variable - first look at data distr.
describe(img_data_train)

# Object Count
describe(img_data_train$object_count) # get general details

# create bar plot 
object_count_images_train <- table(img_data_train$object_count)  # Create table
barplot(object_count_images_train)              # Bar chart
plot(object_count_images_train)                 # Default X-Y plot (lines)

# get box & whisker plot of object count
boxplot(img_data_train$object_count)

# Img width vs height
plot(img_data_train$width, img_data_train$height,
     col = "#cc0000",  # Hex code for datalab.cc red
     pch = 19,         # Use solid circles for points
     main = "Train Image Data: Image Width vs. Image Height",
     xlab = "Image Width",
     ylab = "Image Height")

plot(img_data_train$object_count, img_data_train$width,
     col = "#cc0000",  # Hex code for datalab.cc red
     pch = 19,         # Use solid circles for points
     main = "Train Image Data: Object Count vs. Image Width",
     xlab = "Image Object Count",
     ylab = "Image Width")

plot(img_data_train$object_count, img_data_train$height,
     col = "#cc0000",  # Hex code for datalab.cc red
     pch = 19,         # Use solid circles for points
     main = "Train Image Data: Object Count vs. Image Height",
     xlab = "Image Object Count",
     ylab = "Image Height")

plot(img_data_train$object_count, img_data_train$area,
     col = "#cc0000",  # Hex code for datalab.cc red
     pch = 19,         # Use solid circles for points
     main = "Train Image Data: Object Count vs. Image Area",
     xlab = "Image Object Count",
     ylab = "Image Area")

# show density of aspect ratios
describe(img_data_train$aspect_ratio_float)
aspect_ratio_f <- table(img_data_train$aspect_ratio_float)
barplot(aspect_ratio_f)              # Bar chart
plot(aspect_ratio_f)                 # Default X-Y plot (lines)
hist(img_data_train$aspect_ratio_float)

aspect_ratio <- table(img_data_train$aspect_ratio)
barplot(aspect_ratio)              # Bar chart
plot(aspect_ratio)                 # Default X-Y plot (lines)




# CLEAN UP #################################################

# Clear environment
rm(list = ls()) 

# Clear packages
p_unload(all)  # Remove all add-ons

# Clear console
cat("\014")  # ctrl+L

# Clear mind :)