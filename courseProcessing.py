import pandas as pd
from pathlib import Path
# Read the data as a dataframe
cwd = Path.cwd()
filePath = Path(cwd / 'courseData/LIVE_Course_Catalog_Extract_UG19_20190722_for_SC.csv')
courseTable = pd.read_csv(filePath)

# Define graduation requirements
# Define code variables
SUB_CODE_ENGR = 'ENGR'
SUB_CODE_AHSE = 'AHSE'
SUB_CODE_MTH = 'MTH'
SUB_CODE_SCI = 'SCI'
SUB_CODE_SUST = 'SUST'
SUB_CODE_ADMN = 'ADMN'
# General Requirements
generalRequirementsCredits = {
    SUB_CODE_ENGR: 46,
    SUB_CODE_MTH: 10,
    SUB_CODE_SCI: 20,
    SUB_CODE_AHSE: 28
}

def getAllCourses():
    return courseTable.values
 
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

