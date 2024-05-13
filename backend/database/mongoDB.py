from mongoengine import Document, StringField, IntField

class Assistant(Document):
    name = StringField(required=True)
    mobile = IntField()
    email = StringField()
    salary = IntField()
    city = StringField()
    country = StringField()
    department = StringField()
    role = StringField()
