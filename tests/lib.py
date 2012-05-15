import unittest

from mongoengine.document import Document
from mongoengine.fields import ComplexDateTimeField

from medoco.lib.info import document_list, field_list
from medoco.lib.info.document import DocumentInfo
from medoco.lib.info.field import FieldInfo


class InfoTest(unittest.TestCase):

    def test_document_list(self):
        self.assertListEqual(
            document_list,
            ['Document', 'EmbeddedDocument', 'DynamicDocument',
                'DynamicEmbeddedDocument'])

    def test_field_list(self):
        self.assertListEqual(
            field_list,
            ['StringField', 'IntField', 'FloatField', 'BooleanField',
                'DateTimeField', 'EmbeddedDocumentField', 'ListField',
                'DictField', 'ObjectIdField', 'ReferenceField', 'MapField',
                'DecimalField', 'ComplexDateTimeField', 'URLField',
                'GenericReferenceField', 'FileField', 'BinaryField',
                'SortedListField', 'EmailField', 'GeoPointField', 'ImageField',
                'SequenceField', 'UUIDField', 'GenericEmbeddedDocumentField'])

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
