import unittest

from mongoengine.document import Document
from mongoengine.fields import ComplexDateTimeField

from medoco.lib.info import document_data, field_data
from medoco.lib.info.document import DocumentInfo
from medoco.lib.info.field import FieldInfo


class InfoTest(unittest.TestCase):

    def test_document_info(self):
        document_info = DocumentInfo(Document)
        self.assertEqual(document_info.klass, Document)
        self.assertEqual(document_info.name, 'Document')

    def test_field_info(self):
        """
        Based on the complicated ComplexDateTimeField that is twice subclassed
        """
        field_info = FieldInfo(ComplexDateTimeField)
        self.assertEqual(field_info.klass, ComplexDateTimeField)
        self.assertEqual(field_info.name, 'ComplexDateTimeField')
        self.assertListEqual(
            sorted(field_info.attrs),
            ['choices', 'db_field', 'default', 'help_text', 'max_length',
                'min_length', 'name', 'primary_key', 'regex', 'required',
                'separator', 'unique', 'unique_with', 'validation',
                'verbose_name'])

    def test_document_data_keys(self):
        self.assertListEqual(
            ['Document', 'DynamicDocument', 'DynamicEmbeddedDocument',
                'EmbeddedDocument'],
            sorted(document_data.keys()))

    def test_field_data_keys(self):
        self.assertListEqual(
            ['BinaryField', 'BooleanField', 'ComplexDateTimeField',
                'DateTimeField', 'DecimalField', 'DictField', 'EmailField',
                'EmbeddedDocumentField', 'FileField', 'FloatField',
                'GenericEmbeddedDocumentField', 'GenericReferenceField',
                'GeoPointField', 'ImageField', 'IntField', 'ListField',
                'MapField', 'ObjectIdField', 'ReferenceField', 'SequenceField',
                'SortedListField', 'StringField', 'URLField', 'UUIDField'],
            sorted(field_data.keys()))
