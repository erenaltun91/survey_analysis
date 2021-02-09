
# Project 1 of the Data Scientist Nanodegree Program - Analysis of StackOverflow surveys

This project analyses the StackOverflow surveys from the year 2017 to 2020 and gives insight into specific questions. This insights will then be published on the 'Medium' platform.

## Installations
- Follow the link: https://insights.stackoverflow.com/survey
- Download the Data of the surveys from 2017 to 2020
- Put the files in this repo into a folder of your choice
- create another folder called 'data' into the chosen folder and put the downloaded survey csv-files in it, one after another. While doing this rename the surveys like written in the 'File Description'
- Install following python libraries:
    - pandas, numpy, matplotlib

`pip install numpy`  
`pip install pandas`  
`pip install matplotlib`  

- Run the main file

## Project Motivation
- In the course of the Data Scientist Nanodegree Prgram this analysis was done to be published on a social media platform ('Medium')
- It compares the participation on the survey of countries and genders between the years
- It compares the working hours per week and the age demographics in 2020 between the countries  

## File Descriptions

- Project 1 - Survey Analysis.ipynb
    - Main file with code
    - Starts analysis and saves plot into folder
    
- functions.py
    - Module with functions for the analysis
    
- X_survey_results.csv
    - Survey Data from https://insights.stackoverflow.com/survey
    - X: years from 2017 to 2020
    
- survey_results_schema.csv
    - Description of data
    
## Usage
- Run the Code in the ipynp-file
- The data will be read in from the 'data' directory
- The plots will be saved in the 'results' directory 

## Summary
- The analysis shows that the USA has the highest amount of participants and that the trend about the participation on the survey does not change
- The data on the genders shows, that the participants are mostly men. The other genders besides females decreased over the years
- For working hours per week you should choose Germany because it has the least number of working hours with an average of 39 working hours per week.
- The age demographics plots show that India has the youngest participants on average.

## Licensing, Authors, Acknowledgement

- This analysis was made by me, an Udacity student with the data provided by StackOverflow
- The results and the code can be used in any way
- Please contact me for feedback

### Contact: 
Medium: https://medium.com/@eren.altun  
LinkedIn: https://www.linkedin.com/in/eren-altun91/
