"""
Lesson 03 - POST (add book) then POST (delete book)
  - Building the URL from config + resources
  - Sending a JSON body from a payload function
  - Chaining: use the ID from the add response to delete

Run from the Api_Test folder:
    python -m lessons.03_post_and_delete_api
"""
import requests

from utilities.configurations import getConfig
from utilities.payloads import addBookPayload
from utilities.resources import ApiResources

BASE_URL = getConfig()['API']['endpoint']
headers = {"Content-Type": "application/json"}

# Add Book
addBook_response = requests.post(
    BASE_URL + ApiResources.addBook,
    json=addBookPayload("fefrewe"),
    headers=headers,
)
print(addBook_response.json())
response_json = addBook_response.json()
print(type(response_json))

bookId = response_json['ID']
print(bookId)

# Delete Book
response_deleteBook = requests.post(
    BASE_URL + ApiResources.deleteBook,
    json={"ID": bookId},
    headers=headers,
)

assert response_deleteBook.status_code == 200
res_json = response_deleteBook.json()

print(res_json["msg"])
assert res_json["msg"] == "book is successfully deleted"
