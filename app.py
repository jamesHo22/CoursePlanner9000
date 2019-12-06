from flask import Flask, jsonify, render_template, request
from flask import render_template
from flask import jsonify
from flask import request
import courseProcessing as cp
import pandas as pd
import os

# Added a static folder where we can upload pictures
image_folder = os.path.join('static', 'image_folder')

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = image_folder

@app.route('/')
def home():
    # Allows me to display the logo onto the home page
    full_filename = os.path.join(app.config['UPLOAD_FOLDER'], 'logo.jpg')
    return render_template('home.html', logo = full_filename)

@app.route('/course_dir/')
def course_dir():
    courses = cp.getAllCourses()
    full_filename = os.path.join(app.config['UPLOAD_FOLDER'], 'logo.jpg')
    return render_template('course_dir.html', courses = courses, logo = full_filename)

@app.route('/roadmap/')
def roadmap():
    full_filename = os.path.join(app.config['UPLOAD_FOLDER'], 'logo.jpg')
    return render_template('roadmap.html', logo = full_filename)

# Test method for requesting data
@app.route('/_add_numbers')
def add_numbers():
    a = request.args.get('a', 0, type=int)
    b = request.args.get('b', 0, type=int)
    return jsonify(result=a * b)

@app.route('/_getAllCurrentCourses')
def getCurrentCourses():
    '''Returns json of all the courses'''
    pass

@app.route('/_addCourseById')
def addCourseById():
    '''Looks at request and adds the course ID to a list'''
    pass

@app.route('/_update_course_list')
def updateCourseList():
    '''Looks at request and adds the course ID to a list'''
    queryParamsDict = request.args.to_dict()
    filtGenGradReq = queryParamsDict['filtGenGradReq']
    filtMonday = queryParamsDict['M']
    filtTuesday = queryParamsDict['T']
    filtWednesday = queryParamsDict['W']
    filtThursday = queryParamsDict['R']
    filtFriday = queryParamsDict['F']
    
    # Build the query list
    queryList = []
    for i, v in queryParamsDict.items():
        if v == 'true':
            queryList.append(i)
        
    cp.filterCourses(queryList)
    print(queryList)
    return jsonify(result=queryParamsDict)


# Link to documentation page
@app.route('/documentation')
def documentation():
    full_filename = os.path.join(app.config['UPLOAD_FOLDER'], 'Untitled.png')
    return render_template('Documentation.html', diagram = full_filename)

if __name__ == '__main__':
    app.run(debug=True)
