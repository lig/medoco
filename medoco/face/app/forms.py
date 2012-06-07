from mongoforms import MongoForm

from medoco.lib.documents import DocumentSpec


class TypeForm(MongoForm):
    class Meta:
        document = DocumentSpec
