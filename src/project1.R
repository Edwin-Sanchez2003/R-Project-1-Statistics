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
BASE_PATH <- ".\\data\\pre_proc_data\\"

# get data for images in the train set & take a sneak peek in console
img_data_train <- import(paste(BASE_PATH, "train\\image_data.csv", sep=""))
head(img_data_train)

# get data for objects in the train set & take a sneak peek in console
obj_data_train <- import(paste(BASE_PATH, "train\\object_data.csv", sep=""))
head(obj_data_train)

# get data for images in the test set & take a sneak peek in console
img_data_test <- import(paste(BASE_PATH, "test\\image_data.csv", sep=""))
head(img_data_test)

# get data for objects in the test set & take a sneak peek in console
obj_data_test <- import(paste(BASE_PATH, "test\\object_data.csv", sep=""))
head(obj_data_test)

# get data for images in the validation set & take a sneak peek in console
img_data_validation <- import(paste(BASE_PATH, "validation\\image_data.csv", sep=""))
head(img_data_validation)

# get data for objects in the train set & take a sneak peek in console
obj_data_validation <- import(paste(BASE_PATH, "validation\\object_data.csv", sep=""))
head(obj_data_validation)

## OBJECT COUNT IN IMAGES ##################################
describe(img_data_train$object_count) # get general details
describe(img_data_validation$object_count) # get general details
describe(img_data_test$object_count) # get general details

# Put graphs in 3 rows and 1 column
par(mfrow = c(3, 1))

# create bar plot 
barplot(
  table(img_data_train$object_count), 
  main="Train Image Data: Object Count",
  xlab="Object Count",
  ylab="Frequency",
  ylim=c(0, 175))              # Bar chart
barplot(
  table(img_data_validation$object_count), 
  main="Validation Image Data: Object Count",
  xlab="Object Count",
  ylab="Frequency",
  ylim=c(0, 175)
  )         # Bar chart
barplot(
  table(img_data_test$object_count),
  main="Test Image Data: Object Count",
  xlab="Object Count",
  ylab="Frequency",
  ylim=c(0, 175))               # Bar chart


# get box & whisker plot of object count for each dataset
boxplot(
  img_data_train$object_count, 
  main="Train Image Data: Object Count",
  xlab="Object Count",
  ylim= c(0, 35), 
  horizontal = T)
boxplot(
  img_data_validation$object_count,
  main="Validation Image Data: Object Count",
  xlab="Object Count",
  ylim= c(0, 35), 
  horizontal = T)
boxplot(
  img_data_test$object_count,
  main="Test Image Data: Object Count",
  xlab="Object Count",
  ylim= c(0, 35), 
  horizontal = T)

# Restore graphic parameter
par(mfrow=c(1, 1))


## OBJECT DATA ##############################
describe(obj_data_train) # get general details
describe(img_data_validation) # get general details
describe(img_data_test) # get general details

par(mfrow = c(2, 1))
hist(obj_data_train$x)
hist(obj_data_train$y)
par(mfrow = c(1, 1))
plot(obj_data_train$x, obj_data_train$y,
     col = "#cc0000",  # Hex code for datalab.cc red
     pch = 19,         # Use solid circles for points
     main = "Train Object Data:Location of Objects",
     xlab = "X Location",
     ylab = "Y Location")

par(mfrow = c(2, 1))
hist(obj_data_train$x_norm)
hist(obj_data_train$y_norm)
par(mfrow = c(1, 1))
plot(obj_data_train$x_norm, obj_data_train$y_norm,
     xlim= c(0.0, 1.0),
     ylim= c(0.0, 1.0),
     col = "#cc0000",  # Hex code for datalab.cc red
     pch = 19,         # Use solid circles for points
     main = "Train Object Data: Normalized Location of Objects",
     xlab = "X Location (Normalized)",
     ylab = "Y Location (Normalized)")

## COMBO PLOTS FOR ALL 3 SETS ######################

# plot & compare normalized object locations
par(mfrow = c(2, 1))
hist(obj_data_validation$x_norm)
hist(obj_data_validation$y_norm)
par(mfrow = c(1, 1))
par(mfrow = c(2, 1))
hist(obj_data_test$x_norm)
hist(obj_data_test$y_norm)
par(mfrow = c(1, 1))

par(mfrow = c(2, 2))
plot(obj_data_train$x_norm, obj_data_train$y_norm,
     xlim= c(0.0, 1.0),
     ylim= c(0.0, 1.0),
     col = "#cc0000",  # Hex code for datalab.cc red
     pch = 19,         # Use solid circles for points
     main = "Train: Normalized Location of Objects",
     xlab = "X Location (Normalized)",
     ylab = "Y Location (Normalized)")

plot(obj_data_validation$x_norm, obj_data_validation$y_norm,
     xlim= c(0.0, 1.0),
     ylim= c(0.0, 1.0),
     col = "#cc0000",  # Hex code for datalab.cc red
     pch = 19,         # Use solid circles for points
     main = "Validation: Normalized Location of Objects",
     xlab = "X Location (Normalized)",
     ylab = "Y Location (Normalized)")

plot(obj_data_test$x_norm, obj_data_test$y_norm,
     xlim= c(0.0, 1.0),
     ylim= c(0.0, 1.0),
     col = "#cc0000",  # Hex code for datalab.cc red
     pch = 19,         # Use solid circles for points
     main = "Test: Normalized Location of Objects",
     xlab = "X Location (Normalized)",
     ylab = "Y Location (Normalized)")
par(mfrow = c(1, 1))
# CLEAN UP #################################################

# Clear environment
rm(list = ls()) 

# Clear packages
p_unload(all)  # Remove all add-ons

# Clear console
cat("\014")  # ctrl+L

# Clear mind :)

