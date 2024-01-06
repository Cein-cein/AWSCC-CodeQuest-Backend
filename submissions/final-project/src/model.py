from . import db

class Passwords(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    website = db.Column(db.String(80), unique=False, nullable=False)
    email = db.Column(db.String(320), unique=False, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)

    def __repr__(self):
        return f"<Passwords {self.website}-{self.email}-{self.password}>"