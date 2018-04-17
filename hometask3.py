def foo(store, number):
  store.sort(key = lambda i: i["price"], reverse = True)
  return store[:number]

print(foo([{"name": "bread", "price": 100},
    {"name": "wine", "price": 138},
    {"name": "meat", "price": 15},
    {"name": "water", "price": 1}], 2))
"""
[
    {"name": "wine", "price": 138},
    {"name": "bread", "price": 100}
]
"""
#######################################
print(foo([{"name": "pen", "price": 5},
    {"name": "whiteboard", "price": 170}], 1))
"""
[{"name": "whiteboard", "price": 170}]
"""

