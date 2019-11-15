class Major:
    '''
    Major class contains
    - required general courses
    - required general credits
    '''
    # # define required Courses
    # MAJOR_MECHE_COURSES = list()
    # MAJOR_MECHE_COURSES.append("COURSE1")
    # MAJOR_MECHE_COURSES.append("COURSE2")
    # MAJOR_MECHE_COURSES.append("COURSE3")
    # MAJOR_MECHE_COURSES.append("COURSE3")

    # CURRENT_COURSES = list()
    # CURRENT_COURSES.append("COURSE1")
    # CURRENT_COURSES.append("COURSE2")

    def __init__(self):
        '''
        initializes a Major object that contains all the 
        general requirement credits and required courses
        '''
        # TODO: Read a course requirement csv to determine the major requirements
        # Define code variables
        self.SUB_CODE_ENGR = 'ENGR'
        self.SUB_CODE_AHSE = 'AHSE'
        self.SUB_CODE_MTH = 'MTH'
        self.SUB_CODE_SCI = 'SCI'
        self.SUB_CODE_SUST = 'SUST'
        self.SUB_CODE_ADMN = 'ADMN'

        # Define a list of general courses
        self.generalRequiredCourses = []
        # General Requirements
        self.generalRequiredCredits = {
            self.SUB_CODE_ENGR: 46,
            self.SUB_CODE_MTH: 10,
            self.SUB_CODE_SCI: 20,
            self.SUB_CODE_AHSE: 28
        }
        
        
