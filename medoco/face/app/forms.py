from django.forms import CharField, Textarea
from mongoforms import MongoForm

from medoco.lib.documents import DocumentSpec


class DocumentSpecForm(MongoForm):

    class Meta:
        document = DocumentSpec
        fields = ('name')

    schema = CharField(widget=Textarea)
