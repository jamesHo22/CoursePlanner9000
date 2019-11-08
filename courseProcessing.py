import pandas as pd
from pathlib import Path
# Read the data as a dataframe
cwd = Path.cwd()
filePath = Path(cwd / 'courseData/LIVE_Course_Catalog_Extract_UG19_20190722_for_SC.csv')
courseTable = pd.read_csv(filePath)

# Define graduation requirements
# Define code variables
SUB_CODE_ENGF = 'ENGR'
SUB_CODE_AHSE = 'AHSE'
SUB_CODE_MTH = 'MTH'
SUB_CODE_SCI = 'SCI'
SUB_CODE_SUST = 'SUST'
SUB_CODE_ADMN = 'ADMN'
# General Requirements
generalRequirementsCredits = {
    :
}
