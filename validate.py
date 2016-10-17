from jsonschema import validate
from jsonschema import FormatChecker
import json

with open('schema/repository.schema.json') as schema_file:
    schema = json.load(schema_file)

with open('example-data/repository.json') as data_file:
    data = json.load(data_file)

validate(data, schema, format_checker=FormatChecker())
print 'yeah! valid. well done chap!'
