from flask import Flask
from flask import render_template
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/course_dir/')
def course_dir():
    return render_template('course_dir.html')

@app.route('/roadmap/')
def roadmap():
    return render_template('roadmap.html')


if __name__ == '__main__':
    app.run()
