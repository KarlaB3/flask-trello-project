from main import db

class Card(db.Model):
    __tablename__= "CARDS"

    id = db.Column(db.Integer,primary_key=True)
    title = db.Column(db.String())
    description = db.Column(db.String())
    date = db.Column(db.Date())
    status = db.Column(db.String())
    priority = db.Column(db.String())
    user_id = db.Column(db.Integer, db.ForeignKey("USERS.id"), nullable=False)
    comments = db.relationship(
        "Comment",
        backref="card",
        cascade="all, delete"
    )