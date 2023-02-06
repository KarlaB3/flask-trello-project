from main import ma
from marshmallow import fields

class CardSchema(ma.Schema):
    class Meta:
        ordered = True
        fields = ("id", "title", "description","date","status","priority", "user", "comments")
    user = fields.Nested("UserSchema", only=("email",))
    comments = fields.List(fields.Nested("CommentSchema"))

card_schema = CardSchema()
cards_schema = CardSchema(many=True)