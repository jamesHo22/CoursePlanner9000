import pandas as pd
from pathlib import Path
import re
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
    filePath = Path(cwd / 'courseData/LIVE_Course_Catalog_Extract_UG19_20190722_for_SC.csv')
    courseTable = pd.read_csv(filePath).values
    return courseTable
#%%
def getCourseTimes(text):
    '''
    Looks for the start and end times of a course
    '''
    # Import the table
    cwd = Path.cwd()
    filePath = Path(cwd / 'courseData/2019_S1_offering.csv')
    courseTable = pd.read_csv(filePath)

    # while("" in instructors): 
    #     instructors.remove("")
    eachLine = text.splitlines()
    print(eachLine)
    for line in eachLine:
        # Parse the text to get usefull information
        timeRegexPat = "([a-zA-Z]+)\s(\d{2}):(\d{2})-(\d{2}):(\d{2})([A-Z]{2})"
        instructorRegexPat = "(.*?)(?=\/)"

        instructorRegexPatAM = "(.*?) / ([a-zA-Z]+) (\d{2}:\d{2}[a-zA-Z]+)-(\d{2}:\d{2}[a-zA-Z]+); (.*)"
        instructorRegexPatPM = "(.*?) / ([a-zA-Z]+) (\d{2}:\d{2})-(\d{2}:\d{2}[a-zA-Z]+); (.*)"
        matchedObject = re.match(instructorRegexPatAM, line)
        
        # This check here is intended to switch between AM and PM time patterns
        if matchedObject is None:
            matchedObject = re.match(instructorRegexPatPM, line)
        
        instructor = matchedObject.group(1)
        day = matchedObject.group(2)
        startTime = matchedObject.group(3)
        endTime = matchedObject.group(4)
        location = matchedObject.group(5)
    
        print(instructor, day, startTime, endTime, location)


    # timeList = list(filter(lambda a: ';' in a, filteredList))
    # nameList = list(filter(lambda a: ';' in a, filteredList))
    # not the prettiest way, but its fast
    
    # print(times)
    # print(instructors)

    # TODO: add 
    # start time column, 
    # end time column, 
    # instructors column, 
    # location column
    pass
#%%

# descriptions = courseTable['Faculty / Schedule'].values
# for i in range(3):
#     getCourseTimes(descriptions[i])
    
#%%

 
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

