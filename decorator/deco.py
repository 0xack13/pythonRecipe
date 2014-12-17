import time

#Define decorator
def time_dec(func):

  def wrapper(*arg):
      t = time.time()
      res = func(*arg)
      print func.func_name, time.time()-t
      return res

  return wrapper


@time_dec
def printFunction(n):
	print "Here is my func!"

printFunction(10)