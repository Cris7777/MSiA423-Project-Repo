# Project Repository

<!-- toc -->

- [Project Charter](#project-charter)
- [Project Backlog](#project-backlog)


<!-- tocstop -->

## Project Charter 

### Vision

The project provides a tool for virtual soccer teams founders to estimate scores of players in their teams, as well as to find players right for their teams.

### Mission

- The product enables users to predict overall scores for players in their teams based on combinations on different input attributes, which includes: age, weight, strength, stamina, etc.

- The product produces recommendations of players with predicted scores according to different positions.

### Success criteria 

**ML Metric**: 

- Predict player scores with Mean Squared Error of  lower than 10. 

**Business Metric**: 

- Over 80% of users select recommended players as members of their teams.

- No less than $100,000 of yearly revenue generated by payed service and advertisements.

## Project Backlog

### Project Themes

### Project Epics

**Main Page**

### Project Timeline

**Week 1-2: Data Processing**

- Exploratory Data Analysis

  * Data Overview

    The dataset contains information on over 18,000 players.

    + Minimum and Maximum
    + Mean and Median
    + Skewness
    + Influential Observations
    

  * Data Cleaning
      
      + NAs Removing
      + Duplicates Removing
      + Outliers Removing



- Model Building

  Train multiple models to predict scores of players, including both linear and non-linear models. 
  
  * Linear Regression
  * Neural Network
  * Random Forest
  * Decision Tree
  
  MSE is the measurement for model performance. The model with the lowest MSE will be selected as the final model deployed in the product.

**Week 3-8: APP Building**

Building pipelines and web APP.

**Week 9-10**

Test web APP, optimize user interfaces and write the final report.


<!--stackedit_data:
eyJoaXN0b3J5IjpbLTc5NjM4MzI4MCwxMTY4OTg2MTgsLTEyNz
UwNTg1ODgsLTE0MzMxMDY4MzgsLTE0OTk2MzcxNDYsLTIyOTA4
OTE1MSwxNzg4Nzk0MDE2LDE1MTk3NjcwNDQsLTk4MjU1MTYyNC
wtODg1MTk0MzYsNTU0NDc0ODM3LDE1NzAxMzU5MTIsMTc1ODEy
MzM5NywzMjgwOTA4MjUsNTkzNzE4ODQyLC0xMTQwODA5MTk3LD
c5OTMzODU0MCwtMTQyMzkyNTE0NF19
-->