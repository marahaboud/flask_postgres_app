from app import db


# This class is going to be the person table in databse
# it inhertis from db.Model
class Person(db.Model):
    __tablename__= 'people'

    # here we define the columns we want in the table
    pid = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text, nullable=False)
    age = db.Column(db.Integer)
    job = db.Column(db.Text)

    # Return a string containing a printable representation of an object
    # https://docs.python.org/3/library/functions.html#repr
    def __repr__(self):
        if self.job:
            return f'Person with name {self.name} and age {self.age} has a job {self.job}'
        else:
            return f'Person with name {self.name} and age {self.age} with no job'

