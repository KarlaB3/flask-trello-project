from main import ma 

class CardSchema(ma.Schema):
    class Meta:
        fields = ("id", "title", "description","date","status","priority")

card_schema = CardSchema()
cards_schema = CardSchema(many=True)