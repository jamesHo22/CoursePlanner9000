class User:
    def __init__(self):
        '''
        instantiates the MechE major specific course and credit requirements
        '''
        self.currentCourses = list()
    
    def addCourse(self, courseRowID):
        '''
        This function takes in a course code and adds it to a list.
        @param {str} courseRowID: the rowID for the course the user wishes to add to the schedule
        '''
        if courseRowID not in self.currentCourses:
            self.currentCourses.append(courseRowID)
    
    def getCurrentCourses(self):
        '''
        returns a list of all the current courses
        '''
        courses = dict()
        for i,v in enumerate(self.currentCourses):
            courses[i] = v
        return courses

    def clearCourses(self):
        '''
        Clear all the courses from the list
        '''
        self.currentCourses = list()
