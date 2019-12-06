import pandas as pd
from pathlib import Path
import re
from datetime import datetime
import numpy as np
# Read the data as a dataframe


# TODO: 
def checkRequiredCourses(requiredCourses, currentCourses):
    '''
    This method will take in a list of required courses and current courses and return the courses you still need
    '''
    li_dif = [i for i in requiredCourses + currentCourses if i not in requiredCourses or i not in currentCourses] 
    return li_dif 


def getAllCourses():
    cwd = Path.cwd()
    filePath = Path(cwd / 'formattedCourses.csv')
    courseTable = pd.read_csv(filePath).values
    return courseTable
#%%
def getCourseInfo(text):
    '''
    Parses the description the 'Faculty / Schedule' column of the csv from my.olin.edu add/drop
    and creates a dataframe with the correct columns
    text: String, the text you want to parse. 
    '''
    # Import the table
    cwd = Path.cwd()
    filePath = Path(cwd / 'courseData/2019_S1_offering.csv')
    courseTable = pd.read_csv(filePath)
    # Split each line into an array
    eachLine = text.splitlines()
    # Iterate through each array and use RegEx to pick out the parts you need
    listOfCourses = list()
    for line in eachLine:
        
        # Parse the text to get usefull information
        
        instructorRegexPat = "(.*?)(?=\/)"

        instructorRegexPatAM = "(.*?) / ([a-zA-Z]+) (\d{2}:\d{2}[a-zA-Z]+)-(\d{2}:\d{2}[a-zA-Z]+); (.*)"
        instructorRegexPatPM = "(.*?) / ([a-zA-Z]+) (\d{2}:\d{2})-(\d{2}:\d{2}[a-zA-Z]+); (.*)"
        instructorRegexPatNoDays = "(.*?) / (\d{2}:\d{2})-(\d{2}:\d{2}[a-zA-Z]+); (.*)"
        matchedObject = re.match(instructorRegexPatAM, line)
        
        # This check here is intended to switch between AM and PM time patterns
        if matchedObject is None:
            matchedObject = re.match(instructorRegexPatPM, line)

        # handles weird case where there is a 00:00 time and no start date
        if "00:00-00:00AM;" in line:
            matchedObject = re.match(instructorRegexPatNoDays, line)
            instructor = matchedObject.group(1)
            day = None
            startTime = "01:00AM"
            endTime = "01:00AM"
            location = matchedObject.group(4)

        # Handles the normal cases
        else:
            instructor = matchedObject.group(1)
            day = matchedObject.group(2)
            startTime = matchedObject.group(3)
            endTime = matchedObject.group(4)
            location = matchedObject.group(5)

        # Add PM to the end of the startTime string so the format is the same for all time strings
        if "PM" in endTime and "AM" not in startTime:
            startTime = startTime + "PM"

        if "AM" in endTime and "AM" not in startTime:
            startTime = startTime + "AM"

        # Convert all the strings into the right data types
        startTime = getDateTime(startTime)
        endTime = getDateTime(endTime)
        daysOffered = getWeekdays(day)
        listOfCourses.append([instructor, daysOffered, startTime, endTime, location])
    return listOfCourses
#%%
def getDateTime(dateString):
    '''
    This function takes in the string that represents a time and returns a datetime object
    dateString: String, represents the time 00:00AM as an example
    '''
    dateObject = datetime.strptime(dateString, "%I:%M%p")
    # print(dateObject.time())
    return dateObject.time()
#%%
def getWeekdays(days):
    '''
    Given a string of characters, converts it into a boolean tuple with length of 7, 
    each representing whether or not the course is offered on each day
    days: String, with characters in MTWRT representing when each class is offered in the week
    returns: Tuple, indexed monday to friday in order. 1 means offered, 0 means not
    '''
    if days is None:
        return None
    else:
        daysDict = {
                "M":0,
                "T":0,
                "W":0,
                "R":0,
                "F":0,
            }
        
        listOfDays = list(days)
            
        for day in listOfDays:
            daysDict[day] = 1

    return daysDict.get("M"), daysDict.get("T"), daysDict.get("W"), daysDict.get("R"), daysDict.get("F") 

# Parse through the Facuilty/Schedule column and get all the info
#%%
def formatCourses():
    '''
    takes the course data from my.olin.edu and creates a table with the corrent columns
    '''
    cwd = Path.cwd()
    filePath = Path(cwd / 'courseData/2019_S1_offering.csv')
    courseTable = pd.read_csv(filePath)

    # Make new columns
    # instructor column
    counter = 0
    formattedColumns = ['Course Code', 'Name', 'Req', 'Credits','Begin Date', 'End Date', 'Instructor', 'M', 'T', 'W', 'R', 'F', 'start_time', 'end_time', 'location']
    formattedDataFrame = pd.DataFrame(columns=formattedColumns)
    descriptions = courseTable['Faculty / Schedule'].values
    for i in range(len(courseTable)):
        # Read all the values from the original dataframe
        courseCode = courseTable.iloc[i]['Course Code']
        name = courseTable.iloc[i]['Name']
        req = courseTable.iloc[i]['Req']
        numCredits = courseTable.iloc[i]['Credits']
        begin_date = datetime.strptime(courseTable.iloc[0]['Begin Date'], '%m/%d/%Y')
        end_date = datetime.strptime(courseTable.iloc[0]['End Date'], '%m/%d/%Y')
        
        listOfCourses = getCourseInfo(descriptions[i])
        for j in range(len(listOfCourses)):
            counter+=1
            instructor, days, startTime, endTime, location = listOfCourses[j]
            if days is not None:
                M,T,W,R,F = days
            else:
                M,T,W,R,F = 0,0,0,0,0
            newRow = pd.Series([courseCode, name, req, numCredits, begin_date, end_date, instructor, M, T, W, R, F, startTime, endTime, location], index=formattedColumns)
            print(newRow)
            formattedDataFrame.loc[counter] = newRow

    formattedDataFrame.to_csv("formattedCourses.csv")

# %%
def filterCourses():
    '''
    This function will take in some query parameters and filter the formatted courses
    returns: dictionary of all the courses and their information
    ''' 
# TODO:
# Make a SQL database with these columns
# ID (auto id), 
# STUDENT_REVIEW_ID (LATER),
# COURSE_CODE (string), 
# SUBJECT_CODE (string), 
# START_TIME (datetime),
# END_TIME (datetime),
# DAY_SUN, 
# DAY_MON, 
# DAY_TUES, 
# DAY_WED, 
# DAY_THURS, 
# DAY_FRI, 
# DAY_SAT,
# LOCATION,
# COURSE_NAME, 
# COURSE_DESCRIPTION, 
# PREREQUISITES, 
# CREDITS, 
# INSTRUCTORS, 
# SECTION,
# RECOMMENDED_PRERQUISITES,
# EST_HOURS,
# LAB (BOOLEAN),
# DATE_ADDED




