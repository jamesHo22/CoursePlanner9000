import pandas as pd
from pathlib import Path
# Read the data as a dataframe
cwd = Path.cwd()
filePath = Path(cwd / 'courseData/LIVE_Course_Catalog_Extract_UG19_20190722_for_SC.csv')
courseTable = pd.read_csv(filePath)

# TODO: 
def checkRequiredCourses(requiredCourses, currentCourses):
    '''
    This method will take in a list of required courses and current courses and return the courses you still need
    '''
    li_dif = [i for i in requiredCourses + currentCourses if i not in requiredCourses or i not in currentCourses] 
    return li_dif 


 
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

