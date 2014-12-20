class Memoizer(object):
    """Caches the result of a function.
    """

    def __init__(self, function):
        self.function = function
        self.__name__ = function.__name__
        self.__doc__ = function.__doc__

        self.cached_values = {}

    def __call__(self, *fn_args,**fn_kwargs):
        """Wrapper for calling the Cached Function.
        """
        assert not fn_args, ("CachedMethod cannot be used with positional"
                             "arguments.")

        kwargs_sig = self.kwargs_signature(**fn_kwargs)

        if kwargs_sig not in self.cached_values:
            print "Calculating new value."
            self.cached_values[kwargs_sig] = self.function(**fn_kwargs )
        else:
            print "Returning cached value."

        return self.cached_values[kwargs_sig]

    def kwargs_signature(self, **fn_kwargs):
        """Returns kwargs signature--an immutable, given a set of kwargs. 
        """
        tp = tuple([v for k,v in sorted(fn_kwargs.items())])
        return str(tp.__hash__())

    def clear(self, **fn_kwargs):
        """Clears the cached data."""

        if not fn_kwargs:
            # Clear all if a set of kwargs was not specified.
            self.cached_values = {}
        else:
            # Otherwise just clear the value for the specified kwargs 
            # combination.
            kwargs_sig = self.kwargs_signature(**fn_kwargs)
            self.cached_values.pop(kwargs_sig, None)