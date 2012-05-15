from mongoengine.document import __all__ as document_list
from mongoengine.fields import __all__ as field_list

from document import DocumentInfo
from field import FieldInfo


document_list = filter(lambda field: field.endswith('Document'), document_list)
_document_module = __import__('mongoengine.document', fromlist=['mongoengine'])
_document_data_module = __import__('medoco.lib.info.document_data',
    fromlist=['medoco', 'lib', 'info'])

for document_name in document_list:
    klass = getattr(_document_module, document_name)
    setattr(_document_data_module, document_name, DocumentInfo(klass))


field_list = filter(lambda field: field.endswith('Field'), field_list)
_field_module = __import__('mongoengine.fields', fromlist=['mongoengine'])
_field_data_module = __import__('medoco.lib.info.field_data',
    fromlist=['medoco', 'lib', 'info'])

for field_name in field_list:
    klass = getattr(_field_module, field_name)
    setattr(_field_data_module, field_name, FieldInfo(klass))
