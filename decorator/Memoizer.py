def Memoizer(*args, **kwargs):
    """The outer wrapper for creating a object decorated."""
    import time

    class MemoizerObject(object):
        """Caches the result of a function.
        """
    
        def __init__(self, function, verbose=True):
            self.function = function
            self.__name__ = function.__name__
            self.__doc__ = function.__doc__
            
            self.verbose = verbose
            
            self.cached_values = {}
            self.statistics = {}
        
        def __call__(self, *fn_args, **fn_kwargs):
            """Wrapper for calling the Cached Function.
            """
            assert not fn_args, ("CachedMethod cannot be used with positional "
                              "arguments.")
            
            kwargs_sig = self.kwargs_signature(**fn_kwargs)
            
            # Calculate the new value, if needed and update the functional call
            # statistics
            if kwargs_sig not in self.cached_values:
                t1 = time.time()
                self.cached_values[kwargs_sig] = self.function(**fn_kwargs )
                t2 = time.time()
                
                # Update the statistics
                self.statistics['time_last_call'] = (t2-t1)*1000. # milliseconds
                self.statistics['number_of_calls'] = \
                    self.statistics.get('number_of_calls', 0) + 1
                
                if self.verbose:
                    print ("'{name}' calculated a new value which took "
                           " {time:.3f} ms.".format(name=self.__name__, 
                           time=self.statistics['time_last_call']))
            else:
                if self.verbose:
                    print ("'{name}' returned a cached "
                           "value.".format(name=self.__name__)) 
            
            return self.cached_values[kwargs_sig]
    
        def kwargs_signature(self, **fn_kwargs):
            """Returns kwargs signature--an immutable, given a set of kwargs. 
            """
            tp = tuple([v for k,v in sorted(fn_kwargs.items())])
            return str(tp.__hash__())
    
        def clear(self, **fn_kwargs):
            """Clears the cached data and statistics."""
            
            if not fn_kwargs:
                # Clear all if a set of kwargs was not specified.
                self.cached_values = {}
            else:
                # Otherwise just clear the value for the specified kwargs 
                # combination.
                kwargs_sig = self.kwargs_signature(**fn_kwargs)
                self.cached_values.pop(kwargs_sig, None)
                
            # Clear the statistics
            self.statistics.clear()

    def inner_decorator(function):
        return MemoizerObject(function, *args, **kwargs)
    return inner_decorator

@Memoizer(verbose=True)
def sum(a, b):
    return a+b

print sum(a=3,b=2)    # Function is evaluated, return value
print sum(a=3,b=2)    # Function returns cached value
sum.clear()           # The cached value is cleared
print sum(a=3,b=2)    # Function is evaluated, return value
print "{name} has been called {number} times.".format(name=sum.__name__,
    number=sum.statistics['number_of_calls'])