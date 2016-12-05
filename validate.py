from jsonschema import FormatChecker
from jsonschema import validate
import codecs
import json


OGGBUNDLE_TYPES = (
    'reporoot',
    'repofolder',
    'dossier',
    'document',
)


def validate_data(document_name, schema_name):
    doc_fn = 'example-data/%s.json' % document_name
    print "Validating %-35s" % doc_fn,
    with codecs.open(doc_fn, 'r', 'utf-8-sig') as data_file:
            data = json.load(data_file)

    schema_fn = 'schema/%s.json' % schema_name
    with open(schema_fn) as schema_file:
        schema = json.load(schema_file)

    try:
        validate(data, schema, format_checker=FormatChecker())
        print " - success"
    except:
        print " - failed"
        print
        raise


for type_name in OGGBUNDLE_TYPES:
    validate_data('%ss' % type_name, '%ss.schema' % type_name)

validate_data('configuration', 'configuration.schema')
