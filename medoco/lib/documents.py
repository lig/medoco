from mongoengine import Document
from mongoengine.fields import StringField, DynamicField


class DocumentSpec(Document):
    name = StringField(max_length=255, required=True, unique=True)
    schema = DynamicField()
