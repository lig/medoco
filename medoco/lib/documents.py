from mongoengine import Document
from mongoengine.document import EmbeddedDocument
from mongoengine.fields import (StringField, ListField, ReferenceField,
    RECURSIVE_REFERENCE_CONSTANT, DictField, EmbeddedDocumentField)

from .info import document_data, field_data


class FieldSpec(EmbeddedDocument):
    name = StringField(required=True)
    tipe = StringField(required=True, choices=field_data.keys())
    attrs = DictField()


class DocumentSpec(Document):
    name = StringField(required=True, unique=True)  # @note: primary_key?
    tipe = StringField(required=True, choices=document_data.keys())
    bases = ListField(ReferenceField(RECURSIVE_REFERENCE_CONSTANT))
    fields = ListField(EmbeddedDocumentField(FieldSpec))
