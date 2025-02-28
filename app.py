from models import Student
from flask import Flask,render_template,redirect,url_for,request

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

@app.route('/create')
def create():
    if request.method == 'POST':
        n=request.form['name']
        f=request.form['family']
        Student.create(name=n,family=f)
        return redirect(url_for('index'))
    return render_template('create.html')

if __name__=="__main__":
    app.run(debug=True)