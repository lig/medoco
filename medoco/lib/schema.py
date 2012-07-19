import json


class SchemaValidationError(Exception):
    pass


def _validate_doc(doc):
    if not isinstance(doc, dict):
        raise SchemaValidationError(
            'Document must have dictionary like structure.')

    for key, value in doc.items():

        if not isinstance(key, (str)):
            raise SchemaValidationError(
                'Property names must be strings.')

        _validate_value(value)


def _validate_value(value):

    if isinstance(value, dict):
        _validate_doc(value)
    elif isinstance(value, list):
        for item in value:
            _validate_value(item)
    elif not isinstance(value, str):
        raise SchemaValidationError('Property values must be type names.')


class DocumentSchema(object):

    def __init__(self, data):
        _validate_doc(data)
        self.data = data

    def to_json(self):
        return json.dumps(self.data)

    @classmethod
    def from_json(cls, json_data):
        return cls(json.loads(json_data))
