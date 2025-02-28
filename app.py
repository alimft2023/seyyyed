from models import Student
from flask import Flask,render_template

app = Flask(__name__)


@app.route('/')
def index():
    students=Student.select()
    return render_template('index.html',students=students)


if __name__=="__main__":
    app.run(debug=True)