from models import Student
from flask import Flask,render_template,redirect,url_for

app = Flask(__name__)


@app.route('/')
def index():
    students=Student.select()
    return render_template('index.html',students=students)

@app.route('/details/<int:id>')
def details(id):
    s=Student.get_by_id(id)
    return render_template('details.html',s=s)

@app.route('/delete/<int:id>')
def delete(id):
    s=Student.get_by_id(id)
    s.delete_instance()
    return redirect(url_for('index'))

if __name__=="__main__":
    app.run(debug=True)