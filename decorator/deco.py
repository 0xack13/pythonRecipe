import time

def time_dec(func):

  def wrapper(*arg):
      t = time.time()
      res = func(*arg)
      print func.func_name, time.time()-t
      return res

  return wrapper


@time_dec
def myFunction(n):
	print "here is my func"

myFunction(10)