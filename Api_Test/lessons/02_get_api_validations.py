"""
Lesson 02 - GET request + validations
  - requests.get() with query params
  - response.json(), status code, headers
  - Finding one item in a list response and comparing it

Run from the Api_Test folder:
    python -m lessons.02_get_api_validations
"""
import requests

from utilities.configurations import getConfig
from utilities.resources import ApiResources

url = getConfig()['API']['endpoint'] + ApiResources.getBook
response = requests.get(url, params={'AuthorName': 'Rahul Shetty'})
# print(response.text)
# print(type(response.text))
# dict_response = json.loads(response.text)
# print(dict_response[0]['isbn'])
json_response = response.json()
print(type(json_response))
print(json_response[0]['isbn'])
assert response.status_code == 200
print(response.headers)
assert response.headers['Content-Type'] == 'application/json;charset=UTF-8'

# Retrieve the book details with ISBN RGHCC
actualBook = None
for book in json_response:
    if book['isbn'] == 'RGHCC':
        actualBook = book
        print(actualBook)
        break

expectedBook = {
    "book_name": "Learn API Automation with RestAssured",
    "isbn": "RGHCC",
    "aisle": "12239"
}

assert actualBook == expectedBook
