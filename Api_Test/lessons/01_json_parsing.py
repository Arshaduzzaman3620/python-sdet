"""
Lesson 01 - JSON parsing
  - json.loads(): JSON *string*  -> Python dict
  - json.load():  JSON *file*    -> Python dict
  - Comparing two JSON files

Run from the Api_Test folder:
    python -m lessons.01_json_parsing
"""
import json

from utilities.configurations import TEST_DATA_DIR

courses = '{"name": "RahulShetty","languages": [ "Java", "Python"]}'

# loads method parses a json string and returns a dictionary
dict_courses = json.loads(courses)
print(type(dict_courses))
print(dict_courses)
print(dict_courses['name'])
# get me the first language taught by trainer
# list_language = dict_courses['languages']
# print(type(list_language))
# print(list_language[0])
print(dict_courses['languages'][0])

# ****** Parse content present in Json file
with open(TEST_DATA_DIR / 'course.json') as f:
    data = json.load(f)
    print(data)
    print(type(data))
    print(data['courses'][1]['title'])
    print(data['dashboard']['website'])
    print(type(data['dashboard']))
    # price of course 'RPA'
    print(type(data['courses']))
    for course in data['courses']:
        # print(course)
        if course['title'] == "RPA":
            print(course['price'])
            assert course['price'] == 45

# Compare two json files
with open(TEST_DATA_DIR / 'course1.json') as fi:
    data2 = json.load(fi)
    assert data == data2
