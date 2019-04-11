# Prediction and Recommendation on Players for Virtual Soccer Team

<!-- toc -->

- [Project Charter](#project-charter)
- [Project Backlog](#project-backlog)

<!-- tocstop -->

## Project Charter 

### Vision

The product is a web APP which provides a transparent and accurate tool for virtual soccer teams founders in any soccer video game to predict overall scores of players in their teams, as well as to find players right for their teams.

### Mission

Accuracy and transparency are product goals.

**Accuracy**

The product enables users to predict overall scores for players in their teams based on combinations on different input attributes, which includes: age, weight, strength, stamina, shot power, etc.

According to the predicted score, the product produces recommendations of players different positions to users.

**Transparency**

Users are available to monitor the process of prediction and recommendation when using the product. All scores, positions of players will be displayed.

### Success criteria 

**ML Metric**: 

- Less than 10 of Mean Squared Error to predict  scores of players

- More than 0.7 of R-Squared for the final model

**Business Metric**: 

- 80% of users select recommended players as members of their teams.

- $100,000 of yearly revenue generated by payed service and advertisements.

- 3000 active users after first year run of the product

- 0.8 Click Through Rate for users who open the product

## Project Backlog

### Home

This part provides a clear and overall description on all players. This part is the main page of the product and enables users to switch to any other function of the product.

**Epic 1: List Main Page Content**

- Story 1: Statistics on Player Information
  * Backlog
     + Provide a table of count of players by country on top of the page
     + Provide a pie chart of count of players by position
  * Icebox
    + Change static figures to dynamic figures
    + Add player pictures when opening the product

- Story 2: Advertisements 
  * Backlog
     + Provide a picture which links to an external product
  * Icebox
    + Add more advertisements to the main page
    + Scroll among advertisements automatically
    
**Epic 2: Switch to other Functions**

- Story 1: Switch to Prediction
  * Backlog
     + Show an icon at the bottom of the page which represents the function of prediction
     + Click on the prediction icon which connects to the page of prediction
  * Icebox
    + Change icon color on clicking

- Story 2: Switch to Recommendation
  * Backlog
     + Show an icon at the bottom of the page which represents the function of recommendation
     + Click on the prediction icon which connects to the page of recommendation
  * Icebox
    + Change icon color on clicking

- Story 3: Stay at Main Page
  * Backlog
     + Show an icon at the bottom of the page which represents main page
     + Click on the prediction icon which connects to the main page
  * Icebox
    + Change icon color on clicking

### Prediction

This part enables users to predict overall scores of players according to input attributes.

**Epic 1: Prediction Input**

- Story 1: Input Attributes
  * Backlog
    + Provide the blank to fill in player score of strength
    + Provide the blank to fill in player score of balance
    + Provide the blank to fill in player score of shot power
    + Provide the blank to fill in player score of stamina
    + Provide the blank to fill in player score of other significant variables
  * Icebox
    + Divide scores into different classes
    + Allow users to choose scores from a list

- Story 2: Go to Outcome
  * Backlog
    + Show a button which links to the outcome page
  * Icebox
    + Jump out a window to ask users confirm input data

**Epic 2: Prediction Outcome**

- Story 1: Provide Outcome
  * Backlog
    + Use the model to predicted score based on input attributes
    + Provide the score to the user
  * Icebox
    + Provide possible advantages of the player as well

- Story 2: Return to Input
  * Backlog
    + Show a button which links back to the attributes input page
  * Icebox
    + Jump out a window to ask users whether to save prediction of this time

**Epic 3: Switch to other Functions**

- Story 1: Stay at Prediction
  * Backlog
     + Show an icon at the bottom of the page which represents the function of prediction
     + Click on the prediction icon which connects to the page of prediction
  * Icebox
    + Change icon color on clicking

- Story 2: Switch to Recommendation
  * Backlog
     + Show an icon at the bottom of the page which represents the function of recommendation
     + Click on the prediction icon which connects to the page of recommendation
  * Icebox
    + Change icon color on clicking

- Story 3: Stay at Main Page
  * Backlog
     + Show an icon at the bottom of the page which represents main page
     + Click on the prediction icon which connects to the main page
  * Icebox
    + Change icon color on clicking

### Recommendation

This part recommends actual users for players to choose according to their previous input.

**Epic 1: Recommendation Filter**

- Story 1: Input Filter
  * Backlog
    + Provide the blank for users to fill in player position
    + Provide the blank for users to fill in player age
    + Provide the blank for users to fill in other possible conditions
  * Icebox
    + Allow users to choose scores from a list

- Story 2: Go to Outcome
  * Backlog
    + Show a button which links to the outcome page
  * Icebox
    + Jump out a window to ask users confirm input conditions

**Epic 2: Recommendation Outcome**

- Story 1: Provide Outcome
  * Backlog
    + Find players in the dataset of scores within 1 point range of predicted outcomes.
    + Filter closest players above by input conditions
    + Provide recommended players to the user
  * Icebox
    + Provide more information on the player, such as photo, nationality, club, etc.

- Story 2: Return to Input
  * Backlog
    + Show a button which links back to the filter input page
  * Icebox
    + Jump out a window to ask users whether to save prediction of this time
    + Jump out a window to ask users whether to use recommended players in the team

**Epic 3: Switch to other Functions**

- Story 1: Switch to Prediction
  * Backlog
     + Show an icon at the bottom of the page which represents the function of prediction
     + Click on the prediction icon which connects to the page of prediction
  * Icebox
    + Change icon color on clicking

- Story 2: Stay at Recommendation
  * Backlog
     + Show an icon at the bottom of the page which represents the function of recommendation
     + Click on the prediction icon which connects to the page of recommendation
  * Icebox
    + Change icon color on clicking

- Story 3: Stay at Main Page
  * Backlog
     + Show an icon at the bottom of the page which represents main page
     + Click on the prediction icon which connects to the main page
  * Icebox
    + Change icon color on clicking

### Project Timeline

**Week 1-2: Data Processing**

- Exploratory Data Analysis

  * Data Overview

    The dataset contains information on 18,207 players. Each player has unique ID and name with 85 attributes. The response variable is overall score and the rest of the attributes are possible independent variables. Overall description of the data includes following categories.

    + Descriptive Statistics
    
        Construct a summary on the data, including total count of observations, minimum value, maximum value, mean and median for each attribute.
        
    + Skewness
    
      Draw histograms for all attributes with numerical values to see the skewness. For models that require normal distribution, log transform attributes that are left or right skewed.
      
    + Influential Observations
    
        Check all observations with extreme values, for example, observations with some attributes of lower than 0 or larger than 100.

  * Data Cleaning
      
      + NAs Removing
       
         Remove observations having NA values for selected variables. 
         
      + Duplicates Removing
        
        Remove duplicated observations, which are defined as observations sharing the same unique player ID.
        
      + Outliers Removing
      
        Remove all abnormal observations that could have impact on parameters of the model.
      
      + Invalid Attributes Removing
     
        Remove attributes that will not be selected to build models, such as player ID, player photo, player nationality, player club and club logo.

- Model Building

  Split the dataset into training set and test set with proportions of 80% and 20% respectively. Use training set to fit multiple models to predict scores of players, including both linear and non-linear models. 
  
  * Linear Regression
  * Neural Network
  * Random Forest
  * Support Vector Machine
  
  MSE is the common measurement of performances for all models listed above. After running a 10-fold cross validation for 10-times, the model with the lowest mean MSE will be selected as the final model deployed in the product.

**Week 3-8: Product Building**

- [ ] Build pipelines

- [ ] Realize all functions of the product 

- [ ] Link different parts of the product together

**Week 9-10**

- [ ] Test the feasibility of the product 

- [ ] Optimize the product

- [ ] Write the final report

<!--stackedit_data:
eyJoaXN0b3J5IjpbLTE5NDQ2NzEyNTcsLTgyMzEzMDM5NSwtOT
M3OTQ0MCw4MDM5ODQ2ODMsMTc3NTgwNjM1MCw4NDkzMTc4OTQs
MTI1MjYzNjY1NywxOTg2NDg3Mjk4LC0xNzA4ODI3NDA5LDEwMz
QzMTYzMDcsNTEwMTc0NDI1LC0yMTA1OTM5Njg4LC0xODg5MDA5
MzQzLC04NTc3MzAyMDMsODU5NTIxNzgxLC0xMTUyMzI0NDIxLD
ExNjg5ODYxOCwtMTI3NTA1ODU4OCwtMTQzMzEwNjgzOCwtMTQ5
OTYzNzE0Nl19
-->