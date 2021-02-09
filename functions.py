import pandas as pd
import numpy as np
import os
from matplotlib import pyplot as plt
import seaborn as sb

def read_survey(path,year):
    
    """
    Reads all survey - files in the directory
    
    INPUT: 
    year - str - year of the survey we want
    
    OUTPUT:
    df - DataFrame - Data of survey we want
    
    """
    os.chdir(path+"/data")
    for i in os.listdir():
        if ('survey' in i) & (year in i):
            df = pd.read_csv(i,engine='python')
    os.chdir(path)
    return df 
    
def gender_conversion(df):
    """
    Converts gender other than 'Female' and 'Male' to a category 'Other' to visualize it better
    
    INPUT:
    df - DataFrame - Dataframe with 'Gender' column
    
    OUTPUT:
    df - DataFrame - Dataframe with new 'Gender2' column
    """
    
    df.loc[(df['Gender'] == 'Male') | (df['Gender'] == 'Man') , 'Gender2'] = 'Male'
    df.loc[(df['Gender'] == 'Female') | (df['Gender'] == 'Woman') , 'Gender2'] = 'Female'
    df.loc[(df['Gender2']!= 'Male') & (df['Gender2'] !='Female'), 'Gender2'] = 'Other'
    
    return df

def plot_workinghours_per_week(df,country,hours_limit):
    """
    Plots the hours of work per week of a Dataframe of a specific country and prints the average working hours per week
    
    INPUT:
    df - DataFrame - DataFrame with a 'Country' column and a 'WorkWeekHrs' column
    country - str - Country of choice
    hours_limit - int - Limits the hours for filtering too high values
    
    OUTPUT:
    Plot - Histogram with the distribution of working hours per week
    Text - Prints the average working hours per week in each country
    """
    
    df[(df['Country']==country) & (df['WorkWeekHrs'] <= hours_limit)]['WorkWeekHrs'].hist()
    plt.title("Hours at Work per Week in "+country+" in 2020")
    plt.ylabel('Number of Participants')
    plt.xlabel('Hours at Work')
    print("The average hours of work per week in "+country+" is {}".format(np.round(df[(df['Country']==country) & (df['WorkWeekHrs'] <= hours_limit)]['WorkWeekHrs'].mean())))
     
def plot_age(df,country,age_limit):
    """
    Plots the age structure of a Dataframe of a specific country and prints the average age.
    Due to values < 18 the function filters them aout
    
    INPUT:
    df - DataFrame - DataFrame with a 'Country' column and a 'Age' column
    country - str - Country of choice
    age_limit - int - Limits the age for filtering too high values
    
    OUTPUT:
    Plot - Histogram with the distribution of working hours per week 
    Text - Prints the average age in each country
    """
    
    df[(df['Country']==country) & (df['Age'] >= 18) & (df['Age'] <= age_limit)]['Age'].hist()
    plt.title("Age demographics in "+country+" in 2020")
    plt.ylabel('Number of Participants')
    plt.xlabel('Age')
    print("The average age in "+country+" is {}".format(np.round(df[(df['Country']==country) & (df['Age'] >= 18) & (df['Age'] <= age_limit)]['Age'].mean())))
