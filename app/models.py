from . import db

class User(db.Model):
    __tablename__ = 'users'
    id=db.Column(db.Integer,primary_key=True,nullable=False,unique=True)
    image=db.Column(db.String(256))
    username=db.Column(db.String(256))
    fname=db.Column(db.String(256))
    lname=db.Column(db.String(256))
    age=db.Column(db.String(256))
    sex=db.Column(db.String(256))
    highscore=db.Column(db.Integer)
    tdollars=db.Column(db.Integer)
    addedOn=db.Column(db.DateTime,nullable=False)
    

    def __init__(self, image, username, fname, lname, age, sex, addedOn):
        self.image = image
        self.username = username
        self.fname = fname
        self.lname = lname
        self.age = age 
        self.sex = sex
        self.highscore = 0
        self.tdollars = 0
        self.addedOn =addedOn
    
    def __repr__(self):
        return '<id {}>'.format(self.id)