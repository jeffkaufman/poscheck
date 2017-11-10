from poscheck import *

def unchecked(a, b):
    pass

@poscheck
def checked(a, b):
    pass

@poscheck
def one():
    return 1

@poscheck_except(1)
def partly_checked(a, b):
    pass

def start():
  unchecked(a=1, b=2)
  checked(a=1, b=2)
  unchecked(1, 2)
  partly_checked(a=1, b=2)
  partly_checked(1, b=2)

  assert(one()==1)

  caught_error = False
  try:
      checked(a=1, b=2, c=3)
  except TypeError:
      caught_error = True
  assert caught_error

  caught_error = False
  try:
      unchecked(a=1, b=2, c=3)
  except TypeError:
      caught_error = True
  assert caught_error

  caught_error = False
  try:
      checked(1, 2)
  except PositionalArgumentsError:
      caught_error = True
  assert caught_error

  caught_error = False
  try:
      partly_checked(1, 2)
  except PositionalArgumentsError:
      caught_error = True
  assert caught_error

  caught_error = False
  try:
      unchecked(1,2,3)
  except TypeError:
      caught_error = True
  assert caught_error

  caught_error = False
  try:
      checked(1,2,3)
  except PositionalArgumentsError:
      caught_error = True
  assert caught_error

  print "all tests passed"

if __name__ == "__main__":
    start()
