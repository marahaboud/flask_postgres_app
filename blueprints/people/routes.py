from flask import render_template, redirect, request, url_for, Blueprint

from blueprints.app import db
from blueprints.people.models import Person

people = Blueprint('people', __name__, template_folder='templates')

@people.route('/')
def index():
    people = Person.query.all()
    return render_template('people/index.html', people=people)

@people.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'GET':
        return render_template('people/create.html')
    elif request.method == 'POST':
        name = request.form.get('name')
        age = request.form.get('age')
        job = request.form.get('job')

        person = Person(name=name, age=age, job=job)

        db.session.add(person)
        db.session.commit()
        return redirect(url_for('people.index'))
