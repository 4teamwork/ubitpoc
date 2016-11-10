from jsonschema import validate
from jsonschema import FormatChecker
import json


def validate_files(filename):
    with open('schema/{}.schema.json'.format(filename)) as schema_file:
        schema = json.load(schema_file)
    with open('example-data/{}.json'.format(filename)) as data_file:
        data = json.load(data_file)

    validate(data, schema, format_checker=FormatChecker())


validate_files('content')
validate_files('configuration')

print 'yeah! valid. well done chap!'
