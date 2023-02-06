from main import db

class Comment(db.Model):
    __tablename__= "COMMENTS"

    id = db.Column(db.Integer,primary_key=True)
    message = db.Column(db.String())
    user_id = db.Column(db.Integer, db.ForeignKey("USERS.id"), nullable=False)
    card_id = db.Column(db.Integer, db.ForeignKey("CARDS.id"), nullable=False)