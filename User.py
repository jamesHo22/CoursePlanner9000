class User:
    def __init__(self):
        '''
        instantiates the MechE major specific course and credit requirements
        '''
        self.currentCourses = list()
    
    def addCourse(self, courseCode):
        '''
        This function takes in a course code and adds it to a list.
        @param {str} courseCode: the code for the course the user wishes to add to the schedule
        
        '''
        self.currentCourses.append(courseCode)
    
    def getCurrentCourses(self):
        '''
        returns a list of all the current courses
        '''
        return self.currentCourses

    def clearCourses(self):
        '''
        Clear all the courses from the list
        '''
        self.currentCourses = list()
