from mongoengine.document import __all__ as _document_list
from mongoengine.fields import __all__ as _field_list

from document import DocumentInfo
from field import FieldInfo


def _init_data(class_list, class_sufix, me_module_name, info_class):
    class_list = filter(lambda field: field.endswith(class_sufix), class_list)
    module = __import__('mongoengine.%s' % me_module_name,
        fromlist=['mongoengine'])
    data = {}

    for name in class_list:
        klass = getattr(module, name)
        data[name] = info_class(klass)

    return data


document_data = dict(_init_data(
    _document_list, 'Document', 'document', DocumentInfo))

field_data = dict(_init_data(_field_list, 'Field', 'fields', FieldInfo))
