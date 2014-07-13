class PositionalArgumentsError(Exception):
    def __init__(self, f):
        self.f = f
    def __str__(self):
        return "%s takes only keyword arguments" % self.f.__name__

def poscheck(f):
    def checked_f(*args, **kwargs):
        if args:
            raise PositionalArgumentsError(f)
        f(**kwargs)
    return checked_f
