from app import db

class Students(db.Model):
    __tablename__ = 'students'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    school_grade = db.Column(db.Integer)
    course = db.Column(db.String())
    responsible_phone = db.Column(db.String())


    def __init__(self, name, school_grade, course, responsible_phone):
        self.name = name
        self.school_grade = school_grade
        self.course = course
        self.responsible_phone = responsible_phone

    def __repr__(self):
        return '<id {}>'.format(self.id)