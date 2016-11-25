from jsonschema import validate
from jsonschema import FormatChecker
import json


OGGBUNDLE_TYPES = (
    'reporoot',
    'repofolder',
    'dossier',
    'document',
)


def validate_data(document_name, schema_name):
    doc_fn = 'example-data/%s.json' % document_name
    with open(doc_fn) as data_file:
        data = json.load(data_file)

    schema_fn = 'schema/%s.json' % schema_name
    with open(schema_fn) as schema_file:
        schema = json.load(schema_file)

    try:
        validate(data, schema, format_checker=FormatChecker())
        print "%s - validation successful" % doc_fn
    except:
        print
        print "%s - validation failed" % doc_fn
        print
        raise


for type_name in OGGBUNDLE_TYPES:
    validate_data('%ss' % type_name, '%ss.schema' % type_name)

validate_data('configuration', 'configuration.schema')
