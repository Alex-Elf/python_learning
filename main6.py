print((i for i in range(5)))

def foo():
  yield 1
  yield 2
  yield 0/0

it = foo()
print(next(it))
print(next(it))
#print(next(it))

try:
  print(next(it))
except StopIteration:
  print('Error')
except ZeroDivisionError:
  print("No zero division")
"""
for i in it:
  print i
"""
